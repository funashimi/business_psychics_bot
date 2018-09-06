import telebot
import datetime

token = "685593634:AAEwgHf10pent1egzhXe2cFDtv17tSeghZY"
bot = telebot.TeleBot(token)

daysOfTheWeek = ('null', "понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье")
today = datetime.date.today()
isoWeekDay = today.isoweekday()

tomorrow = datetime.date.today()+datetime.timedelta(days=1)
isoWeekTomorrow = tomorrow.isoweekday()


@bot.message_handler(commands=['start'])
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row('Сегодня', 'Завтра')
    user_markup.row('пн', 'вт', 'ср', 'чт', 'пт', 'сб')
    bot.send_message(message.from_user.id, '''\r 
Здравствуйте.

С помощью этого бота вы сможете посмотреть расписание группы 437335/0201.

Выберите, на какое время вы хотите увидеть расписание.''', reply_markup=user_markup)


@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == 'пн':
        bot.send_message(message.from_user.id, '''\r
Понедельник:

⏱10:00-11:40
💡Управление развитием цифровых предприятий
📝Лекция
🏠3-ий учебный корпус
🚪Аудитория 206

-----------------

⏱12:00-13:40
💡Управление развитием цифровых предприятий
📝Практика
🏠3-ий учебный корпус
🚪Аудитория 206

-----------------

⏱14:00-15:40
💡Управление жизненным циклом информационных систем
👱🏻Анисифоров Алексей Борисович
📝Лекция
🏠4-ый учебный корпус
🚪Аудитория 300

-----------------

⏱16:00-17:40
💡Управление жизненным циклом информационных систем
👱🏻Анисифоров Алексей Борисович
📝Практика
🏠4-ый учебный корпус
🚪Аудитория 300
    ''')
    elif message.text == 'вт':
        bot.send_message(message.from_user.id, '''\r
Вторник:

⏱10:00-11:40
💡Технологии программирования
📝Лекция
👱🏻Фролов Александр Константинович
🏠3-ий учебный корпус
🚪Аудитория 400

-----------------

⏱12:00-13:40
💡Технологии программирования
📝Практика
👱🏻Фролов Александр Константинович
🏠3-ий учебный корпус
🚪Аудитория 309

-----------------

⏱14:00-15:40
💡Рынки ИКТ
👩🏻Ростова Ольга Владимировна
📝Лекция
🏠3-ий учебный корпус
🚪Аудитория 503

-----------------

⏱16:00-17:40
💡Рынки ИКТ
👩🏻Ростова Ольга Владимировна
📝Практика
🏠3-ий учебный корпус
🚪Аудитория 204''')
    elif message.text == 'ср':
        bot.send_message(message.from_user.id, '''\r
Среда:

⏱08:00-9:40
💡Военная подготовка
📝Практика
🏠Военная кафедра

-----------------

⏱10:00-11:40
💡Военная подготовка
📝Практика
🏠Военная кафедра''')
    elif message.text == 'чт':
        bot.send_message(message.from_user.id, '''\r
Занятий в этот день нет.''')
    elif message.text == 'пт':
        bot.send_message(message.from_user.id, '''\r
Пятница:

(!!! Чётная неделя !!!)
⏱10:00-11:40
💡Архитектура предприятия
📝Практика
🏠3-ий учебный корпус
🚪Аудитория 406

-----------------

(!!! Нечётная неделя !!!)
⏱12:00-13:40
💡Архитектура предприятия
📝Лекция
🏠3-ий учебный корпус
🚪Аудитория 401

-----------------

(!!! Чётная неделя !!!)
⏱14:00-15:40
💡Архитектура предприятия
📝Практика
🏠3-ий учебный корпус
🚪Аудитория 406

-----------------

(!!! Чётная неделя !!!)
⏱16:00-17:40
💡Архитектура предприятия
📝Практика
🏠3-ий учебный корпус
🚪Аудитория 406''')
    elif message.text == 'сб':
        bot.send_message(message.from_user.id, '''\r
Суббота:

⏱10:00-11:40
💡Управление инвестициями в развитие электронного бизнеса
📝Лекция
🏠3-ий учебный корпус
🚪Аудитория 105

-----------------

⏱12:00-13:40
💡Управление инвестициями в развитие электронного бизнеса
📝Практика
🏠3-ий учебный корпус
🚪Аудитория 105''')
    elif message.text == 'Сегодня':
        if isoWeekDay == 1:
            bot.send_message(message.from_user.id, '''\r
Понедельник:

⏱10:00-11:40
💡Управление развитием цифровых предприятий
📝Лекция
🏠3-ий учебный корпус
🚪Аудитория 206

-----------------

⏱12:00-13:40
💡Управление развитием цифровых предприятий
📝Практика
🏠3-ий учебный корпус
🚪Аудитория 206

-----------------

⏱14:00-15:40
💡Управление жизненным циклом информационных систем
👱🏻Анисифоров Алексей Борисович
📝Лекция
🏠4-ый учебный корпус
🚪Аудитория 300

-----------------

⏱16:00-17:40
💡Управление жизненным циклом информационных систем
👱🏻Анисифоров Алексей Борисович
📝Практика
🏠4-ый учебный корпус
🚪Аудитория 300
                ''')
        elif isoWeekDay == 2:
            bot.send_message(message.from_user.id, '''\r
Вторник:

⏱10:00-11:40
💡Технологии программирования
📝Лекция
👱🏻Фролов Александр Константинович
🏠3-ий учебный корпус
🚪Аудитория 400

-----------------

⏱12:00-13:40
💡Технологии программирования
📝Практика
👱🏻Фролов Александр Константинович
🏠3-ий учебный корпус
🚪Аудитория 309

-----------------

⏱14:00-15:40
💡Рынки ИКТ
👩🏻Ростова Ольга Владимировна
📝Лекция
🏠3-ий учебный корпус
🚪Аудитория 503

-----------------

⏱16:00-17:40
💡Рынки ИКТ
👩🏻Ростова Ольга Владимировна
📝Практика
🏠3-ий учебный корпус
🚪Аудитория 204''')
        elif isoWeekDay == 3:
            bot.send_message(message.from_user.id, '''\r
Среда:

⏱08:00-9:40
💡Военная подготовка
📝Практика
🏠Военная кафедра

-----------------

⏱10:00-11:40
💡Военная подготовка
📝Практика
🏠Военная кафедра''')
        elif isoWeekDay == 4:
            bot.send_message(message.from_user.id, '''\r
Занятий в этот день нет.''')
        elif isoWeekDay == 5:
            bot.send_message(message.from_user.id, '''\r
Пятница:

(!!! Чётная неделя !!!)
⏱10:00-11:40
💡Архитектура предприятия
📝Практика
🏠3-ий учебный корпус
🚪Аудитория 406

-----------------

(!!! Нечётная неделя !!!)
⏱12:00-13:40
💡Архитектура предприятия
📝Лекция
🏠3-ий учебный корпус
🚪Аудитория 401

-----------------

(!!! Чётная неделя !!!)
⏱14:00-15:40
💡Архитектура предприятия
📝Практика
🏠3-ий учебный корпус
🚪Аудитория 406

-----------------

(!!! Чётная неделя !!!)
⏱16:00-17:40
💡Архитектура предприятия
📝Практика
🏠3-ий учебный корпус
🚪Аудитория 406''')
        elif isoWeekDay == 6:
            bot.send_message(message.from_user.id, '''\r
Суббота:

⏱10:00-11:40
💡Управление инвестициями в развитие электронного бизнеса
📝Лекция
🏠3-ий учебный корпус
🚪Аудитория 105

-----------------

⏱12:00-13:40
💡Управление инвестициями в развитие электронного бизнеса
📝Практика
🏠3-ий учебный корпус
🚪Аудитория 105''')
        elif isoWeekDay == 7:
            bot.send_message(message.from_user.id, '''\r
Занятий в этот день нет.''')
    elif message.text == 'Завтра':
        if isoWeekTomorrow == 1:
            bot.send_message(message.from_user.id, '''\r
Понедельник:

⏱10:00-11:40
💡Управление развитием цифровых предприятий
📝Лекция
🏠3-ий учебный корпус
🚪Аудитория 206

-----------------

⏱12:00-13:40
💡Управление развитием цифровых предприятий
📝Практика
🏠3-ий учебный корпус
🚪Аудитория 206

-----------------

⏱14:00-15:40
💡Управление жизненным циклом информационных систем
👱🏻Анисифоров Алексей Борисович
📝Лекция
🏠4-ый учебный корпус
🚪Аудитория 300

-----------------

⏱16:00-17:40
💡Управление жизненным циклом информационных систем
👱🏻Анисифоров Алексей Борисович
📝Практика
🏠4-ый учебный корпус
🚪Аудитория 300
                ''')
        elif isoWeekTomorrow == 2:
            bot.send_message(message.from_user.id, '''\r
Вторник:

⏱10:00-11:40
💡Технологии программирования
📝Лекция
👱🏻Фролов Александр Константинович
🏠3-ий учебный корпус
🚪Аудитория 400

-----------------

⏱12:00-13:40
💡Технологии программирования
📝Практика
👱🏻Фролов Александр Константинович
🏠3-ий учебный корпус
🚪Аудитория 309

-----------------

⏱14:00-15:40
💡Рынки ИКТ
👩🏻Ростова Ольга Владимировна
📝Лекция
🏠3-ий учебный корпус
🚪Аудитория 503

-----------------

⏱16:00-17:40
💡Рынки ИКТ
👩🏻Ростова Ольга Владимировна
📝Практика
🏠3-ий учебный корпус
🚪Аудитория 204''')
        elif isoWeekTomorrow == 3:
            bot.send_message(message.from_user.id, '''\r
Среда:

⏱08:00-9:40
💡Военная подготовка
📝Практика
🏠Военная кафедра

-----------------

⏱10:00-11:40
💡Военная подготовка
📝Практика
🏠Военная кафедра''')
        elif isoWeekTomorrow == 4:
            bot.send_message(message.from_user.id, '''\r
Занятий в этот день нет.''')
        elif isoWeekTomorrow == 5:
            bot.send_message(message.from_user.id, '''\r
Пятница:

(!!! Чётная неделя !!!)
⏱10:00-11:40
💡Архитектура предприятия
📝Практика
🏠3-ий учебный корпус
🚪Аудитория 406

-----------------

(!!! Нечётная неделя !!!)
⏱12:00-13:40
💡Архитектура предприятия
📝Лекция
🏠3-ий учебный корпус
🚪Аудитория 401

-----------------

(!!! Чётная неделя !!!)
⏱14:00-15:40
💡Архитектура предприятия
📝Практика
🏠3-ий учебный корпус
🚪Аудитория 406

-----------------

(!!! Чётная неделя !!!)
⏱16:00-17:40
💡Архитектура предприятия
📝Практика
🏠3-ий учебный корпус
🚪Аудитория 406''')
        elif isoWeekTomorrow == 6:
            bot.send_message(message.from_user.id, '''\r
Суббота:

⏱10:00-11:40
💡Управление инвестициями в развитие электронного бизнеса
📝Лекция
🏠3-ий учебный корпус
🚪Аудитория 105

-----------------

⏱12:00-13:40
💡Управление инвестициями в развитие электронного бизнеса
📝Практика
🏠3-ий учебный корпус
🚪Аудитория 105''')
        elif isoWeekTomorrow == 7:
            bot.send_message(message.from_user.id, '''\r
Занятий в этот день нет.''')


bot.polling(none_stop=True)
