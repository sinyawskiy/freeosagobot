#coding: utf8
from copy import copy

DATABASE_NAME = u'osagobot.sqlite'

FIRST_NAME = u'Страховое брокерское агенство'
LAST_NAME = u'Выбор'
PHONE_NUMBER = u'79272363738'


SEND_EMAIL = True
EMAIL_TO = u'igormitrakov@gmail.com'
EMAIL_FROM_USER = u'ufaosagobot@gmail.com'
EMAIL_FROM = u'<%s> "%s %s"' % (EMAIL_FROM_USER, FIRST_NAME, LAST_NAME)
EMAIL_FROM_PASSWORD=u'reRAtUWa93786'
EMAIL_SUBJECT = u'Расчёт ОСАГО (телеграм бот)'
EMAIL_TEXT = u'''
Расчёт выполнен успешно, контактные данные получены:
%(answers_text)s

Необходимо связаться.
'''

SUCCESS_TEXT = u'''Стоимость полиса ОСАГО:
%(osago_max).2f р.

Расчёт был произведён по стандартному КБМ.
Стоимость Вашего ОСАГО может уменьшиться
за счёт скидки за безаварийную езду.

Отправьте нам Ваш номер телефона для связи
'''

COMMANDS = {
    u'simple_cmd': u'/osago',
    u'simple_txt': u'Рассчитать ОСАГО',
    u'reset_cmd': u'/reset',
    u'reset_txt': u'На главную страницу',
    u'help_cmd': u'/help',
    u'help_txt': u'Справка'
}

URL="http://strahovka-ufa.ru/strahovka-ufa/"

WELCOME_ATTR = copy(COMMANDS)
WELCOME_ATTR.update({
    'first_name': FIRST_NAME,
    'last_name': LAST_NAME
})
WELCOME_TEXT = u'''Добро пожаловать!
Вас приветствует робот @StrahovkaUfaBot
Страховое брокерское агенство "Выбор"
КАСКО ОСАГО ДОМ КВАРТИРА

%(simple_cmd)s - %(simple_txt)s
%(reset_cmd)s - %(reset_txt)s
%(help_cmd)s - %(help_txt)s
''' % WELCOME_ATTR

HELP_TEXT = u'''Рассчитываются только легковые авто и только по региону Башкортостан, владелец только физическое лицо, условия страхования только стандартные. Срок страхования - только один год!

%(first_name)s "%(last_name)s"''' % {
    'first_name': FIRST_NAME,
    'last_name': LAST_NAME
}


# if __name__ == "__main__":
#     import smtplib
#     from email.mime.multipart import MIMEMultipart
#     from email.mime.text import MIMEText
#
#     msg = MIMEMultipart()
#     msg['From'] = EMAIL_FROM
#     msg['To'] = EMAIL_TO
#     msg['Subject'] = EMAIL_SUBJECT
#
#     msg.attach(MIMEText(EMAIL_TEXT.encode('utf8')))
#
#     mail_server = smtplib.SMTP('smtp.gmail.com', 587)
#     mail_server.ehlo()
#     mail_server.starttls()
#     mail_server.ehlo()
#     mail_server.login(EMAIL_FROM_USER, EMAIL_FROM_PASSWORD)
#     mail_server.sendmail(EMAIL_FROM, EMAIL_TO, msg.as_string())
#
#     mail_server.quit()