from aiogram import types, Dispatcher
from config import dp, logger
from keyboards import client_keyboard


async def send_welcome(message: types.Message):
    """ Welcome and help message """
    logger.info(
        f'[client - send_welcome] {message.from_user.id} - {message.from_user.username} - message: {message.text}'
    )
    if 'youtube' in message.text:
        await message.answer(
            "Test message 2",
            reply_markup=client_keyboard
        )
    else:
        await message.answer(
            "Test message",
            reply_markup=client_keyboard
        )


def register_handlers_client(dispatcher: Dispatcher):
    dispatcher.register_message_handler(send_welcome, commands=['start', 'help'])
