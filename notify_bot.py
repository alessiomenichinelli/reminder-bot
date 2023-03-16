import telebot
import time
import reminder_methods

TOKEN = "6250862393:AAG9ccxUx78NmGHpaoKY7wuL4av8cmmTzvM"

bot = telebot.TeleBot(TOKEN, parse_mode=None)

while(True):
    list = reminder_methods.check()
    if(list[0] == True):
        bot.send_message(list[1], "Promemoria:\n"+list[2])
    time.sleep(60)