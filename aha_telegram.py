import asyncio
from aiogram import Bot, Dispatcher, types

# Replace 'YOUR_TELEGRAM_BOT_TOKEN' with your actual bot token
bot_token = 'YOUR_TELEGRAM_BOT_TOKEN'

# Initialize the bot and dispatcher
bot = Bot(token=bot_token)
dp = Dispatcher(bot)


async def send_telegram_message(chat_id, message):
    # Send the message
    await bot.send_message(chat_id=chat_id, text=message)


async def main():
    # Replace 'TARGET_CHAT_ID' with the chat ID of the user or group you want to send the message to
    chat_id = 'TARGET_CHAT_ID'

    # Replace 'YOUR_MESSAGE' with the actual message you want to send
    message = 'YOUR_MESSAGE'

    await send_telegram_message(chat_id, message)
    await bot.close()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
