import pytz
import random
import logging
import telegram
import requests
from bs4 import BeautifulSoup
from datetime import datetime, time
from telegram.utils.helpers import escape_markdown
from telegram.ext import Updater, InlineQueryHandler, CommandHandler, MessageHandler, Filters
from telegram import InlineQueryResultArticle, ParseMode, InputTextMessageContent

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

def start(bot, update):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')

def error(bot, update, error):
    """ Log Errors caused by Updates. """
    logger.warning('Update "%s" caused error "%s"', update, error)

def unknown(bot, update):
    ''' Send a message to unknown commands '''
    bot.send_message(chat_id=update.message.chat_id, text="Sorry, I didn't understand that command. Try again, puta!")

def foodalert(bot, update):
    ''' Send messages about food - only works after 12 '''
    cest_tz = pytz.timezone('Europe/Prague')
    cest_time = cest_tz.localize(datetime.now())
    lb_time = cest_time.replace(hour=12, minute=0, second=0, microsecond=0)

    if (cest_time >= lb_time) == True:
        for i in range(10):
            bot.send_message(chat_id=update.message.chat_id, text="Food Alert!")
            +- i
    else:
        bot.send_message(chat_id=update.message.chat_id, text="Food Alert not possible prior to 12 AM.")
        
def javajob(bot, update):
    link = "https://www.jobs.cz/en/?q%5B%5D=Java&date=24h&salary=30000&employment=full"
    page = requests.get(link)
    soup = BeautifulSoup(page.content, 'html.parser')
    find = soup.find_all('div', attrs={"class":"standalone search-list__item"})
    for div in find:
            links = div.findAll('a', attrs={'class':"search-list__main-info__title__link"})
            for link in links:
                    ad = link.get_text() + ' ' + link.get('href')
                    bot.send_message(chat_id=update.message.chat_id, text=ad)

def fransmom(bot,update):
    ''' Insult Generator '''

    leadIn = [
                "Fransisco's Mom"
            ]

    insults = [
                "such a puta, she gives out frequent rider miles. "
                ,"such a puta, she has people take numbers to get into her bedroom"
                ,"is so ugly when she tried to join an ugly contest they said, 'Sorry, no professionals.'"
    ]

    data = [leadIn, insults]
    insult = ""
    for column in data:
        rand = random.randint(0,(len(column)-1))
        insult = insult + column[rand] + " "
    
    bot.send_message(chat_id=update.message.chat_id, text=insult)

def dimi_random_excuse(bot, update):
    ''' Random Excuse '''
    leadIn = [
    "I can't because"
    ,"Seriously I can't,"
    ,"Honestly I can't,"
    ]

    perpetrator = [
    "Francisco's mom",
    "Princess Peach",
    "Godzilla",
    "a handicapped gentleman",
    "a triceratops named Penelope",
    "the inventor of the slanket",
    "the director of 101 Dalmations",
    "the little Asain kid from Indiana Jones",
    "a man with 6 fingers on his right hand",
    "my mom",
    "Raiden from Mortal Kombat",
    "Mayor McCheese",
    "Scrooge McDuck",
    "the ghost of Margaret Thatcher",
    "the ghost of Hitler",
    "Ghost Dad",
    "the entire Roman Empire",
    "Kevin Ware's leg bone",
    "a British chap",
    "a Hasidic Jew",
    "Kevin Spacey",
    "Kevin Costner's stunt double",
    "Kevin McCallister's real life fake tarantuala",
    "the Cthulhu"
    ]

    delay = [
    "gave me a hicky.",
    "tried to kill me.",
    "ran me over with a diesel backhoe.",
    "died in front of me.",
    "tried to seduce me.",
    "beat me into submission.",
    "hid my Trapper Keeper.",
    "stole my bicycle",
    "slept with my uncle.",
    "called me \"too gay to fly a kite,\" whatever the means.",
    "stole my identity.",
    "broke into my house.",
    "put me in a Chinese finger trap.",
    "came after me.",
    "came on me.",
    "texted racial slurs from my phone.",
    "spin-kicked me in the collar bone",
    "tried to sell me vacuum cleaners.",
    "crapped in my gas tank.",
    "made me golf in shoes filled with macaroni and cheese.",
    "pulled me over in a stolen cop car and demanded fellatio.",
    "made me find Jesus.",
    "kept telling me knock knock jokes."
    ]

    data = [leadIn, perpetrator, delay]

    excuse = ""
    for column in data:
        rand = random.randint(0,(len(column)-1))
        excuse = excuse + column[rand] + " "

    bot.send_message(chat_id=update.message.chat_id, text=excuse)

def seifs_impossible_excuses(bot, update):
    link = "http://programmingexcuses.com/"
    page = requests.get(link)
    soup = BeautifulSoup(page.content, 'html.parser')
    for data in soup.find_all('div', class_='wrapper'):
        for a in data.find_all('a'):
            p_excuse = a.text
    bot.send_message(chat_id=update.message.chat_id, text=p_excuse)

def cigbreak(bot, update):
    ''' Send messages about cigarette break '''
    bot.send_message(chat_id=update.message.chat_id, text="Cigarette Break Now!")

def main(bot_token="681986974:AAHQbJAUeXF0JKEx-ZYr69hL_cjO8pxG0Is"):
    # Create the Updater and pass it your bot's token.
    updater = Updater(bot_token)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Handlers
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_error_handler(error)
    dp.add_handler(CommandHandler("foodalert", foodalert))
    dp.add_handler(CommandHandler("dimi_random_excuse", dimi_random_excuse))
    dp.add_handler(CommandHandler("fransmom",fransmom))
    dp.add_handler(CommandHandler("seifs_impossible_excuses",seifs_impossible_excuses))
    dp.add_handler(CommandHandler("javajob",javajob))
    dp.add_error_handler(error)
    # Uknown Handler - this needs to always be last.
    unknown_handler = MessageHandler(Filters.command, unknown)
    dp.add_handler(unknown_handler)
    
    # Run
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()