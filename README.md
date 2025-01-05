# ddinstagram
Telegram bot which automatically converts lines to instagram videos from www.instagram.com to ddinstagram.com

## Desired usage flow:
You create telegram group and add telegram-bot (with administrative righs) there
You also add all necessary reciepents with which you are going to share instagram videos
Each time you are sharing instagram video by sending link in format "https://www.instagram.com/..." the message will be replaced with corresponding prefix "https://ddinstagram.com/..." which will allow reciepents to see videos right in the telegram.

# How to build

## Prerequisites
* Git - to download sources from github.com. See [Git's site](https://git-scm.com/downloads).
* Docker Engine - to build project and run it using docker. See [Docker's site](https://docs.docker.com/engine/install/ubuntu/).
* Telegram bot with actual token. See [Telegram's site](https://core.telegram.org/bots)

## Installation notes
1. Download sources of the project
   > git clone https://github.com/exadmin/ddinstagram
2. Go inside project folder
   > cd ddinstagram
3. Specify telegram bot token. Create "bot-token.txt" file with token value inside
   > echo '$token-value$' >> bot-token.txt
4. Run docker image build
   > sudo docker build -t tbot:0.0.1 ./
5. Check docker image is built successfully. Check logs and images
   > sudo docker image ls
6. Run application in detached (background) mode
   > sudo docker run -d tbot:0.0.1

