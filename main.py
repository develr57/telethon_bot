from telethon.sync import TelegramClient

api_id = 0
api_hash = ''
bot_token = ''

# We have to manually call "start" if we want an explicit bot token
bot = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)


async def main():
    # me = await bot.get_me()
    # print(me.stringify())

    # await bot.send_message(1234567890, 'Hello, myself!')

    message = await bot.send_message(
        142341278,
        'This message has **bold**, `code`, __italics__ and '
        'a [nice website](https://mail.ru)!',
        link_preview=True
    )
    print(message.raw_text)
    await message.reply('Cool!')

with bot:
    bot.loop.run_until_complete(main())
