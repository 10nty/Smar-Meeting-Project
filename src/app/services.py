import tempfile

async def process_text(text: str) -> str:
    return f"[Протокол встречи на основе текста]: {text[:100]}..."

async def process_audio(file) -> str:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp:
        tmp.write(await file.read())
        path = tmp.name
    return f"[Аудио получено: {file.filename}] (файл сохранён как {path})"