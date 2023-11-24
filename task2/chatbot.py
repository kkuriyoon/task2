import telegram
import schedule
import time
import pytz
import datetime
import asyncio
import sys
sys.path.append(r'C:\users\user\anaconda3\lib\site-packages')

# Bot: K2022_2_bot
# channel = K2022test
# chat_id = "6849862895"
# token = "6849862895:AAGYluQicfQAFaVahHfbnBZN-wrkKwkY-HM"

# function
def chatbot():
    chat_id = "6849862895"
    bot_token = "6849862895:AAGYluQicfQAFaVahHfbnBZN-wrkKwkY-HM"
    bot = telegram.Bot(token=bot_token)

    now = datetime.datetime.now(pytz.timezone('Asia/Seoul'))
    if now.hour >= 23 or now.hour <= 6:
        return
    str_now = str(now)
    asyncio.run(bot.send_message(chat_id=chat_id, text = '안농'))

chatbot()
schedule.every(30).minutes.do(chatbot)

while True:
    schedule.run_pending()
    time.sleep(1)