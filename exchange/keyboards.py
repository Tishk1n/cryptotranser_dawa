from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from order.keyboardcrypt import back
from order.rukeyboardcrypt import ruback

ru_paid = KeyboardButton('Оплатил', callback_data='rupaid')
ru_orderkb = InlineKeyboardMarkup().add(ru_paid).add(ruback)

paid = KeyboardButton('Paid', callback_data='paid')
orderkb = InlineKeyboardMarkup().add(paid).add(back)