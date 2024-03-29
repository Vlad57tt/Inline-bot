# Inline Bot EX

Инлайн-бот для создания счётов и проверки их статуса (Cryptobot, CrystalPAY).

## Начало использования

1. Скачать данный репозиторий
   ```
   git clone https://github.com/Vlad57tt/Inline-bot.git
   ```

2. Скачать зависимости
   ```
   pip install -r requirements.txt

   ```

3. Создайте .env

	/inlinebot > .env

4. Настройте .env

	Добавьте в .env следующие данные:
	

	TOKEN=58206:AAFzFVEf4aK_oNb1mkdLdhO # Token вашего бота (t.me/BotFather > /mybots > API Token)

	URL_ABOUT=https://about.bot # URL описания (будет встроено в кнопку)

	URL_AGREEMENT=https://agreement.bot # URL пользовательского соглашения (будет встроено в кнопку)

	CRYPTOBOT_CURRENCY=USDT # Валюта платёжки Cryptobot

	CRYPTOBOT_TOKEN=7674:AA0VJ0zTIwGe1AC2gHs # Token платёжки Cryptobot

	CRYPTOBOT_TESTNET=True # Тестнет Cryptobot значения: False, True

	CRYSTAL_LOGIN=cassa123 # Login платёжки CrystalPAY без ()

	CRYSTAL_SECRET=8e17a2950e7N21647c5246b8772 # Secret платёжки CrystalPAY

	ACCEPTED_USER=123, 234 # ID telegram, которые могут использовать /check


5. Запустите бота
   ```
   python3 bot.py

   ```
  
6. : Управляйте ботом через команды:

   - `/start` чтобы запустить бота и открыть меню

   - `/check` чтобы проверить статус счёта

   - `@bot method value` чтобы создать счёт в любом чате. См. инструкцию в боте (/start > Помощь)

   



## Использование

Бот может выдавать периодические ошибки, игнорируйте их.


## Отказ от ответственности

Этот проект предназначен только для образовательных целей. Используйте его на свой страх и риск.