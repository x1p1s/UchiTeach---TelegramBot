import telebot
from telebot import types

botTimeWeb = telebot.TeleBot('6730746764:AAFNA-dZeAl16xUq06op2uk6-eVzwTZ873o')

@botTimeWeb.message_handler(commands=['start'])
def startBot(message):
    first_mess = f"<b>{message.from_user.first_name}</b>, привет!\nХочешь расскажу немного о нашей компании?"
    markup = types.InlineKeyboardMarkup()
    button_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')
    button_no = types.InlineKeyboardButton(text='Нет', callback_data='no')
    markup.add(button_yes, button_no)
    botTimeWeb.send_message(message.chat.id, first_mess, parse_mode='html', reply_markup=markup)

    @botTimeWeb.callback_query_handler(func=lambda call: True)
    def response(function_call):
       if function_call.message:
            if function_call.data == "yes":
               second_mess = "Мы команда профессионалов, увлеченных созданием инновационных решений в сфере информационных технологий. Более детально можешь ознакомиться с нами на нашем сайте!"
               markup = types.InlineKeyboardMarkup()
               markup.add(types.InlineKeyboardButton("Перейти на сайт", url="https://reliab.tech/"))
               botTimeWeb.send_message(function_call.message.chat.id, second_mess, reply_markup=markup)
               botTimeWeb.answer_callback_query(function_call.id)

            if function_call.data == "no":
               third_mess = ("Жаль, но я всегда здесь, если у тебя что-то изменится! 🤖"
                             "\nОзнакомтесь с командами:\n"
                             "/help - если вдруг у вас будут вопросы\n"
                             "/go - пройдите свой первый тестовый опрос\n"
                             "/info - узнайте, какие изменения бота будут в будущем")
               botTimeWeb.send_message(function_call.message.chat.id, third_mess)
pass


@botTimeWeb.message_handler(commands=['help'])
def help(message):
    first_mess = ("Бот создан для hr-опросов, для сбора информации и построения hr-аналитики\n"
                  "Для вопросов, предложений или жалоб, вы можете обратиться к администрации")
    markup1 = types.InlineKeyboardMarkup()
    markup1.add(types.InlineKeyboardButton("Администратор", url="https://t.me/x1p1s"))
    botTimeWeb.send_message(message.chat.id,first_mess,reply_markup=markup1)
    pass

@botTimeWeb.message_handler(commands=['go'])
def info(message):
    first_mess = ("Давайте начнём совместную работу😊")
    markup2 = types.InlineKeyboardMarkup()
    markup2.add(types.InlineKeyboardButton("Пройти опрос", url="https://hr-polls.kontur.ru/polls/4960934b-5ad7-48f3-9f25-27f29d753493"))
    botTimeWeb.send_message(message.chat.id, first_mess, reply_markup=markup2)

    # Ваш код обработки команды info
    pass

@botTimeWeb.message_handler(commands=['info'])
def cancel_interview(message):
    first_mess = (f"<b>{message.from_user.first_name}</b>, ещё раз привет!\nВ будущем бот будет развиваться и становится куда лучше чем сейчас, планируется работа с многими языками и добавление профилей с индивидуальной индификацией\n")
    markup = types.InlineKeyboardMarkup()
    botTimeWeb.send_message(message.chat.id, first_mess, parse_mode='html', reply_markup=markup)


    pass


botTimeWeb.infinity_polling()