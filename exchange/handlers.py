from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from main import dp, types
import keyboards as kb
from order import keyboardcrypt as kbcr
from exchange import exchangecrypto as ex

@dp.callback_query_handler(text=['monxmr2'])
async def makeanechange(callback: types.CallbackQuery):
    await callback.message.answer(f'Monero: {ex.monero}')
    await callback.message.delete()

@dp.callback_query_handler(text=['usdttrx2'])
async def makeanechange(callback: types.CallbackQuery):
    await callback.message.answer(f"USDT: {ex.usdt}")
    await callback.message.delete()

@dp.callback_query_handler(text=['atomcosmos2'])
async def makeanechange(callback: types.CallbackQuery):
    await callback.message.answer(f"ATOM: {ex.atom}")
    await callback.message.delete()

@dp.callback_query_handler(text=['solanasol2'])
async def makeanechange(callback: types.CallbackQuery):
    await callback.message.answer(f"SOLANA: {ex.solana}")
    await callback.message.delete()

@dp.callback_query_handler(text=['cardanoada2'])
async def makeanechange(callback: types.CallbackQuery):
    await callback.message.answer(f"Cardanoada: {ex.cardano}")
    await callback.message.delete()

@dp.callback_query_handler(text=['trontrx2'])
async def makeanechange(callback: types.CallbackQuery):
    await callback.message.answer(f"TRON: {ex.tron}")
    await callback.message.delete()

@dp.callback_query_handler(text=['dogecoindoge2'])
async def makeanechange(callback: types.CallbackQuery):
    await callback.message.answer(f"DOGECOIN: {ex.doge}")
    await callback.message.delete()

@dp.callback_query_handler(text=['avalancheavax2'])
async def makeanechange(callback: types.CallbackQuery):
    await callback.message.answer(f"AVALANCAEVA: {ex.avalanche}")
    await callback.message.delete()

@dp.callback_query_handler(text=['busdbnb2'])
async def makeanechange(callback: types.CallbackQuery):
    await callback.message.answer(f"BUSD: {ex.busd}")
    await callback.message.delete()

@dp.callback_query_handler(text=['usdteth2'])
async def makeanechange(callback: types.CallbackQuery):
    await callback.message.answer(f"USDT: {ex.usdt}")
    await callback.message.delete()