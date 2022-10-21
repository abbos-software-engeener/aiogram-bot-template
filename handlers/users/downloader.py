import os

from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from loader import dp, bot
from tiktok import tk
# from instagram import instadownloader
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.builtin import CallbackQuery
# from pytube import YouTube
from .start import check_user
from instagram import instadownloader
from pytube import YouTube



@dp.message_handler(Text(startswith='https://www.tiktok.com'))
# @check_user
async def test(message:types.Message):
    natija = tk(message.text)

    await message.answer_audio(natija['video'])


@dp.message_handler(Text(startswith='https://www.instagram.com/'))
# @check_user
async def send_media(message:types.Message):
    link1 = message.text
    data = instadownloader(link1=link1)
    if data == "Error":
        await message.answer('Bu URL manzil orqali hech narsa topolmadik!!')
    else:
        if data['type'] == 'image':
            await message.answer_photo(photo=data['media'])
        elif data['type'] == 'video':
            await message.answer_video(video=data['media'])
        elif data['type'] == 'carousel':
            for i in data['media']:
                await message.answer_document(document=i)
        else:

            await message.answer('Bu URL manzil orqali hech narsa topolmadik!!')



@dp.message_handler()
async def test_mesage(message:types.Message):
    chat_id = message.chat.id
    url = message.text
    yt = YouTube(url)
    if message.text.startswith == 'https://youtu.be/' or 'https"//www.youtube.com/':
        await bot.send_message(chat_id, f"Kutib tuting* : *{yt.title}*\n"
                                        f"*Kanal *: [{yt.author}]({yt.channel_url})")
        await download_youtube_video(url, message, bot)



async def download_youtube_video(url, message, bot):
    yt = YouTube(url)
    stream = yt.streams.filter(progressive=True, file_extension='mp4')
    stream.get_highest_resolution().download(f'{message.chat.id}', f'{message.chat.id}_{yt.title}')
    with open(f"{message.chat.id}/{message.chat.id}_{yt.title}", "rb") as video:
        # btn = InlineKeyboardMarkup(inline_keyboard=[
        #         [InlineKeyboardButton(text="Musiqasini yuklab olish", callback_data = "btn_1")]
        # ])
        await bot.send_video(message.chat.id, video, caption="* Video *")
        os.remove(f"{message.chat.id}/{message.chat.id}_{yt.title}")
