import telebot
import const
from telebot.types import InputLocationMessageContent
# import requests # на случай если телеграмм блокирует
# from fake_useragent import UserAgent

# response = requests.get('https://api.telegram.org/', headers={'User-Agent': UserAgent().random})
# print(response)
bot = telebot.TeleBot(const.token)

# bot.send_message(591554858, '=D')
# updates = bot.get_updates()
# print(updates)
# last_update = updates[-1]
# print(last_update)
# message_from_user = last_update.message
# print(message_from_user)
# print(bot.get_me())

def history_log(message,answer):
    print("\n___________________________")           # это разделитель log(a)
    from datetime import datetime                    # это библиотека времени
    print(datetime.now())                            # выводим время отправки сообщения
    print("Сообщение принято от {0} {1}. (id - {2}).\n Текст - {3}".format(message.from_user.first_name,
                                                                    message.from_user.last_name,
                                                                    str(message.from_user.id),
                                                                    message.text))
    print(answer)


@bot.message_handler(commands=["start","help"])
def handle_command(message):
    bot.send_message(message.chat.id, '''У меня есть функция 
Добавляй в конец каждого своего сообщения "#"
чтобы понять его в вверхний регистр)''')
    print("Начат разговор")


@bot.message_handler(content_types=["text"])
def handle_command(message): # после def идет название функции
    print("принято сообщение")
    if message.text == "привет" or message.text == "Привет":

        if message.from_user.id == 591554858:
            bot.send_message(message.chat.id, "Привет Создатель)")
        answer = str(const.privet)
        history_log(message, answer)
        bot.send_message(message.chat.id, const.privet)

    elif message.text == "ПРИВЕТ":
        answer = const.izbran
        history_log(message, answer)
        bot.send_message(message.chat.id, const.izbran)

    elif message.text[-1]=="#":
        bot.reply_to(message, message.text.upper()[:-1])
        answer = message.text.upper()[:-1]
        history_log(message, answer)
    else:
        answer = const.ne_znau
        history_log(message, answer)
        bot.send_message(message.chat.id, const.ne_znau)


bot.polling(none_stop=True, interval=0)