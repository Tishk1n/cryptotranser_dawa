from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from main import dp, types
import keyboards as kb
from order import keyboardcrypt as kbcr
from order import rukeyboardcrypt as rukbcr

###### АНГЛИЙСКАЯ ВЕРСИЯ
@dp.callback_query_handler(text='exchange')
async def makeanechange(callback: types.CallbackQuery):
    await callback.message.answer('<b>📤Choose the cryptocurrency you want to give</b>', reply_markup=kbcr.list_crypto, parse_mode='html')
    await callback.message.delete()

@dp.callback_query_handler(text='monxmr')
async def makeanechange(callback: types.CallbackQuery):
    await callback.message.answer('<b>📥Choose the cryptocurrency you want to get</b>', reply_markup=kbcr.list_crypto_monxmr, parse_mode='html')
    await callback.message.delete()

@dp.callback_query_handler(text='usdttrx')
async def makeanechange(callback: types.CallbackQuery):
    await callback.message.answer('<b>📥Choose the cryptocurrency you want to get</b>', reply_markup=kbcr.list_crypto_usdttrx, parse_mode='html')
    await callback.message.delete()

@dp.callback_query_handler(text='atomcosmos')
async def makeanechange(callback: types.CallbackQuery):
    await callback.message.answer('<b>📥Choose the cryptocurrency you want to get</b>', reply_markup=kbcr.list_crypto_atomcosmos, parse_mode='html')
    await callback.message.delete()

@dp.callback_query_handler(text='solanasol')
async def makeanechange(callback: types.CallbackQuery):
    await callback.message.answer('<b>📥Choose the cryptocurrency you want to get</b>', reply_markup=kbcr.list_crypto_solanasol, parse_mode='html')
    await callback.message.delete()

@dp.callback_query_handler(text='cardanoada')
async def makeanechange(callback: types.CallbackQuery):
    await callback.message.answer('<b>📥Choose the cryptocurrency you want to get</b>', reply_markup=kbcr.list_crypto_cardanoada, parse_mode='html')
    await callback.message.delete()

@dp.callback_query_handler(text='trontrx')
async def makeanechange(callback: types.CallbackQuery):
    await callback.message.answer('<b>📥Choose the cryptocurrency you want to get</b>', reply_markup=kbcr.list_crypto_trontrx, parse_mode='html')
    await callback.message.delete()

@dp.callback_query_handler(text='dogecoindoge')
async def makeanechange(callback: types.CallbackQuery):
    await callback.message.answer('<b>📥Choose the cryptocurrency you want to get</b>', reply_markup=kbcr.list_crypto_dogecoindoge, parse_mode='html')
    await callback.message.delete()

@dp.callback_query_handler(text='avalancheavax')
async def makeanechange(callback: types.CallbackQuery):
    await callback.message.answer('<b>📥Choose the cryptocurrency you want to get</b>', reply_markup=kbcr.list_crypto_avalancheavax, parse_mode='html')
    await callback.message.delete()

@dp.callback_query_handler(text='busdnb')
async def makeanechange(callback: types.CallbackQuery):
    await callback.message.answer('<b>📥Choose the cryptocurrency you want to get</b>', reply_markup=kbcr.list_crypto_busdnb, parse_mode='html')
    await callback.message.delete()

@dp.callback_query_handler(text='usdteth')
async def makeanechange(callback: types.CallbackQuery):
    await callback.message.answer('<b>📥Choose the cryptocurrency you want to get</b>', reply_markup=kbcr.list_crypto_usdteth, parse_mode='html')
    await callback.message.delete()

######### РУ ВЕРСИЯ
@dp.callback_query_handler(text='ruexchange')
async def makeanechange(callback: types.CallbackQuery):
    await callback.message.answer('<b>📤Выберите криптовалюту, которую хотите отдать</b>', reply_markup=rukbcr.ru_list_crypto, parse_mode='HTML')
    await callback.message.delete()

@dp.callback_query_handler(text='rumonxmr')
async def makeanechange(callback: types.CallbackQuery):
    await callback.message.answer('<b>📥Выберите криптовалюту, которую хотите получить</b>', reply_markup=rukbcr.ru_list_crypto_monxmr, parse_mode='html')
    await callback.message.delete()

@dp.callback_query_handler(text='ruusdttrx')
async def makeanechange(callback: types.CallbackQuery):
    await callback.message.answer('<b>📥Выберите криптовалюту, которую хотите получить</b>', reply_markup=rukbcr.ru_list_crypto_usdttrx, parse_mode='html')
    await callback.message.delete()

@dp.callback_query_handler(text='ruatomcosmos')
async def makeanechange(callback: types.CallbackQuery):
    await callback.message.answer('<b>📥Выберите криптовалюту, которую хотите получить</b>', reply_markup=rukbcr.ru_list_crypto_atomcosmos, parse_mode='html')
    await callback.message.delete()

@dp.callback_query_handler(text='rusolanasol')
async def makeanechange(callback: types.CallbackQuery):
    await callback.message.answer('<b>📥Выберите криптовалюту, которую хотите получить</b>', reply_markup=rukbcr.ru_list_crypto_solanasol, parse_mode='html')
    await callback.message.delete()

@dp.callback_query_handler(text='rucardanoada')
async def makeanechange(callback: types.CallbackQuery):
    await callback.message.answer('<b>📥Выберите криптовалюту, которую хотите получить</b>', reply_markup=rukbcr.ru_list_crypto_cardanoada, parse_mode='html')
    await callback.message.delete()

@dp.callback_query_handler(text='rutrontrx')
async def makeanechange(callback: types.CallbackQuery):
    await callback.message.answer('<b>📥Выберите криптовалюту, которую хотите получить</b>', reply_markup=rukbcr.ru_list_crypto_trontrx, parse_mode='html')
    await callback.message.delete()

@dp.callback_query_handler(text='rudogecoindoge')
async def makeanechange(callback: types.CallbackQuery):
    await callback.message.answer('<b>📥Выберите криптовалюту, которую хотите получить</b>', reply_markup=rukbcr.ru_list_crypto_dogecoindoge, parse_mode='html')
    await callback.message.delete()

@dp.callback_query_handler(text='ruavalancheavax')
async def makeanechange(callback: types.CallbackQuery):
    await callback.message.answer('<b>📥Выберите криптовалюту, которую хотите получить</b>', reply_markup=rukbcr.ru_list_crypto_avalancheavax, parse_mode='html')
    await callback.message.delete()

@dp.callback_query_handler(text='rubusdnb')
async def makeanechange(callback: types.CallbackQuery):
    await callback.message.answer('<b>📥Выберите криптовалюту, которую хотите получить</b>', reply_markup=rukbcr.ru_list_crypto_busdnb, parse_mode='html')
    await callback.message.delete()

@dp.callback_query_handler(text='ruusdteth')
async def makeanechange(callback: types.CallbackQuery):
    await callback.message.answer('<b>📥Выберите криптовалюту, которую хотите получить</b>', reply_markup=rukbcr.ru_list_crypto_usdteth, parse_mode='html')
    await callback.message.delete()