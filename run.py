import os
import asyncio
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
import aiosqlite
import logging

from app.handlers import router as user_router
from app.admin import admin as admin_router
from app.database.models import async_main

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def main():
    load_dotenv()
    
    await async_main()
    
    bot = Bot(token=os.getenv('TOKEN'))
    dp = Dispatcher()
    
    dp.include_routers(user_router, admin_router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')