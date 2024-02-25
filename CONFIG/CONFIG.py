from aiogram import Bot, Dispatcher
from loguru import logger
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from CONFIG.CONFIG_BOT import TOKEN
from src.database.EasyDB import EasyDBCreator

schedule = AsyncIOScheduler(timezone="Europe/Moscow")

logger.add('logs/debug.log', format='{time} {level} {message}', level='DEBUG', compression='zip', rotation='1GB')

db = EasyDBCreator()
db.generate_db()

bot = Bot(TOKEN, parse_mode='HTML')
dp = Dispatcher()