# requiesites
# pip install pyTelegramBotAPI
# pip install aiohttp

import telebot
import os
from telebot.async_telebot import AsyncTeleBot
import asyncio
import sys

# read telegram bot from the file
try:
    with open('bot-token.txt', 'r') as file:
        botToken = file.read().replace('\n', '')
except OSError as e:
    print ("Error while reading bot token from bot-token.txt file. Please re-create image with this file.");
    sys.exit();

if not botToken:
    print ("No token is read from bot-token.txt file. Please re-create docker image with valid file content.")
    sys.exit()

# Starting bot in async mode
print ("Starting bot...")
bot = AsyncTeleBot(botToken)

@bot.message_handler()
async def make_some(message: telebot.types.Message):    
    if message.text.startswith("https://www.instagram.com"):
        newMsg = message.text.replace("https://www.instagram.com", "https://ddinstagram.com")
        await bot.delete_message(chat_id = message.chat.id, message_id = message.id)
        # await bot.edit_message_text(text = newMsg, chat_id = message.chat.id, message_id = message.id)
        await bot.send_message(message.chat.id, newMsg)

asyncio.run(bot.polling())