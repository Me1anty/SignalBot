from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

from aiogram import types
from text import link
async def main():
    inline_kb = types.InlineKeyboardMarkup(inline_keyboard=[
        [types.InlineKeyboardButton(text='📝 Регистрация', callback_data='registachia')],
        [types.InlineKeyboardButton(text='📖 Инструкция ', callback_data='instuct')],
        [types.InlineKeyboardButton(text='❗️Выдать сигнал❗️ ', callback_data='signal')]
    ])
    return inline_kb

async def reg():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='📰 Зарегистрироваться', url=link)],
        [InlineKeyboardButton(text='⏪ Главное меню', callback_data='main_menu')]
    ])

async def signal():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='📰 Зарегистрироваться', url=link)],
        [InlineKeyboardButton(text='❗️Выдать сигнал❗️', callback_data='signal')],
        [InlineKeyboardButton(text='⏪ Главное меню', callback_data='main_menu')]
    ])



async def regsitor():
    inline_kb = types.InlineKeyboardMarkup(inline_keyboard=[
        [types.InlineKeyboardButton(text='📝 Регистрация', callback_data='registachia')],
        [InlineKeyboardButton(text='⏪ Главное меню', callback_data='main_menu')]
    ])
    return inline_kb









