# **Задача:** при помощи виртуального окружения и PIP реализовать 
# решение задач с прошлых семинаров:

# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв".
# 2. Создайте программу для игры с конфетами человек против человека.
#  Условие задачи: На столе лежит 2021 конфета. Играют два игрока 
# делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента 
# достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, 
# чтобы забрать все конфеты у своего конкурента? 
#     a) Добавьте игру против бота   
#     b) Подумайте как наделить бота "интеллектом"

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
token_my = '5703063620:AAEI5-nzP9YYC7eO6X7cAntvcHh4u3t0FWw'

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def remove_abc(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    msg = update.message.text
    my_list = list(filter(lambda x: 'абв' not in x , msg.split()))
    await update.message.reply_text(' '.join(my_list))



app = ApplicationBuilder().token("Напишите свой токен").build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(MessageHandler(filters.TEXT, remove_abc))

app.run_polling()
