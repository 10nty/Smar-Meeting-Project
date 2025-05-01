# README.md
# Smart Meeting Notes

Интеллектуальное приложение для протоколирования встреч, с поддержкой загрузки текста, аудио и Telegram-бота.

## 🚀 Возможности
- 📄 Загрузка текста для генерации протокола
- 🎤 Загрузка аудиофайлов (с последующим анализом/распознаванием)
- 🔐 JWT-авторизация
- 🤖 Telegram-бот (принимает текст, отправляет резюме)

## 📦 Установка
bash
python -m venv venv
source venv/bin/activate  # или venv\Scripts\activate на Windows
pip install -r requirements.txt


## 🧪 Запуск
bash
python run.py


- API: http://localhost:8000/docs
- Бот: Telegram → @your_bot_name

## 🛠 Используемые технологии
- FastAPI
- Python-Telegram-Bot
- JWT (jose, passlib)
- Возможность расширения: Whisper, OpenAI GPT

## 🔐 Авторизация
Для получения токена:
POST /token
Body (form): username, password


Затем использовать токен в Authorization: Bearer <your_token> для защищённых маршрутов.

## 📡 Пример запроса
bash
curl -X POST http://localhost:8000/upload_text/ \
-F "content=Сегодня мы обсудили приоритеты на следующий спринт..."


тут есть что мне нужно, точнее Bot_Token есть,