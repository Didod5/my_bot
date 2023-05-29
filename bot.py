from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import settings
import ephem

logging.basicConfig(filename='bot.log', level=logging.INFO)

def greet_user(update, context):
    print('pushing /start')
    update.message.reply_text("Hello user")
    print(update)

def talk_to_me(update, context):
    text = update.message.text
    print(text)
    update.message.reply_text(text)

def get_coord(update, context):
    planet = update.message.text.split()[-1]
    if planet == 'mars' or 'Mars':
        const = ephem.constellation(ephem.Mars('2023/05/05'))
        update.message.reply_text(const)

def main():
    mybot = Updater(settings.API_KEY)
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    # dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    dp.add_handler(CommandHandler("planet", get_coord))


    logging.info('Bot started')
    mybot.start_polling()
    mybot.idle()

if __name__ == '__main__':
    main()