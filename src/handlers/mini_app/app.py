from aiogram import Router
from aiogram.types import Message

from CONFIG.CONFIG import db, logger, bot
from ...filters.OnlyCMD import OnlyCommand

router = Router()

@router.message(OnlyCommand(only_cmd='магазин'))
@logger.catch()
async def create_mini_app(message: Message):
    await message.answer('123')