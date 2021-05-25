import logging
from os import name
from telegram import update
import telegram
from telegram.ext import*
import handlers as handlers


class bot:

    def __init__(self):
        Token = '1811653875:AAHEKcQlEIrNGbPcm3hoJ57EKGNKYsJL-Sg'
        # se configura el login del bot donde mostrara todo
        logging.basicConfig(
            level=logging.INFO,format="%(asctime)s - %(name)s - %(levelname)s - %(message)s,")
        logger = logging.getLogger()

        if __name__ == "__main__":
            #con esto podremos obtener informacion importante sobre nuestro bot de telegram
            nuestro_bot =telegram.Bot(token = Token)
            print (nuestro_bot)

        self.updater = Updater(nuestro_bot.token, use_context=True)
        self.dispatcher = self.updater.dispatcher


    def iniciar_botelegram(self):
        handlers.handlers(self.dispatcher)
        self.updater.start_polling()
        self.updater.idle()


bot().iniciar_botelegram()