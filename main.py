import random
import time

from telebot.async_telebot import AsyncTeleBot

import asyncio
import requests
from telebot import asyncio_helper
# asyncio_helper.proxy = 'http://proxy.server:3128'

bot = AsyncTeleBot("6120958550:AAGRrg6tPTELgmvON1ItKIMYKLADO9BENPQ")

@bot.message_handler(commands=['start'])
async def start_message(message):
    await bot.send_message(message.chat.id, "Подписка на доллар")

@bot.message_handler(content_types=["text"])
async def start_finding(message):
    info = message.text.split(' ')
    if(info[0] == "доллар"):
        while True:
            time.sleep(random.randint(60, 180))
            if(info[1] >= get_binance_dol()):
                await bot.send_message(message.chat.id, f"Есть доллар по {get_binance_dol()}")



@bot.message_handler(commands=['get_data'])
async def send_rates(message):
    binance_dol = get_binance_dol()
    await bot.send_message(message.chat.id, f"dollar now: {binance_dol}")


#return first position of data
def get_binance_dol():
    url = 'https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search'

    headers = {
        'accept': '*/*',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    }

    params = {
        "proMerchantAds": False,
        "page": 1,
        "rows": 10,
        "payTypes": [],
        "countries": [],
        "publisherType": None,
        "tradeType": "BUY",
        "asset": "USDT",
        "transAmount": "",
        "fiat": "BYN"
    }

    response = requests.post(url=url, headers=headers, json=params).json()
    return response['data'][0]['adv']['price']







asyncio.run(bot.polling(none_stop=True, interval=0))