import logging
import settings
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters


logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


def start_bot(update: Updater, context: CallbackContext):
    print(update)
    mytext = f'Hello {update.message.chat.username}! \nI have only /start command! =)'
    update.message.reply_text(mytext)


def chat(update: Updater, context: CallbackContext):
    text = update.message.text
    logging.info(text)

    update.message.reply_text(text)


def main():
    updater = Updater(settings.TOKEN_TELEGRAMM)

    updater.dispatcher.add_handler(CommandHandler("start", start_bot))
    updater.dispatcher.add_handler(MessageHandler(Filters.text, chat))

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
