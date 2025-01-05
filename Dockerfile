FROM python:3.8-slim

WORKDIR /usr/app/tbot

COPY ./telegram-bot.py ./
COPY ./bot-token.txt ./

RUN  pip install pyTelegramBotAPI \
 && pip install aiohttp \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

CMD ["python", "./telegram-bot.py"]