# Sticker statistics collector for the period in Telegram
[![ru](https://img.shields.io/badge/lang-ru-FFFFFF.svg)](README-RU.md)  
[![ru](https://img.shields.io/badge/lang-ru-1C3578.svg)](README-RU.md)  
[![ru](https://img.shields.io/badge/lang-ru-E4181C.svg)](README-RU.md)  
Almost all code got with AI!
## Prepare the environment for execution
```bash
python -m venv venv
source venv/bin/activate
python3 -m pip install --upgrade pip
pip install telethon asyncio pyyaml pandas matplotlib
```
You should also write to the bot [@Stickers](https://t.me/stickers) the message `/packstats` and select the pack for which you will need to collect statistics
### Setting up the parameters
Fill in the fields in the [config.yaml](config.yaml) file according to their examples

## Get data in statistics.csv
Messages will be sent through your account during the specified period - after successful completion of the program, all messages will be deleted
```bash
python3 receive_stat.py 
```

## Display the collected data
The red bars on the charts indicate weekends
```bash
python3 show_stat.py
```
