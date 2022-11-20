from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from main import dp, types
import keyboards as kb
from order import keyboardcrypt as kbcr

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