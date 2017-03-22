#coding: utf8
from copy import copy

DATABASE_NAME = u'osagobot.sqlite'

FIRST_NAME = u'Бесплатный расчёт'
LAST_NAME = u'ОСАГО'
PHONE_NUMBER = u'your_phone'


SEND_EMAIL = True
EMAIL_TO = u'your_email@gmail.com'
EMAIL_FROM_USER = u'your_email@gmail.com'
EMAIL_FROM = u'<%s> "%s %s"' % (EMAIL_FROM_USER, FIRST_NAME, LAST_NAME)
EMAIL_FROM_PASSWORD=u'your_secret'
EMAIL_SUBJECT = u'Расчёт ОСАГО (телеграм бот)'
EMAIL_TEXT = u'''
Расчёт выполнен успешно, контактные данные получены:
%(answers_text)s

Необходимо связаться.
'''

SUCCESS_TEXT = u'''Стоимость полиса ОСАГО:
%(osago_min).2f р.
%(osago_max).2f р.

Расчёт был произведён по стандартному КБМ.
Стоимость Вашего ОСАГО может уменьшиться
за счёт скидки за безаварийную езду.

Отправьте нам Ваш номер телефона для связи
'''

COMMANDS = {
    u'full_cmd': u'/full',
    u'full_txt': u'Рассчитать ОСАГО',
    u'simple_cmd': u'/osago',
    u'simple_txt': u'Рассчитать ОСАГО упрощенно',
    u'reset_cmd': u'/reset',
    u'reset_txt': u'На главную страницу',
    u'help_cmd': u'/help',
    u'help_txt': u'Справка'
}

URL="http://sinyawskiy.ru"

WELCOME_ATTR = copy(COMMANDS)
WELCOME_ATTR.update({
    'first_name': FIRST_NAME,
    'last_name': LAST_NAME
})
WELCOME_TEXT = u'''Добро пожаловать!
Вас приветствует робот @FreeOsagoBot

%(full_cmd)s - %(full_txt)s
%(simple_cmd)s - %(simple_txt)s
%(reset_cmd)s - %(reset_txt)s
%(help_cmd)s - %(help_txt)s
''' % WELCOME_ATTR

HELP_TEXT = u'''Рассчитываются только легковые авто и только по региону Санкт-Петербург, владелец только физическое лицо, условия страхования только стандартные. Срок страхования - только один год!

%(first_name)s "%(last_name)s"''' % {
    'first_name': FIRST_NAME,
    'last_name': LAST_NAME
}