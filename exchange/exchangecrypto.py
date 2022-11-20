from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()


monero = str(cg.get_price(ids='monero', vs_currencies='usd').get("monero").get("usd")).replace("{", "")
usdt = str(cg.get_price(ids='tether', vs_currencies='usd').get("tether").get("usd")).replace("{", "")
atom = str(cg.get_price(ids='cosmos', vs_currencies='usd').get("cosmos").get("usd")).replace("{", "")
doge = str(cg.get_price(ids='dogecoin', vs_currencies='usd').get("dogecoin").get("usd")).replace("{", "")
solana = str(cg.get_price(ids='solana', vs_currencies='usd').get("solana").get("usd")).replace("{", "")
cardano = str(cg.get_price(ids='cardano', vs_currencies='usd').get("cardano").get("usd")).replace("{", "")
tron = str(cg.get_price(ids='tron', vs_currencies='usd').get("tron").get("usd")).replace("{", "")
avalanche = str(cg.get_price(ids='avalanche-2', vs_currencies='usd').get("avalanche-2").get("usd")).replace("{", "")
busd = str(cg.get_price(ids='busd', vs_currencies='usd').get("busd").get("usd")).replace("{", "")
