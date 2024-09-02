from aiogram import Bot, Dispatcher, types,F
from aiogram.types import Message ,ContentType,ErrorEvent
from aiogram.fsm.storage.memory import MemoryStorage
from db.db import DatabaseManager
from aiogram.utils.keyboard import ReplyKeyboardBuilder
import asyncio
from aiogram.types import FSInputFile
from aiogram.filters import Command
import subprocess
import logging
import os
from loader import dp,db,bot , BOT_TOKEN
from aiogram.handlers import ErrorHandler
from aiogram.filters import Filter  

ADMINS = [575089390,6057254437 ]

logger = logging.getLogger(__name__)
logging.basicConfig(filename='botlog.log',level=logging.DEBUG)
class MyFilter(Filter):
    def __init__(self) -> None:
        self.admins = ADMINS
    async def __call__(self, message: Message) -> bool:
        return message.from_user.id in self.admins


@dp.message(Command('adduser'),MyFilter())
async def adduser(message: Message):
    text = message.text
   
    text = text.replace('/adduser',' ').strip()
    await  message.answer('Add-user : '+ text)
    ADMINS.append(int(text))
  


@dp.message(Command('my'),MyFilter())
async def startcommand(message: Message):
  
   await message.answer('Hello! wwww')


     
    
async def send_message(channel_id: int, text: str):
    await bot.send_message(channel_id, text)
async def send_document(channel_id: int, filepath: str):
    doc = FSInputFile(filepath)
    await bot.send_document(channel_id, doc,caption='Парсинг закончен')
    
    

@dp.errors()
class MyHandler(ErrorHandler):
    async def handle(self):
        logger.exception(
            "Cause unexpected exception %s: %s",
            self.exception_name,
            self.exception_message
        )
@dp.message(F.document,MyFilter())
async def get_document(message: Message):
    await message.answer('Начинаю парсинг......')
    filepath = await bot.get_file(message.document.file_id)
    await message.bot.download_file(filepath.file_path,f'./files/{message.from_user.id}.xlsx')
    cwdir = os.getcwd()
    envcopy = os.environ.copy()
    command =  f'python parser.py -F ./files/{message.from_user.id} -B {BOT_TOKEN} -Chat {message.from_user.id} -O ./files/{message.from_user.id}new'
    proc =  subprocess.call(command,cwd=cwdir,env=envcopy,shell=True)
    
    
        
    
    
     

async def main():
    botinfo = await bot.get_me()
    
    print(botinfo)


   
    await dp.start_polling(bot)
if __name__ == '__main__':
  
   
  asyncio.run(main())
 
    