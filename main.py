import aiogram
import asyncio
import logging

from libxml2 import addEncodingAlias

from config import Token, banned_words, bad_words, good_words
from aiogram import Dispatcher, Bot, F
from aiogram.types import message, ChatMemberUpdated
from aiogram.filters import Command, IS_MEMBER, IS_NOT_MEMBER, ChatMemberUpdatedFilter
from aiogram.handlers import message, chat_member

bot = Bot(token=Token)
dp = Dispatcher()



@dp.message(Command("start"))
async def pisun_f6(message: message.Message):
    await message.reply("pisun f6")


@dp.chat_member(ChatMemberUpdatedFilter(IS_NOT_MEMBER >> IS_MEMBER))
async def zahod(event: ChatMemberUpdated, bot: Bot):
    await event.answer(f"привет, {event.from_user.full_name}\n"
                       f"если у тебя есть какие то вопросы, то для начала выполни следущие пункты:\n1. Убедись что вопрос не тупой\n"
                       f"2. Погугли хоть чуть чуть информацию по своей проблеме\n3. Сформулируй нормально и четко свой вопрос")

@dp.chat_member(ChatMemberUpdatedFilter(IS_MEMBER >> IS_NOT_MEMBER))
async def zahod(event: ChatMemberUpdated, bot: Bot):
    await event.answer(f"пользователь {event.from_user.full_name} вышел нахуй из этой пизды\nвот и правильно сделал блять")



@dp.message()
async def pidori(message: message.Message):

    if message.text.lower() in banned_words:
        await bot.send_message(chat_id=5017631350, text="хуйлан обнаруен (по тексту сообщения)")

    elif message.from_user.full_name in banned_words:
        await bot.send_message(chat_id=5017631350, text="хуйлан обнаружен (по нику)")

    elif  message.text.lower()  in bad_words:
        await message.reply('я тебя забаню🤑🤑🤑🤑🤑')

    elif "бандера" in message.text.lower():
        await message.answer_photo(photo="https://t.me/gd_ueban34/1090", message_effect_id="5046589136895476101")

    elif message.text.lower() in good_words:
        await message.bot.send_animation(chat_id=message.chat.id,
                                     animation="https://media.tenor.com/9POfFUzmiAgAAAAM/social-credit-meme.gif")

    if message.chat.full_name.lower() != "linux and tux chat":
        await bot.send_message(chat_id=5017631350, text=(f"{message.from_user.full_name}\n{message.from_user.full_name}"
                                                         f"({message.from_user.id}):{message.text}\n\n{message.chat.linked_chat_id}\n"
                                                         f"{message.chat.invite_link}\n{message.chat.id}"))



async def main():
    await dp.start_polling(bot)


while True:
    logging.basicConfig(level=logging.DEBUG)
    asyncio.run(main())