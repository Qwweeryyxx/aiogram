# перенести все from aiogram кроме Bot и Dispatcher
from aiogram import F, Router#<----тута добавить Router
#после чего создать router = Router()
# и заменить все dp на router
from aiogram.filters import Command
from aiogram.types import Message

import app.keyboards as kb

router = Router() # - это заменяет диспетчер 

# чтобы потом работало нужно ДОБАВИТЬ в основном файле, в функцию main() dp.include_router(router)
# у меня в моём примере это 64 строка (или 5 с конца если изменю файл и забуду переписать тут)
# а так же добавить в импорты основного файла from app.handlers import router


# перенести для модульности сюда все @dp из основного файла бота
@router.message(Command('start'))
async def start(message: Message):
    await message.answer(f"Привет! {message.from_user.first_name}\nТвой айди {message.from_user.id}\n напиши /help для спиская команд", reply_markup=kb.main)
    print("CommandStart")

@router.message(F.text == "хай")
async def m_hi(message: Message):
    await message.answer("Охаёшечки Даттебаёшечки!")
    print(1)

@router.message(F.photo)
async def get_photo(message: Message):
    await message.answer(f"ID фото: {message.photo[-1].file_id}")
    print(f"хэш полученного фото: {message.photo[-1].file_id}")
    print("получено фото")

@router.message(Command('get_photo'))
async def get_photo(message: Message):
    await message.answer_photo(photo="AgACAgIAAxkBAAMiasprpnVo4LE55M8AAVTxVsXBE-wfAAI6Imsbz8JQSrXbqEuhCfY1AQADAgADbQArouterQQ", 
                               caption="Смотри какая милая!")
    print("отправлено фото!")


@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer("""Это сообщение помогайка!:
/start - запуск бота
/help получить это сообщение
/get_photo - получить фото красивой мухи
отправь фото в чат и оно скажет его айди
/dianon - покажет все что знает о тебе""")
    print("cmd_help")

@router.message(Command('dianon'))
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