from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import settings
import ephem
import datetime


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
    user_planet = update.message.text.split()[-1].lower()
    
    date = datetime.datetime.today()
    planet_dict = {'mercury': ephem.Mercury(date),
                   'venus': ephem.Venus(date), 'mars': ephem.Mars(date),
                   'jupiter': ephem.Jupiter(date), 'saturn': ephem.Saturn(date),
                   'uranus': ephem.Uranus(date), 'neptune': ephem.Neptune(date)}
    user_planet = planet_dict[user_planet]

    const = ephem.constellation(user_planet)[-1]
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