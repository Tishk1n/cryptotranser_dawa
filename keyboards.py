from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

ru = KeyboardButton('Русский')
en = KeyboardButton('English')
language = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(ru).add(en)
ReplyKeyboardRemove

exchange = KeyboardButton('Make an exchange', callback_data='exchange')
support = KeyboardButton('SUPPORT', callback_data='support', url='https://t.me/coinblinker_supprot')
reviews = KeyboardButton('REVIEWS', callback_data='reviews', url='https://coinblinker.com/en/reviews/')
rules = KeyboardButton('RULES', callback_data='rules', url='https://coinblinker.com/en/rules/')
faq = KeyboardButton('FAQ', callback_data='faq', url='https://coinblinker.com/en/faq/')
en_main_menu = InlineKeyboardMarkup().add(exchange).row(support, rules, faq, reviews)

ru_exchange = KeyboardButton('Провести обмен', callback_data='ruexchange')
ru_support = KeyboardButton('Поддержка', callback_data='support', url='https://t.me/coinblinker_supprot')
ru_reviews = KeyboardButton('Обзор', callback_data='reviews', url='https://coinblinker.com/en/reviews/')
ru_rules = KeyboardButton('Правила', callback_data='rules', url='https://coinblinker.com/en/rules/')
ru_faq = KeyboardButton('FAQ', callback_data='faq', url='https://coinblinker.com/en/faq/')
ru_main_menu = InlineKeyboardMarkup().add(ru_exchange).row(ru_support, ru_rules, ru_faq, ru_reviews)


