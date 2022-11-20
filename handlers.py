from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from main import dp, types
import keyboards as kb
from order import keyboardcrypt as kbcr

class Language(StatesGroup):
    language = State()


@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.answer('Привет! Выбери язык', reply_markup=kb.language)
    await Language.language.set()
    await message.delete()

@dp.message_handler(state=Language.language)
async def english_menu(message: types.Message, state: FSMContext):
    await message.answer('💱Welcome to Coinblinker Exchange!\n\n📈 Our advantages:\n1) Automatic exchange\n2) The most profitable course\n3) Responsive support', reply_markup=kb.en_main_menu)
    await Language.next()
    await message.delete()


@dp.callback_query_handler(text='back')
async def get_back(callback: types.CallbackQuery):
    await callback.message.answer('Loading menu...', reply_markup=kb.en_main_menu)
    await callback.message.delete()


@dp.callback_query_handler(text='rules')
async def makeanechange(callback: types.CallbackQuery):
    await callback.message.answer('https://coinblinker.com/en/rules/')
    await callback.message.delete()

@dp.callback_query_handler(text='reviews')
async def makeanechange(callback: types.CallbackQuery):
    await callback.message.answer('https://coinblinker.com/en/reviews/')
    await callback.message.delete()

@dp.callback_query_handler(text='faq')
async def makeanechange(callback: types.CallbackQuery):
    await callback.message.answer('https://coinblinker.com/en/faq/')
    await callback.message.delete()

@dp.callback_query_handler(text='support')
async def makeanechange(callback: types.CallbackQuery):
    await callback.message.answer('ты нажал пальчиком в анальчик')
    await callback.message.delete()
