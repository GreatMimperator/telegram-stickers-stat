import csv
import datetime

import pandas as pd
from telethon import TelegramClient, events
import asyncio
import yaml

# Чтение параметров из YAML файла
with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)

api_id = config['api_id']
api_hash = config['api_hash']
phone_number = config['phone_number']
query_delay_ms = config['query_delay_ms']

# Создание и запуск клиента
client = TelegramClient('session_name', api_id, api_hash)


async def get_statistics_for_date(date, message_list: list):
    future = asyncio.Future()

    @client.on(events.NewMessage(from_users='Stickers'))
    async def handler(event):
        message = event.message.message
        if date in message:
            future.set_result(message)
            message_list.append(event.message)
            client.remove_event_handler(handler)
        else:
            raise Exception(f"Bad answer: {message}")

    response = await client.send_message('Stickers', date)
    message_list.append(response)

    return await future


def parse_statistics_message(message):
    stats = {}
    lines = message.split('\n')
    for line in lines:
        if 'Использовано' in line or 'Usage' in line:
            stats['usage'] = int(line.split(': ')[1])
        elif 'Установлено' in line or "Installed" in line:
            stats['installed'] = int(line.split(': ')[1])
        elif 'Удалено' in line or "Removed" in line:
            stats['removed'] = int(line.split(': ')[1])
    return stats


async def gather_statistics(start_date, end_date):
    current_date = start_date
    all_stats = []
    messages_to_delete = []

    while current_date <= end_date:
        date_str = current_date.strftime("%m/%d/%Y")
        message = await get_statistics_for_date(date_str, messages_to_delete)
        stats = parse_statistics_message(message)
        stats['date'] = date_str
        all_stats.append(stats)
        current_date += pd.DateOffset(days=1)
        await asyncio.sleep(query_delay_ms / 1000)
    await client.delete_messages('Stickers', messages_to_delete)
    return all_stats


def save_statistics_to_csv(statistics, filename):
    keys = statistics[0].keys()
    with open(filename, 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(statistics)


async def main():
    await client.start(phone_number)

    print("Enter start date (mm/dd/yyyy): ")
    start_date = input()
    start_date = pd.to_datetime(start_date, format='%m/%d/%Y')

    print("Enter end date (empty if today, mm/dd/yyyy otherwise): ")
    end_date = input()
    if end_date.strip() == '':
        end_date = datetime.datetime.now()
    else:
        end_date = pd.to_datetime(end_date, format='%m/%d/%Y')

    statistics = await gather_statistics(start_date, end_date)
    save_statistics_to_csv(statistics, 'statistics.csv')

    await client.disconnect()


if __name__ == "__main__":
    asyncio.run(main())
