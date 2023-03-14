import telebot
import time
import reminder_methods

TOKEN = "6222171448:AAE4XBIYa26UzoRD1zWZeoH6TE2i_2rpVgA"

bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['start']) 
def send_welcome(message):
    bot.send_message(message.chat.id, "Ciao " + str(message.chat.first_name)+"!\n"+"Cosa vuoi fare?")

@bot.message_handler(commands=['add']) 
def add_reminder(message):
    bot.send_message(message.chat.id, "Inserisci promemoria:")

    @bot.message_handler(func=lambda m: True)
    def add(message):
        date = message.text.split()[0]
        time = message.text.split()[1]
        name = message.text.split()[2]
        chat_id = message.chat.id
        reminder_methods.add([chat_id, date, time, name])
        bot.send_message(message.chat.id, "Aggiunto!")

    bot.register_next_step_handler(message, add)

@bot.message_handler(commands=['remove']) 
def remove_reminder(message):
    bot.send_message(message.chat.id, "Inserisci promemoria:")

    @bot.message_handler(func=lambda m: True)
    def remove(message):
        date = message.text.split()[0]
        time = message.text.split()[1]
        name = message.text.split()[2]
        chat_id = message.chat.id
        flag = reminder_methods.remove([chat_id, date, time, name])
        if(flag == True):
            bot.send_message(message.chat.id, "Rimuovi!")
        else:
            bot.send_message(message.chat.id, "Promemoria non trovato!")

    bot.register_next_step_handler(message, remove)

@bot.message_handler(func=lambda message: True)
def unknown(message):
    bot.reply_to(message, "Sorry, I didn't understand that command.")

def main():
    bot.infinity_polling()
    time.sleep(1)
    list = reminder_methods.check()
    if(list[0] == True):
        bot.send_message(list[1], "Promemoria:\n"+list[2])

main()