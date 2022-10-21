from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from loader import dp


# @dp.message_handler(CommandStart())
# async def bot_start(message: types.Message):
#     await message.answer(f"Salom, {message.from_user.full_name}!")

def check_user(func):
    async def wrapper_func(message):
        chat_id = message.from_user.id
        data = await dp.bot.get_chat_member(chat_id=-1001870472203,user_id=chat_id)
        print(data)
        if data.status in ["left","kicked"]:
            ink_menu = InlineKeyboardMarkup(row_width=2, inline_keyboard=[
        [
            InlineKeyboardButton(text="➕ A'zo bo'lish", url='https://t.me/error_bity'),
            InlineKeyboardButton(text="✅ Tasdiqlash", callback_data='check_user')
        ]
    ])
            await message.answer(f"Quyidagi kanallarimizga obuna boʻling. Botni keyin toʻliq ishlatishingiz mumkin!  {message.from_user.full_name}!", reply_markup=ink_menu)

            return False
        return func(message)
    return wrapper_func

@check_user
@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    user = message.from_user
    # await message.reply_video(video=open("handlers/users/data.mp4","rb"),caption="https://t.me/error_bity")
    data = await dp.bot.get_chat_member(chat_id=-1001870472203,user_id=message.from_user.id)

    if data.status in ["left","kicked"]:
        ink_menu = InlineKeyboardMarkup(row_width=2, inline_keyboard=[
            [
                InlineKeyboardButton(text="➕ A'zo bo'lish", url='https://t.me/error_bity'),
                InlineKeyboardButton(text="✅ Tasdiqlash", callback_data='check_user')
            ]
        ])
        await message.answer(f"Quyidagi kanallarimizga obuna boʻling. Botni keyin toʻliq ishlatishingiz mumkin!  {message.from_user.full_name}!", reply_markup=ink_menu)
    else:
        await message.answer(text="Video kochirish uchun link tashang")

# page = 'https://t.me/Code_Mates_Academy'
@dp.callback_query_handler()
async def start_button(call:types.CallbackQuery):
    chat_id = call.message.chat.id
    query = call.data
    if query == "check_user":
        data = await dp.bot.get_chat_member(chat_id=-1001870472203,user_id=chat_id)
        if data.status in ["left","kicked"]:
            await call.answer("Kechirasiz siz Kanalga a'zo bo'lmadingiz",show_alert=True)
        else:
            await call.message.delete()
            await dp.bot.send_message(chat_id=chat_id,text="Sz kanalga a'zo bo'lgan szi!!!")


