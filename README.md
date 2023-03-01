# Telegram bot for f-academy.ru

bot_link

## Description 

Telegram bot for academy project. 
Communicates with users and enrolls in academy courses.

## Usage

### Python running:

To run, you need to set up environment variables in the .env file

**DEBUG** - debug mode (1 or 0)

**TELEGRAM_TOKEN** - Telegram token

**LOGGING_PATH** - log path

```
pip install -r requirements.txt
python main.py
```

### Docker running:
```
docker-compose up --build -d
```

## Technologies used

- Python 3.10
- Aiogram
- Asyncio
- Docker