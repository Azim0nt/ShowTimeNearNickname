# Документация скрипта - Скрипт добавлять часы рядом с никмеймом пользователя

## Описание
Этот скрипт позволяет добавлять часы с текущем временим профиля пользователя в Telegram. Он использует библиотеку Telethon для установки текущего времени в качестве имени и информации о времени в качестве описания профиля.

## Установка
1. Установите зависимости, выполнив следующую команду:
```
pip install telethon pytz
```
2. Получите `api_id` и `api_hash` на [mytelegram.org](https://mytelegram.org/). Зарегистрируйтесь и создайте новое приложение для получения этих данных.
3. Замените значения `"YOUR_API_ID"`, `"YOUR_API_HASH"` и `"YOUR_NICKNAME"` в коде на свои фактические данные. В поле `"YOUR_NICKNAME"` укажите ваш никнейм в Telegram.

## Использование
1. Импортируйте необходимые модули:
```python
import time
from telethon import TelegramClient
from telethon.tl.functions.account import UpdateProfileRequest
from datetime import datetime
import pytz
```
2. Инициализируйте клиент Telegram:
```python
api_id = "YOUR_API_ID"
api_hash = "YOUR_API_HASH"
username = "YOUR_NICKNAME"
client = TelegramClient("carpediem", api_id, api_hash)
client.start()
```
3. Определите функцию для преобразования времени в строку:
```python
def convert_time_to_string(dt):
    return f"{dt.hour}:{dt.minute:02}"
```
4. Определите асинхронную функцию `main`, в которой будет основная логика обновления профиля:
```python
async def main():
    while True:
        current_time = convert_time_to_string(datetime.now().astimezone(pytz.timezone('Asia/Tashkent')))
        new_first_name = f"{username} | {current_time}"
        await client(UpdateProfileRequest(first_name=new_first_name))
        description = f"Сейчас время: {current_time}"
        await client(UpdateProfileRequest(about=description))
        time.sleep(60)
```
5. Запустите асинхронный цикл с помощью `asyncio`:
```python
if __name__ == '__main__':
    import asyncio
    asyncio.get_event_loop().run_until_complete(main())
```
6. Запустите скрипт:
```
python main.py
```
7. Скрипт будет обновлять информацию в вашем профиле Telegram каждые 60 секунд.

## Примечания
- Убедитесь, что ваш аккаунт Telegram не защищен двухэтапной аутентификацией. Если она включена, вам понадобится ввести дополнительный пароль при первом запуске скрипта.
- Если вы получаете ошибку `SessionPasswordNeededError`, следуйте инструкциям в консоли для ввода пароля. Это происходит только

 при первом запуске скрипта или при сбросе сессии.
- Скрипт будет работать, пока он запущен в вашей среде выполнения. Если вы остановите скрипт, обновление профиля также прекратится.

## Важная информация
Пожалуйста, обратите внимание, что использование этого скрипта для автоматического обновления профиля может нарушать правила использования Telegram. Убедитесь, что вы не нарушаете правила сообщества Telegram, прежде чем использовать скрипт.
