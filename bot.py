import asyncio
from aiogram import Bot, Dispatcher, F
from app.handlers import router

from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()
print("Bot started!")


async def main():
    dp.include_router(router)  #<-------
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())