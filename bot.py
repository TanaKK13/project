import telebot
from telebot import types
from pathlib import Path
from parser_youtube import new

bot = telebot.TeleBot('5371040522:AAE4Q4Tl7OUQ48oVOmpv5vRMo68VSMmNY3s')


class Info():

    def __init__(self, name):
        self.inf = 'На курсе {} тебя ждут: вебинары, домашки и личный наставник.'.format(name)
        self.reklama = 'Переходи на сайт за более подробной информацией.'


class Refresh():
    name = 'Рефреш'
    price = 'от 1890 до 4500, зависит от тарифа'
    discr = 'Это финальный курс, на котором мы повторим весь материал за одну неделю.'


class Fresh():
    name = 'Фреш'
    price = '3500'
    discr = 'Это курс подготовки за 3 месяца до ЕГЭ.'


class Extra():
    name = 'Экстра'
    price = 'от 3500 до 4500, зависит от тарифа'
    discr = 'Это курс, который стартует в январе, каждого года.'


class Osnova():
    name = 'Основа'
    price = 'от 3100 до 3990, зависит от тарифа'
    discr = 'основной курс'


class Speccourse():
    name = 'спецкурсы'
    price = 'от 300 до 3000, зависит от тарифа и самого спецкурса'
    discr = 'Это небольшые курсы, которые длятся около месяца.'


osnova = Osnova()
extra = Extra()
fresh = Fresh()
refresh = Refresh()
spec = Speccourse()


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    menu = types.KeyboardButton('Узнать способности бота')
    markup.add(menu)
    photo = Path('telegram_bot', 'images', 'first_img.jpg')
    photo_first = open(photo, 'rb')
    bot.send_message(message.chat.id,
                     'Привет, я *бот-помощник Эйджея*,и я помогу сделать твою подготовку к ЕГЭ интереснее и удобнее! Пока можешь посмотреть на мои умения!'.format(
                         message.from_user), reply_markup=markup, parse_mode='Markdown')
    bot.send_photo(message.chat.id, photo_first)


@bot.message_handler(content_types=['text'])
def inline_key(menu):
    if menu.text == 'Узнать способности бота':
        mainmenu = types.InlineKeyboardMarkup(row_width=2)
        item_teacher = types.InlineKeyboardButton(text='Узнать про Эйджея 🥸', callback_data='key_teacher')
        item_course = types.InlineKeyboardButton(text='Узнать про курсы 🤓', callback_data='key_course')
        item_meme = types.InlineKeyboardButton(text='Полистать мемы 😂', callback_data='key_meme')
        item_test = types.InlineKeyboardButton(text='Пройти тест 💪', callback_data='key_test')
        item_video = types.InlineKeyboardButton(text='Прокачать мозг 🧠', callback_data='key_video')
        mainmenu.add(item_teacher, item_course, item_meme, item_test, item_video)
        photo = Path('telegram_bot', 'images', 'menu.jpg')
        photo_menu = open(photo, 'rb')
        bot.send_photo(menu.chat.id, photo_menu)
        bot.send_message(menu.chat.id,
                         'Вооу, кажется был замечен ученик, готовый побороться за свои баллы! Чем хочешь заняться?',
                         reply_markup=mainmenu)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == 'mainmenu':
        mainmenu = types.InlineKeyboardMarkup(row_width=2)
        item_teacher = types.InlineKeyboardButton(text='Узнать про Эйджея 🥸', callback_data='key_teacher')
        item_course = types.InlineKeyboardButton(text='Узнать про курсы 🤓', callback_data='key_course')
        item_meme = types.InlineKeyboardButton(text='Полистать мемы 😂', callback_data='key_meme')
        item_test = types.InlineKeyboardButton(text='Пройти тест 💪', callback_data='key_test')
        item_video = types.InlineKeyboardButton(text='Прокачать мозг 🧠', callback_data='key_video')
        mainmenu.add(item_teacher, item_course, item_meme, item_test, item_video)
        photo = Path('telegram_bot', 'images', 'menu.jpg')
        photo_menu = open(photo, 'rb')
        bot.send_photo(call.message.chat.id, photo_menu)
        bot.send_message(call.message.chat.id, 'Куда хочешь пойти дальше? 🤔', reply_markup=mainmenu)
    elif call.data == 'key_teacher':
        menu_teacher = types.InlineKeyboardMarkup(row_width=2)
        item_video_aj = types.InlineKeyboardButton(text='Видео про Эйджея',
                                                   url='https://www.youtube.com/watch?v=cxjDxx2Mks4&t=8s',
                                                   callback_data='key_video_aj')
        back = types.InlineKeyboardButton(text='Назад ⬅️', callback_data='mainmenu')
        menu_teacher.add(item_video_aj, back)
        photo = Path('telegram_bot', 'images', 'inf_aj.jpg')
        photo_inf = open(photo, 'rb')
        bot.send_photo(call.message.chat.id, photo_inf)
        bot.send_message(call.message.chat.id,
                         '*здесь будет информация про Эйджея, пока вам достаточно знать, что он топ*',
                         reply_markup=menu_teacher)
    elif call.data == 'key_course':
        menu_course = types.InlineKeyboardMarkup(row_width=2)
        item_osnova = types.InlineKeyboardButton(text='Всё про основу', callback_data='key_osnova')
        item_extra = types.InlineKeyboardButton(text='Всё про экстру', callback_data='key_extra')
        item_fresh = types.InlineKeyboardButton(text='Всё про фреш', callback_data='key_fresh')
        item_refresh = types.InlineKeyboardButton(text='Всё про рефреш', callback_data='key_refresh')
        item_spec = types.InlineKeyboardButton(text='Всё про спецкурсы', callback_data='key_spec')
        back = types.InlineKeyboardButton(text='Назад ⬅️', callback_data='mainmenu')
        menu_course.add(item_osnova, item_spec, item_refresh, item_fresh, item_extra, back)
        photo = Path('telegram_bot', 'images', 'course.jpg')
        photo_course = open(photo, 'rb')
        bot.send_photo(call.message.chat.id, photo_course)
        bot.send_message(call.message.chat.id, 'Про какой курс хочешь узнать побольше?',
                         reply_markup=menu_course)
    elif call.data == 'key_meme':
        menu_meme = types.InlineKeyboardMarkup(row_width=2)
        item_meme = types.InlineKeyboardButton(text='Начать смотреть мемы', callback_data='key_meme')
        back = types.InlineKeyboardButton(text='Назад ⬅️', callback_data='mainmenu')
        menu_meme.add(item_meme, back)
        photo = Path('telegram_bot', 'images', 'meme.jpg')
        meme = open(photo, 'rb')
        bot.send_photo(call.message.chat.id, meme)
        bot.send_message(call.message.chat.id,
                         'Устал от подготовки? Понимаю, я вот устаю от бесконечных отзывов от учеников, их очень много и нужно их всех обработать, кстати можешь познакомиться с ними здесь(*тут будет ссылка*), я вот отдыхаю, когда смотрю мемы, давай покажу и тебе парочку!',
                         reply_markup=menu_meme)
    elif call.data == 'key_test':
        menu_test = types.InlineKeyboardMarkup(row_width=2)
        item_test = types.InlineKeyboardButton(text='Выбрать тему теста', callback_data='item_test')
        back = types.InlineKeyboardButton(text='Назад ⬅️', callback_data='mainmenu')
        menu_test.add(item_test, back)
        photo = Path('telegram_bot', 'images', 'test.jpg')
        test = open(photo, 'rb')
        bot.send_photo(call.message.chat.id, test)
        bot.send_message(call.message.chat.id,
                         'Практика, практика и еще раз практика, как говорит один прекрасный информатик - Коля Касперский! Давай порешаем, какую тему хочешь отработать?',
                         reply_markup=menu_test)
    elif call.data == 'key_video':
        menu_video = types.InlineKeyboardMarkup(row_width=2)
        back = types.InlineKeyboardButton(text='Назад ⬅️', callback_data='mainmenu')
        menu_video.add(back)
        photo = Path('telegram_bot', 'images', 'video_web.jpg')
        video_web = open(photo, 'rb')
        video_list = new()
        text = '\n'.join('{}' for el in range(len(video_list))).format(*video_list)
        bot.send_photo(call.message.chat.id, video_web)
        bot.send_message(call.message.chat.id, text,
                         reply_markup=menu_video)
    elif call.data == 'key_osnova':
        menu_osnova = types.InlineKeyboardMarkup(row_width=2)
        back = types.InlineKeyboardButton(text='Назад ⬅️', callback_data='key_course')
        item_site = types.InlineKeyboardButton(text='Сайт со всеми курсами✨',
                                               url='https://webium.ru/')
        menu_osnova.add(back, item_site)
        text = 'Здесь информация про курс {}, сразу подскажу стоимость {}. {}'.format(osnova.name, osnova.price,
                                                                                      osnova.discr)
        infa = Info(osnova.name)
        infa2 = infa.inf
        text_2 = str(text) + ' ' + str(infa2) + ' ' + str(infa.reklama)
        photo = Path('telegram_bot', 'images', 'osnova.jpg')
        photo_osnova = open(photo, 'rb')
        bot.send_photo(call.message.chat.id, photo_osnova)
        bot.send_message(call.message.chat.id, text_2,
                         reply_markup=menu_osnova)
    elif call.data == 'key_fresh':
        menu_fresh = types.InlineKeyboardMarkup(row_width=2)
        back = types.InlineKeyboardButton(text='Назад ⬅️', callback_data='key_course')
        item_site = types.InlineKeyboardButton(text='Сайт со всеми курсами✨',
                                               url='https://webium.ru/')
        menu_fresh.add(back, item_site)
        text = 'Здесь информация про курс {}, сразу подскажу стоимость {}. {}'.format(fresh.name, fresh.price,
                                                                                      fresh.discr)
        infa = Info(fresh.name)
        infa2 = infa.inf
        text_2 = str(text) + ' ' + str(infa2) + ' ' + str(infa.reklama)
        photo = Path('telegram_bot', 'images', 'freh.jpg')
        photo_freh = open(photo, 'rb')
        bot.send_photo(call.message.chat.id, photo_freh)
        bot.send_message(call.message.chat.id, text_2,
                         reply_markup=menu_fresh)
    elif call.data == 'key_extra':
        menu_extra = types.InlineKeyboardMarkup(row_width=2)
        back = types.InlineKeyboardButton(text='Назад ⬅️', callback_data='key_course')
        item_site = types.InlineKeyboardButton(text='Сайт со всеми курсами✨',
                                               url='https://webium.ru/')
        menu_extra.add(back, item_site)
        infa = Info(extra.name)
        infa2 = infa.inf
        text = 'Здесь информация про курс {}, сразу подскажу стоимость {}. {}'.format(extra.name, extra.price,
                                                                                      extra.discr)
        text_2 = str(text) + ' ' + str(infa2) + ' ' + str(infa.reklama)
        photo = Path('telegram_bot', 'images', 'extra.jpg')
        photo_extra = open(photo, 'rb')
        bot.send_photo(call.message.chat.id, photo_extra)
        bot.send_message(call.message.chat.id, text_2,
                         reply_markup=menu_extra)
    elif call.data == 'key_refresh':
        menu_refresh = types.InlineKeyboardMarkup(row_width=2)
        back = types.InlineKeyboardButton(text='Назад ⬅️', callback_data='key_course')
        item_site = types.InlineKeyboardButton(text='Сайт со всеми курсами✨',
                                               url='https://webium.ru/')
        menu_refresh.add(back, item_site)
        text = 'Здесь информация про курс {}, сразу подскажу стоимость {}. {}'.format(refresh.name, refresh.price,
                                                                                      refresh.discr)
        infa = Info(refresh.name)
        infa2 = infa.inf
        text_2 = str(text) + ' ' + str(infa2) + ' ' + str(infa.reklama)
        photo = Path('telegram_bot', 'images', 'refreh.jpg')
        photo_ref = open(photo, 'rb')
        bot.send_photo(call.message.chat.id, photo_ref)
        bot.send_message(call.message.chat.id, text_2,
                         reply_markup=menu_refresh)
    elif call.data == 'key_spec':
        menu_spec = types.InlineKeyboardMarkup(row_width=2)
        back = types.InlineKeyboardButton(text='Назад ⬅️', callback_data='key_course')
        item_site = types.InlineKeyboardButton(text='Сайт со всеми курсами✨',
                                               url='https://webium.ru/')
        menu_spec.add(back, item_site)
        infa = Info(spec.name)
        text = 'Здесь информация про курс {}, сразу подскажу стоимость {}. {}'.format(spec.name, spec.price, spec.discr)
        text_2 = str(text) + ' ' + str(infa.reklama)
        photo = Path('telegram_bot', 'images', 'spec.jpg')
        photo_spec = open(photo, 'rb')
        bot.send_photo(call.message.chat.id, photo_spec)
        bot.send_message(call.message.chat.id, text_2,
                         reply_markup=menu_spec)


bot.polling()
