import os
import random
from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.types import FSInputFile

from app import keyboards as kb
from app.database.requests import add_user
from aiogram import types
from text import start_text, instrukcia
sent_photos = {}

async def get_random_photo(user_id):
    photo_directory = './image'
    if user_id not in sent_photos:
        sent_photos[user_id] = []
    available_photos = [photo for photo in os.listdir(photo_directory) if photo not in sent_photos[user_id]]
    if not available_photos:
        sent_photos[user_id] = []
        available_photos = os.listdir(photo_directory)
    photo = random.choice(available_photos)
    sent_photos[user_id].append(photo)
    return os.path.join(photo_directory, photo)

router = Router()

@router.message(CommandStart())
async def cmd_start(message: types.Message):
    welcome_text = start_text
    await message.answer(welcome_text, reply_markup=await kb.main())

    await add_user(message.from_user.id)

@router.callback_query(F.data == 'main_menu')
async def back_to_main(call: CallbackQuery):
    welcome_text = start_text
    
    await call.message.answer(welcome_text, reply_markup=await kb.main())



@router.callback_query(F.data == 'registachia')
async def registachia(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer_photo(photo='AgACAgIAAxkBAAO1ZkCAPUSZKILZkD0DIwXkPT1eI2wAAiHXMRv_owFKnGaBfGqr3LcBAAMCAAN5AAM1BA', reply_markup=await kb.reg())

@router.callback_query(F.data == 'instuct')
async def instuct(callback: CallbackQuery):
    help_text = instrukcia
    await callback.answer()
    await callback.message.answer(help_text, reply_markup=await kb.regsitor())


@router.callback_query(F.data == 'signal')
async def process_signal(callback: CallbackQuery):
    photo_path = await get_random_photo(callback.from_user.id)
    photo = FSInputFile(photo_path)
    await callback.message.answer_photo(photo=photo, reply_markup=await kb.signal())
    await callback.answer()