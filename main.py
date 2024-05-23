import logging
from telegram.ext import Updater, CommandHandler
import config
from drawing_generator import generate_drawing

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def draw(update, context):
    text = ' '.join(context.args)

    image_url = generate_drawing(text)

    if image_url:
        update.message.reply_photo(image_url)
    else:
        update.message.reply_text("Не удалось сгенерировать рисунок. Попробуйте еще раз!")


def main():
    updater = Updater(token = config.TELEGRAM_TOKEN, use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("draw", draw))

    updater.start_polling()
    Updater.idle()

if __name__ == '__main__':
    main()