# coding: utf8
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from telebot import TeleBot, apihelper
from telebot.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, InlineQueryResultArticle, InputTextMessageContent, ReplyKeyboardRemove
import tornado
from tornado.httpserver import HTTPServer
from tornado.ioloop import PeriodicCallback, IOLoop
from tornado.queues import Queue, QueueEmpty
from tornado.web import RequestHandler, os
import time
from include.SQLiteHandler import SQLiteHandler
from include.questions import QUESTIONS, get_text_question, get_text_answer
from include.calculate import calculate
from config import WELCOME_TEXT, HELP_TEXT, DATABASE_NAME, COMMANDS, URL, PHONE_NUMBER, FIRST_NAME, LAST_NAME, SUCCESS_TEXT, SEND_EMAIL, EMAIL_FROM, EMAIL_TO, EMAIL_SUBJECT, EMAIL_TEXT, EMAIL_FROM_PASSWORD, EMAIL_FROM_USER


#https://github.com/sinyawskiy/freeosagobot.git

class SqlitePeriodicCallback(PeriodicCallback):
    def __init__(self, request_queue, response_queue, callback_time, io_loop=None):
        if callback_time <= 0:
            raise ValueError("Periodic callback must have a positive callback_time")
        self.callback_time = callback_time
        self.io_loop = io_loop or IOLoop.current()
        self._running = False
        self._timeout = None
        self.sql = SQLiteHandler(os.path.join(os.path.dirname(os.path.abspath(__file__)), DATABASE_NAME))
        self.sql.connect()
        self.request_queue = request_queue
        self.response_queue = response_queue

    def get_attr(self, message, attr):
        return self.sql.fetchOne(''' SELECT %(attr)s FROM osago WHERE chat_id=%(chat_id)s ORDER BY date DESC LIMIT 1;''' % {
            'chat_id': message['chat_id'],
            'attr': attr
        })[0]

    def set_answer(self, attr, questions, message):
        value = None
        item_date = self.get_attr(message, 'date')
        for question in questions:
            if question[1] == attr:
                for answer in question[2]:
                    if answer[0] == message['text']:
                        value = answer[1]
                        break

        if value is not None:
            #print attr, value
            row = self.sql.execute(''' UPDATE osago SET %(attr)s='%(value)s' WHERE chat_id=%(chat_id)s AND date = %(date)s''' % {
                'chat_id': message['chat_id'],
                'attr': attr,
                'value': value,
                'date': item_date
            })
            self.sql.commit()
        return

    def get_cities(self, region_id):
        for question in QUESTIONS:
            if question[1] == 'region':
                break
        for region in question[2]:
            if region[1] == u'%s' % region_id:
                if len(region)==3:
                    return [region[2]]
        return None

    def get_question_title(self, message):
        row = self.sql.fetchOne(''' SELECT vladelec, usloviya, tip_ts, moshnost, pricep, region, city, period_fl, period_ul, period_in, spisok, voditeli, kbm, narusheniya FROM osago WHERE chat_id=%(chat_id)s ORDER BY date DESC LIMIT 1;''' % message)
        question_title = None
        questions = QUESTIONS
        answers = map(None, ['vladelec', 'usloviya', 'tip_ts', 'moshnost', 'pricep', 'region', 'city', 'period_fl', 'period_ul', 'period_in', 'spisok', 'voditeli', 'kbm', 'narusheniya'], row)
        vladelec = answers[0][1] or None
        region = answers[5][1] or None
        spisok = answers[10][1] or None
        usloviya = answers[1][1] or None
        cities = self.get_cities(region) if region else None

        for answer in answers:
            if answer[1] == None:
                if answer[0] == 'city' and not cities:
                    pass
                elif answer[0] == 'pricep' and vladelec == '1' and usloviya == '1': # transit and fl
                    pass
                elif answer[0] in ['period_fl', 'period_ul', 'period_in', 'narusheniya', 'region', 'city'] and usloviya == '1': # transit
                    pass
                elif answer[0] in ['spisok', 'voditeli', 'kbm'] and vladelec == '2' and usloviya == '1': # transit and ul
                    pass
                elif answer[0] in ['period_fl', 'period_ul', 'spisok', 'voditeli', 'kbm', 'region', 'city', 'pricep'] and usloviya == '2':
                    pass
                elif answer[0] == 'period_fl' and vladelec == '2':
                    pass
                elif answer[0] == 'period_ul' and vladelec == '1':
                    pass
                elif answer[0] in ['voditeli','kbm'] and spisok == '2':
                    pass
                else:
                    question_title = answer[0]
                    break

        if question_title == u'city':
            questions = cities

        return question_title, questions, answers

    def get_progress(self, answers, question_title):
        answers_count = 0
        for answer in answers:
            answers_count += 1
            if answer[0]==question_title:
                break
        return int(answers_count*100/len(answers))

    def send_email(self, message):
        item_date = self.get_attr(message, 'date')
        row = self.sql.fetchOne('''SELECT first_name, last_name, username, phone_number, price, vladelec, usloviya, tip_ts, moshnost, pricep, region, city, period_fl, period_ul, period_in, spisok, voditeli, kbm, narusheniya FROM osago WHERE chat_id=%(chat_id)s AND date = %(date)s''' % {
            'chat_id': message['chat_id'],
            'date': item_date
        })
        answers = map(None, ['first_name', 'last_name', 'username', 'phone_number', 'price', 'vladelec', 'usloviya', 'tip_ts', 'moshnost', 'pricep', 'region', 'city', 'period_fl', 'period_ul', 'period_in', 'spisok', 'voditeli', 'kbm', 'narusheniya'], row)

        result = []
        for answer in answers:
            if answer[1] is not None:
                result.append(u'%s: %s' % (get_text_question(answer[0]), get_text_answer(answer[0], answer[1])))
        answers_text = u'\n'.join(result)


        msg = MIMEMultipart()
        msg['From'] = EMAIL_FROM
        msg['To'] = EMAIL_TO
        msg['Subject'] = EMAIL_SUBJECT

        msg.attach(MIMEText((EMAIL_TEXT % {'answers_text': answers_text}).encode('utf8')))

        mail_server = smtplib.SMTP('smtp.gmail.com', 587)
        mail_server.ehlo()
        mail_server.starttls()
        mail_server.ehlo()
        mail_server.login(EMAIL_FROM_USER, EMAIL_FROM_PASSWORD)
        mail_server.sendmail(EMAIL_FROM, EMAIL_TO, msg.as_string())

        mail_server.quit()

    def save_price(self, message, price):
        item_date = self.get_attr(message, 'date')
        row = self.sql.execute(''' UPDATE osago SET price='%(price)s'WHERE chat_id=%(chat_id)s AND date = %(date)s''' % {
            'chat_id': message['chat_id'],
            'price': u'%.2f' % price,
            'date': item_date
        })
        self.sql.commit()

    def save_contact(self, message):
        item_date = self.get_attr(message, 'date')
        row = self.sql.execute(''' UPDATE osago SET phone_number='%(phone_number)s', first_name='%(first_name)s', last_name='%(last_name)s' WHERE chat_id=%(chat_id)s AND date = %(date)s''' % {
            'chat_id': message['chat_id'],
            'first_name': message['first_name'],
            'last_name': message['last_name'],
            'phone_number': message['phone_number'],
            'date': item_date
        })
        self.sql.commit()

        if SEND_EMAIL:
            self.send_email(message)

    def get_question(self, message, start):
        markup = None
        question = ''
        question_title, questions, answers = self.get_question_title(message)

        if question_title and not start:
            self.set_answer(question_title, questions, message)
            question_title, questions, answers = self.get_question_title(message)

        #print question_title, questions, answers

        if not question_title:
            osago_min, osago_max, formula = calculate(answers)
            self.save_price(message, osago_max)
            question = SUCCESS_TEXT % {
                'osago_min': osago_min,
                'osago_max': osago_max,
                'formula': formula
            }
            markup = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
            phone_button = KeyboardButton(text="Отправить номер телефона", request_contact=True)
            reset_button = KeyboardButton(text=COMMANDS[u'reset_txt'])
            markup.add(reset_button)
            markup.add(phone_button)
            is_calc = True
        else:
            is_calc = False
            for question_item in questions:
                #print question_item[1], question_title, question_item[1] == question_title
                if question_item[1] == question_title:
                    question = u'%s? (%s %%)' % (question_item[0], self.get_progress(answers, question_title))
                    markup = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
                    for button_item in question_item[2]:
                        markup.add(KeyboardButton(text=button_item[0]))
                    break

        return question, markup, is_calc

    def queue_callback(self):
        #print 'sqlite_callback'
        try:
            message = self.request_queue.get_nowait()
        except QueueEmpty:
            pass
        else:
            start = False
            is_reset = False
            if message['text'] in [COMMANDS['full_cmd'], COMMANDS['full_txt']]:
                message.update({
                    'date': int(time.time()),
                    'kbm': '3',
                    'osago_type': 'full'
                })
                row = self.sql.execute(''' INSERT INTO osago (date, chat_id, username, first_name, last_name, osago_type) VALUES (%(date)s, '%(chat_id)s', '%(username)s', '%(first_name)s', '%(last_name)s', '%(osago_type)s');''' % message)
                start = True
            elif message['text'] in [COMMANDS['simple_cmd'], COMMANDS['simple_txt']]:
                message.update({
                    'date': int(time.time()),
                    'osago_type': 'simple',
                    'vladelec': '1',
                    'usloviya': '0',
                    'kbm': '3',
                    'tip_ts': 'b',
                    'region': '3',
                    'period_in': '10'
                })
                row = self.sql.execute(''' INSERT INTO osago (date, chat_id, username, first_name, last_name, vladelec, usloviya, tip_ts, region, period_in, osago_type, kbm) VALUES (%(date)s, '%(chat_id)s', '%(username)s', '%(first_name)s', '%(last_name)s', '%(vladelec)s', '%(usloviya)s', '%(tip_ts)s', '%(region)s', '%(period_in)s', '%(osago_type)s', '%(kbm)s');''' % message)
                start = True
            elif message['text'] in [COMMANDS['reset_cmd'], COMMANDS['reset_txt']]:
                markup = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
                # button_osago = KeyboardButton(text=COMMANDS['full_txt'])
                button_simple = KeyboardButton(text=COMMANDS['simple_txt'])
                # markup.add(button_osago)
                markup.add(button_simple)
                self.response_queue.put({
                    'chat_id':message['chat_id'],
                    'wait_message_id':message['wait_message_id'],
                    'message_text':WELCOME_TEXT,
                    'markup': markup
                })
                is_reset = True
            elif message['text'] == 'contact':
                self.save_contact(message)
                markup = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
                reset_button = KeyboardButton(text=COMMANDS[u'reset_txt'])
                markup.add(reset_button)
                self.response_queue.put({
                    'chat_id':message['chat_id'],
                    'wait_message_id':message['wait_message_id'],
                    'message_text': 'contact',
                    'markup': markup
                })
                is_reset = True

            if not is_reset:
                self.sql.commit()
                question, markup, is_calc = self.get_question(message, start=start)
                self.response_queue.put({
                    'chat_id':message['chat_id'],
                    'wait_message_id':message['wait_message_id'],
                    'message_text':question,
                    'markup': markup
                })
                if is_calc:
                    markup = InlineKeyboardMarkup()
                    url_button = InlineKeyboardButton(text="Перейти на наш сайт", url=URL)
                    markup.add(url_button)
                    question = u'Более подробную информацию Вы можете узнать на нашем сайте.'
                    self.response_queue.put({
                        'chat_id':message['chat_id'],
                        'wait_message_id':message['wait_message_id'],
                        'message_text': question,
                        'markup': markup
                    })
            self.request_queue.task_done()

    def _run(self):
        if not self._running:
            return
        try:
            return self.queue_callback()
        except Exception:
            self.io_loop.handle_callback_exception(self.queue_callback)
        finally:
            self._schedule_next()


class BotPeriodicCallback(PeriodicCallback):
    def __init__(self, bot, callback_time, io_loop=None):
        if callback_time <= 0:
            raise ValueError("Periodic callback must have a positive callback_time")
        self.callback_time = callback_time
        self.io_loop = io_loop or IOLoop.current()
        self._running = False
        self._timeout = None
        self.bot = bot

    def bot_callback(self, timeout=1):
        #print 'bot_callback'
        if self.bot.skip_pending:
            self.bot.skip_pending = False
        updates = self.bot.get_updates(offset=(self.bot.last_update_id + 1), timeout=timeout)
        self.bot.process_new_updates(updates)
        self.bot.send_response_messages()

    def _run(self):
        if not self._running:
            return
        try:
            return self.bot_callback()
        except Exception:
            self.io_loop.handle_callback_exception(self.bot_callback)
        finally:
            self._schedule_next()


class AppTeleBot(TeleBot, object):
    def __init__(self, token, request_queue, response_queue, threaded=True, skip_pending=False):
        super(AppTeleBot, self).__init__(token, threaded=True, skip_pending=False)
        self.request_queue = request_queue
        self.response_queue = response_queue

    def send_response_messages(self):
        try:
            message = self.response_queue.get_nowait()
        except QueueEmpty:
            pass
        else:
            self.send_chat_action(message['chat_id'], 'typing')
            if message['message_text'] == 'contact':
                self.send_contact(message['chat_id'], phone_number=PHONE_NUMBER, last_name=LAST_NAME, first_name=FIRST_NAME, reply_markup=message['markup'])
            else:
                self.send_message(message['chat_id'], message['message_text'], reply_markup=message['markup'])
            self.response_queue.task_done()

def main():
    TOKEN = '295287234:AAFMAAReWNpmj8Nrl7ioKnKIUoBOU8pWFbI'
    #SECRET = 'FMyFYphgQkSykstkjdQSgDhZqMk3DCzNNAPhDgJt'

    request_queue = Queue(maxsize=0)
    response_queue = Queue(maxsize=0)
    bot = AppTeleBot(TOKEN, request_queue, response_queue)
    info_api = bot.get_me()
    print info_api

    @bot.message_handler(commands=['start'])
    def send_welcome(message):
        keyboard_calc = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        # button_osago = KeyboardButton(text=COMMANDS['full_txt'])
        button_simple = KeyboardButton(text=COMMANDS['simple_txt'])
        # keyboard_calc.add(button_osago)
        keyboard_calc.add(button_simple)
        bot.send_message(message.chat.id, WELCOME_TEXT, reply_markup=keyboard_calc)

    @bot.message_handler(commands=['help'])
    def send_help(message):
        keyboard = InlineKeyboardMarkup()
        url_button = InlineKeyboardButton(text="Перейти на наш сайт", url=URL)
        keyboard.add(url_button)
        bot.send_message(message.chat.id, HELP_TEXT, reply_markup=keyboard)

    @bot.message_handler(func=lambda message: True, content_types=['text', 'contact'])
    def echo_all(message):
        # print message
        if message.content_type == 'text':
            markup = ReplyKeyboardRemove(selective=False)
            response = bot.send_message(message.chat.id,  u'Подождите...', reply_markup=markup)
            bot.request_queue.put({
                'text': message.text,
                'chat_id': message.chat.id,
                'username': message.chat.username,
                'first_name': message.chat.first_name,
                'last_name': message.chat.last_name,
                'message_id': message.message_id,
                'wait_message_id': response.message_id
            })
        else:
            markup = ReplyKeyboardRemove(selective=False)
            response = bot.send_message(message.chat.id,  u'Подождите...', reply_markup=markup)
            bot.request_queue.put({
                'text': 'contact',
                'chat_id': message.chat.id,
                'username': message.chat.username,
                'first_name': message.contact.first_name,
                'last_name': message.contact.last_name,
                'phone_number': message.contact.phone_number,
                'message_id': message.message_id,
                'wait_message_id': response.message_id
            })


    ioloop = tornado.ioloop.IOLoop.instance()

    BotPeriodicCallback(bot, 1000, ioloop).start()
    SqlitePeriodicCallback(request_queue, response_queue, 1000, ioloop).start()

    ioloop.start()


if __name__ == "__main__":
    main()