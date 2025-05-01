import asyncio
import uvicorn
from app.telegram_bot import start_bot

async def main():
    # Запуск FastAPI-сервера в одной задаче
    server = asyncio.create_task(uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True))

    # Запуск Telegram-бота в другой задаче
    bot_task = asyncio.create_task(start_bot())

    # Ожидаем завершения обоих процессов
    await asyncio.gather(server, bot_task)

if __name__ == "__main__":
    # Запуск основного асинхронного процесса
    asyncio.run(main())