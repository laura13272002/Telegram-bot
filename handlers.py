import telegram
from telegram import replymarkup
from telegram import update
from telegram.ext import*
from telegram.inline.inlinekeyboardbutton import InlineKeyboardButton
from telegram.inline.inlinekeyboardmarkup import InlineKeyboardMarkup


def handlers(dispatcher):
    dispatcher.add_handler(CommandHandler("start", comando_start))
    dispatcher.add_handler(CommandHandler("help", comando_help))
    dispatcher.add_handler(CommandHandler("ppt", comando_matemat))
    # dispatcher.add_error_handler(errores)


def comando_start(update, context):
    update.message.reply_text(
        f"Bienvenido al bot {update.effective_user['first_name']} , usa /help para saber mas de mi uso.")


def comando_help(update, context):
    update.message.reply_text("Puedes usar varios comandos")


def comando_matemat(update, context, bot):

    keyboard = [
        [
            InlineKeyboardButton("Symbolab", url='https://es.symbolab.com/'),
        ],
        [InlineKeyboardButton("Resta", callback_data='resta'), InlineKeyboardButton("Suma", callback_data='suma'),
         InlineKeyboardButton("Division", callback_data='div'), InlineKeyboardButton(
             "Multiplicacion", callback_data='multi')
         ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text(
        'Ufffff la verdad eso es algo muy complicado para mi, te recomiendo a mi amigo, Aunque si te puedo ayudar con matematicas sencillas', reply_markup=reply_markup)

    
