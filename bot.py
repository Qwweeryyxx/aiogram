import asyncio

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message
from app.handlers import router

from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()
print("Bot started!")

@dp.message(Command('start'))
async def start(message: Message):
    await message.answer(f"Привет! {message.from_user.first_name}\nТвой айди {message.from_user.id}\n напиши /help для спиская команд")
    print("CommandStart")

@dp.message(F.text == "хай")
async def m_hi(message: Message):
    await message.answer("Охаёшечки Даттебаёшечки!")
    print(1)

@dp.message(F.photo)
async def get_photo(message: Message):
    await message.answer(f"ID фото: {message.photo[-1].file_id}")
    print(f"хэш полученного фото: {message.photo[-1].file_id}")
    print("получено фото")

@dp.message(Command('get_photo'))
async def get_photo(message: Message):
    await message.answer_photo(photo="AgACAgIAAxkBAAMiasprpnVo4LE55M8AAVTxVsXBE-wfAAI6Imsbz8JQSrXbqEuhCfY1AQADAgADbQADPQQ", 
                               caption="Смотри какая милая!")
    print("отправлено фото!")


@dp.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer("""Это сообщение помогайка!:
/start - запуск бота
/help получить это сообщение
/get_photo - получить фото красивой мухи
отправь фото в чат и оно скажет его айди
/dianon - покажет все что знает о тебе""")
    print("cmd_help")

@dp.message(Command('dianon'))
async def dianon(message: Message):
    await message.answer(f"""вот все что я о тебе знаю:
имя: {message.from_user.first_name}\n
твой телеграмм айди: {message.from_user.id}
есть ли у тебя премиум?: {message.from_user.is_premium}
юзернейм: @{message.from_user.username}
""")
    audios = await message.from_user.get_profile_audios(
        offset=0,
        limit=10,
    )
    await message.answer(audios)
    return audios


async def main():
    dp.include_router(router)  #<-------
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())