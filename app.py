from loader import vega_assistant


async def on_shutdown(dp):
    await vega_assistant.close()


if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp

    executor.start_polling(dp, on_shutdown=on_shutdown)