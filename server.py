#!/usr/bin/env python3.10.12
import asyncio

from create_bot  import bot 



if __name__ == "__main__":
    asyncio.run(bot.polling())
