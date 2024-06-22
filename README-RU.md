# Сборщик статистики по стикерам за период в Telegram
Почти весь код получен через ИИ!
## Подготовить среду для выполнения
```bash
python -m venv venv
source venv/bin/activate
python3 -m pip install --upgrade pip
pip install telethon asyncio pyyaml pandas matplotlib
```
Вы должны также написать боту [@Stickers](https://t.me/stickers) сообщение `/packstats` и выбрать пак, по которому нужно будет собрать статистику
### Настройка параметров
Заполните поля в файле [config.yaml](config.yaml) согласно их примерам

## Получить данные в statistics.csv
Через ваш аккаунт будут отправляться сообщения в указанный период - после успешного выполнения программы все сообщения будут удалены
```bash
python3 receive_stat.py 
```

## Отобразить собранные данные
Красные полоски на графиках обозначают выходные дни
```bash
python3 show_stat.py
```
