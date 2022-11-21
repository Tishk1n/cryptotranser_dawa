from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from main import dp, types
import order.keyboardcrypt
import order.rukeyboardcrypt
from exchange import exchangecrypto as ex
from aiogram.types.input_file import InputFile
from exchange.keyboards import ru_orderkb, orderkb

@dp.callback_query_handler(text='rupaid')
async def paid(callback: types.CallbackQuery):
    await callback.message.answer('✅Ваш обмен был принят!\nОжидайте поступления криптовалюты на Ваш баланс.')

@dp.callback_query_handler(text='paid')
async def paid(callback: types.CallbackQuery):
    await callback.message.answer('✅Your exchange has been accepted!\nExpect to receive cryptocurrency on your balance.')


@dp.callback_query_handler(text=['rumonxmr2'])
async def makeanechange(callback: types.CallbackQuery):
    await callback.message.answer(f'Monero: {ex.monero}', reply_markup=ru_orderkb)
    await callback.message.answer_photo(InputFile('/Users/admin/Documents/GitHub/cryptotranser_dawa/order/qrcodes/monero.jpg'))
    await callback.message.delete()

@dp.callback_query_handler(text=['ruusdttrx2'])
async def makeanechange(callback: types.CallbackQuery):
    await callback.message.answer(f"USDT: {ex.usdt}", reply_markup=ru_orderkb)
    await callback.message.answer_photo(InputFile('/Users/admin/Documents/GitHub/cryptotranser_dawa/order/qrcodes/usdttrx.jpg'))
    await callback.message.delete()

@dp.callback_query_handler(text=['ruatomcosmos2'])
async def makeanechange(callback: types.CallbackQuery):
    await callback.message.answer(f"ATOM: {ex.atom}", reply_markup=ru_orderkb)
    await callback.message.answer_photo(InputFile('/Users/admin/Documents/GitHub/cryptotranser_dawa/order/qrcodes/atomcosmos.jpg'))
    await callback.message.delete()

@dp.callback_query_handler(text=['rusolanasol2'])
async def makeanechange(callback: types.CallbackQuery):
    await callback.message.answer(f"SOLANA: {ex.solana}", reply_markup=ru_orderkb)
    await callback.message.answer_photo(InputFile('/Users/admin/Documents/GitHub/cryptotranser_dawa/order/qrcodes/sloanasol.jpg'))
    await callback.message.delete()

@dp.callback_query_handler(text=['rucardanoada2'])
async def makeanechange(callback: types.CallbackQuery):
    await callback.message.answer(f"Cardanoada: {ex.cardano}", reply_markup=ru_orderkb)
    await callback.message.answer_photo(InputFile('/Users/admin/Documents/GitHub/cryptotranser_dawa/order/qrcodes/cardanoada.jpg'))
    await callback.message.delete()

@dp.callback_query_handler(text=['rutrontrx2'])
async def makeanechange(callback: types.CallbackQuery):
    await callback.message.answer(f"TRON: {ex.tron}", reply_markup=ru_orderkb)
    await callback.message.answer_photo(InputFile('/Users/admin/Documents/GitHub/cryptotranser_dawa/order/qrcodes/trontrx.jpg'))
    await callback.message.delete()

@dp.callback_query_handler(text=['rudogecoindoge2'])
async def makeanechange(callback: types.CallbackQuery):
    await callback.message.answer(f"DOGECOIN: {ex.doge}", reply_markup=ru_orderkb)
    await callback.message.answer_photo(InputFile('/Users/admin/Documents/GitHub/cryptotranser_dawa/order/qrcodes/dogecoindoge.jpg'))
    await callback.message.delete()

@dp.callback_query_handler(text=['ruavalancheavax2'])
async def makeanechange(callback: types.CallbackQuery):
    await callback.message.answer(f"AVALANCAEVA: {ex.avalanche}", reply_markup=ru_orderkb)
    await callback.message.answer_photo(InputFile('/Users/admin/Documents/GitHub/cryptotranser_dawa/order/qrcodes/avalancheavax.jpg'))
    await callback.message.delete()

@dp.callback_query_handler(text=['rubusdbnb2'])
async def makeanechange(callback: types.CallbackQuery):
    await callback.message.answer(f"BUSD: {ex.busd}", reply_markup=ru_orderkb)
    await callback.message.answer_photo(InputFile('/Users/admin/Documents/GitHub/cryptotranser_dawa/order/qrcodes/busdbnb.jpg'))
    await callback.message.delete()

@dp.callback_query_handler(text=['ruusdteth2'])
async def makeanechange(callback: types.CallbackQuery):
    await callback.message.answer(f"USDT: {ex.usdt}", reply_markup=ru_orderkb)
    await callback.message.answer_photo(InputFile('/Users/admin/Documents/GitHub/cryptotranser_dawa/order/qrcodes/usdteth.jpg'))
    await callback.message.delete()

##################### ENGLISH VERSION

@dp.callback_query_handler(text=['monxmr2'])
async def makeanechange(callback: types.CallbackQuery):
    await callback.message.answer(f'Monero: {ex.monero}', reply_markup=orderkb)
    await callback.message.answer_photo(InputFile('/Users/admin/Documents/GitHub/cryptotranser_dawa/order/qrcodes/monero.jpg'))
    await callback.message.delete()

@dp.callback_query_handler(text=['usdttrx2'])
async def makeanechange(callback: types.CallbackQuery):
    await callback.message.answer(f"USDT: {ex.usdt}", reply_markup=orderkb)
    await callback.message.answer_photo(InputFile('/Users/admin/Documents/GitHub/cryptotranser_dawa/order/qrcodes/usdttrx.jpg'))
    await callback.message.delete()

@dp.callback_query_handler(text=['atomcosmos2'])
async def makeanechange(callback: types.CallbackQuery):
    await callback.message.answer(f"ATOM: {ex.atom}", reply_markup=orderkb)
    await callback.message.answer_photo(InputFile('/Users/admin/Documents/GitHub/cryptotranser_dawa/order/qrcodes/atomcosmos.jpg'))
    await callback.message.delete()

@dp.callback_query_handler(text=['solanasol2'])
async def makeanechange(callback: types.CallbackQuery):
    await callback.message.answer(f"SOLANA: {ex.solana}", reply_markup=orderkb)
    await callback.message.answer_photo(InputFile('/Users/admin/Documents/GitHub/cryptotranser_dawa/order/qrcodes/sloanasol.jpg'))
    await callback.message.delete()

@dp.callback_query_handler(text=['cardanoada2'])
async def makeanechange(callback: types.CallbackQuery):
    await callback.message.answer(f"Cardanoada: {ex.cardano}", reply_markup=orderkb)
    await callback.message.answer_photo(InputFile('/Users/admin/Documents/GitHub/cryptotranser_dawa/order/qrcodes/cardanoada.jpg'))
    await callback.message.delete()

@dp.callback_query_handler(text=['trontrx2'])
async def makeanechange(callback: types.CallbackQuery):
    await callback.message.answer(f"TRON: {ex.tron}", reply_markup=orderkb)
    await callback.message.answer_photo(InputFile('/Users/admin/Documents/GitHub/cryptotranser_dawa/order/qrcodes/trontrx.jpg'))
    await callback.message.delete()

@dp.callback_query_handler(text=['dogecoindoge2'])
async def makeanechange(callback: types.CallbackQuery):
    await callback.message.answer(f"DOGECOIN: {ex.doge}", reply_markup=orderkb)
    await callback.message.answer_photo(InputFile('/Users/admin/Documents/GitHub/cryptotranser_dawa/order/qrcodes/dogecoindoge.jpg'))
    await callback.message.delete()

@dp.callback_query_handler(text=['avalancheavax2'])
async def makeanechange(callback: types.CallbackQuery):
    await callback.message.answer(f"AVALANCAEVA: {ex.avalanche}", reply_markup=orderkb)
    await callback.message.answer_photo(InputFile('/Users/admin/Documents/GitHub/cryptotranser_dawa/order/qrcodes/avalancheavax.jpg'))
    await callback.message.delete()

@dp.callback_query_handler(text=['busdbnb2'])
async def makeanechange(callback: types.CallbackQuery):
    await callback.message.answer(f"BUSD: {ex.busd}", reply_markup=orderkb)
    await callback.message.answer_photo(InputFile('/Users/admin/Documents/GitHub/cryptotranser_dawa/order/qrcodes/busdbnb.jpg'))
    await callback.message.delete()

@dp.callback_query_handler(text=['usdteth2'])
async def makeanechange(callback: types.CallbackQuery):
    await callback.message.answer(f"USDT: {ex.usdt}", reply_markup=orderkb)
    await callback.message.answer_photo(InputFile('/Users/admin/Documents/GitHub/cryptotranser_dawa/order/qrcodes/usdteth.jpg'))
    await callback.message.delete()