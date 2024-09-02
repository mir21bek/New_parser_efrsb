
from aiogram import Bot, Dispatcher, types,F
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.default import DefaultBotProperties
from db.db import DatabaseManager
BOT_TOKEN = '7492954991:AAGEYDF-1pmuqfJEzgETUdASmwBpP5itmE8'

storage = MemoryStorage()
dp = Dispatcher(storage=storage)

db = DatabaseManager('db/database.db')
bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode='HTML'))

