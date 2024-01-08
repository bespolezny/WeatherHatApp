import os
from telebot.async_telebot import AsyncTeleBot


from exceptions.bot_exceptions import *


try:
    bot = AsyncTeleBot(token = os.getenv("telegram_api_key"))
except Exception as ex: # Касательно этого момента я хз какое исключение тут ловить :-)
    if isinstance(ex, TokenNotFound):
        raise TokenNotFound
    else:
        raise InvalidToken


