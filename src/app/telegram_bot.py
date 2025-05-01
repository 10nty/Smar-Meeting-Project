import os
import asyncio
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from dotenv import load_dotenv
from pathlib import Path

# Загружаем переменные окружения из .env
env_path = Path(__file__).resolve().parent.parent
load_dotenv(dotenv_path=env_path / '.env')

BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN не задан! Убедись, что он есть в .env")

# Включаем логирование
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.DEBUG)

# Обработчик команды /start
async def start(update, context):
    print(f"Получено сообщение от {update.message.from_user.username}")
    await update.message.reply_text("Бот запущен!")

# Обработчик обычных сообщений
async def handle_message(update, context):
    print(f"Получено сообщение: {update.message.text}")  # Логируем текст сообщения
    await update.message.reply_text(f"Ты сказал: {update.message.text}")

# Основная функция для запуска бота
async def start_bot():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    await app.run_polling()