
# TelegramStarsGifts

Script for sending Telegram gifts to users in exchange for Telegram Stars via Telethon.

Скрипт для отправки подарков в Telegram в обмен на Telegram Stars через Telethon.

---

## English

### Overview

`TelegramGift.py` is a simple CLI script that sends a **Telegram Star Gift** to a specific user using the Telethon client.  
You manually enter a gift ID, a user ID and an optional comment, and the script creates an invoice for that gift and pays it using your account session.

The script also allows sending **removed / discontinued gifts** that still exist in Telegram's internal database, as long as you know their gift IDs.  
You can find these and other gift IDs in the channel [@GiftChangesIDs](https://t.me/GiftChangesIDs).

This is useful for:
- Testing Telegram Star gifts sending from a personal or service account.
- Manually rewarding users with gifts for stars or other actions.
- Experimenting with the Telegram Stars API via Telethon.

### How it works

1. The script creates a `TelegramClient` session with your `api_id`, `api_hash` and session name (`star_gift_cli`).  
2. It asks you in the console for:
   - `gift id` – numeric ID of the gift.
   - `user id` – numeric Telegram ID of the recipient.
   - `comment` – optional message that will be sent with the gift (can be empty).  
3. It validates that `gift id` and `user id` are not empty and can be converted to integers.  
4. It loads full user info via `functions.users.GetFullUserRequest` and builds `InputPeerUser` for the recipient.  
5. It creates an `InputInvoiceStarGift` with:
   - target peer (recipient),
   - gift ID,
   - flags `hide_name=False`, `include_upgrade=False`,
   - optional `TextWithEntities` message if a comment was provided.  
6. It requests a payment form with `payments.GetPaymentFormRequest(invoice=invoice)` and then sends the payment via `payments.SendStarsFormRequest`.  
7. After a successful call it prints `Done:` and the result object to the console.

### Requirements

- Python 3.x  
- [Telethon](https://github.com/LonamiWebs/Telethon) installed  
- Telegram API credentials:
  - `api_id`
  - `api_hash`  

You also need a Telegram account that:
- Has access to Telegram Stars and can send star gifts.
- Can log in through Telethon.

### Installation

```bash
git clone https://github.com/aehubhub-hue/TelegramStarsGifts.git
cd TelegramStarsGifts
python -m venv venv

# Linux / macOS
source venv/bin/activate

# Windows
# venv\Scripts\activate

pip install telethon
# or
# pip install -r requirements.txt
```

### Configuration

```python
api_id = 123456              # your api_id
api_hash = "YOUR_API_HASH"   # your api_hash
session = "star_gift_cli"    # session name
```

On the first run, Telethon will ask you to log in with your phone number and code and will save the session file in the current directory.

### Usage

```bash
python TelegramGift.py
```

Then enter in the console:
- `Enter gift id:` – numeric gift ID (including IDs of removed gifts if you know them)  
- `Enter user id:` – numeric Telegram user ID  
- `Enter comment (optional):` – any text or leave blank  

If IDs are invalid, the script prints an error and exits.  
On success you will see `Done: ...` and the user will receive the gift in Telegram.

---

## Русский

### Обзор

`TelegramGift.py` — простой консольный скрипт для отправки **подарков за Telegram Stars** конкретному пользователю через Telethon.  
Ты вручную вводишь ID подарка, ID пользователя и необязательный комментарий, а скрипт создаёт инвойс на этот подарок и оплачивает его от имени твоего аккаунта.

Скрипт также позволяет отправлять **удалённые / снятые с витрины подарки**, которые всё ещё существуют во внутренней базе Telegram, если ты знаешь их ID.  
Посмотреть эти и другие ID подарков можно в канале [@GiftChangesIDs](https://t.me/GiftChangesIDs).

Подходит для:
- Тестов отправки подарков за звёзды с личного или сервисного аккаунта.
- Ручной выдачи подарков пользователям за звёзды или другие действия.
- Экспериментов с Telegram Stars API через Telethon.

### Как работает скрипт

1. Скрипт создаёт `TelegramClient` с твоими `api_id`, `api_hash` и именем сессии (`star_gift_cli`).  
2. В консоли он спрашивает:
   - `Enter gift id:` — числовой ID подарка.
   - `Enter user id:` — числовой Telegram ID получателя.
   - `Enter comment (optional):` — комментарий, который будет отправлен вместе с подарком (можно оставить пустым).  
3. Скрипт проверяет, что `gift id` и `user id` не пустые и могут быть преобразованы в целые числа.  
4. Загружает полную информацию о пользователе через `functions.users.GetFullUserRequest` и создаёт `InputPeerUser` для этого пользователя.  
5. Формирует `InputInvoiceStarGift` с:
   - получателем (`peer`),
   - ID подарка (`gift_id`),
   - флагами `hide_name=False`, `include_upgrade=False`,
   - сообщением `TextWithEntities`, если комментарий был указан.  
6. Запрашивает платёжную форму через `payments.GetPaymentFormRequest` и отправляет платёж `payments.SendStarsFormRequest`.  
7. В случае успеха выводит `Done:` и объект результата в консоль.

### Требования

- Python 3.x  
- Установленный Telethon:  
  ```bash
  pip install telethon
  ```  
- Учётные данные Telegram API:
  - `api_id`
  - `api_hash`  

Нужен Telegram‑аккаунт, который:
- Имеет доступ к Telegram Stars и может отправлять подарки.
- Может авторизоваться через Telethon.

### Установка

```bash
git clone https://github.com/aehubhub-hue/TelegramStarsGifts.git
cd TelegramStarsGifts
python -m venv venv

# Linux / macOS
source venv/bin/activate

# Windows
# venv\Scripts\activate

pip install telethon
# или
# pip install -r requirements.txt
```

### Настройка

```python
api_id = 123456              # твой api_id
api_hash = "YOUR_API_HASH"   # твой api_hash
session = "star_gift_cli"    # имя сессии
```

При первом запуске Telethon запросит номер телефона и код и сохранит файл сессии в текущей папке.

### Запуск

```bash
python TelegramGift.py
```

Дальше в терминале введи:
- `Enter gift id:` — ID подарка (в том числе удалённого, если знаешь его ID)  
- `Enter user id:` — ID получателя  
- `Enter comment (optional):` — комментарий или оставь пустым  

Если ID невалидные, скрипт выведет ошибку и завершится.  
При успехе увидишь `Done: ...`, а пользователь получит подарок в Telegram.

---

## License / Лицензия

This project is intended for personal and experimental use.  
You may modify and use the script in your own projects at your own risk.

Проект предназначен для личного и экспериментального использования.  
Ты можешь изменять и использовать скрипт в своих проектах на свой страх и риск.
