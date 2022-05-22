import telebot
from telebot import types

bot = telebot.TeleBot('5371040522:AAE4Q4Tl7OUQ48oVOmpv5vRMo68VSMmNY3s')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    menu = types.KeyboardButton('Узнать способности бота')
    markup.add(menu)
    bot.send_message(message.chat.id, 'Привет, я бот-помощник Эйджея,и я помогу сделать твою подготовку кЕГЭ интереснее и удобнее! Пока можешь посмотреть на мои умения!'.format(message.from_user), reply_markup=markup)

@bot.message_handler(content_types=['text'])
def inline_key(menu):
    if menu.text == 'Узнать способности бота':
        mainmenu = types.InlineKeyboardMarkup(row_width=2)
        item_teacher = types.InlineKeyboardButton(text='Узнать про Эйджея', callback_data='key_teacher')
        item_course = types.InlineKeyboardButton(text='Узнать про курсы', callback_data='key_course')
        item_meme = types.InlineKeyboardButton(text='Полистать мемы', callback_data='key_meme')
        item_test = types.InlineKeyboardButton(text='Пройти тест', callback_data='key_test')
        item_video = types.InlineKeyboardButton(text='Прокачать мозг', callback_data='key_video')
        mainmenu.add(item_teacher, item_course, item_meme, item_test, item_video)
        bot.send_message(menu.chat.id, 'Вооу, кажется был замечен ученик, готовый побороться за свои баллы! Чем хочешь заняться?', reply_markup=mainmenu)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == 'mainmenu':
        mainmenu = types.InlineKeyboardMarkup(row_width=2)
        item_teacher = types.InlineKeyboardButton(text='Узнать про Эйджея', callback_data='key_teacher')
        item_course = types.InlineKeyboardButton(text='Узнать про курсы', callback_data='key_course')
        item_meme = types.InlineKeyboardButton(text='Полистать мемы', callback_data='key_meme')
        item_test = types.InlineKeyboardButton(text='Пройти тест', callback_data='key_test')
        item_video = types.InlineKeyboardButton(text='Прокачать мозг', callback_data='key_video')
        mainmenu.add(item_teacher, item_course, item_meme, item_test, item_video)
        bot.send_message(call.message.chat.id, 'Куда хочешь пойти дальше?', reply_markup=mainmenu)
    elif call.data == 'key_teacher':
        menu_teacher = types.InlineKeyboardMarkup(row_width=2)
        item_video_aj = types.InlineKeyboardButton(text='Видео про Эйджея', url='https://www.youtube.com/watch?v=cxjDxx2Mks4&t=8s', callback_data='key_video_aj')
        back = types.InlineKeyboardButton(text='Назад', callback_data='mainmenu')
        menu_teacher.add(item_video_aj, back)
        bot.send_message(call.message.chat.id,'*здесь будет информаия про Эйджея, пока вам достаточно знать, что он топ*',
                         reply_markup= menu_teacher)
    elif call.data == 'key_course':
        menu_course = types.InlineKeyboardMarkup(row_width=2)
        item_osnova = types.InlineKeyboardButton(text='Все про основу', callback_data='key_osnova')
        item_extra = types.InlineKeyboardButton(text='Все про экстру', callback_data='key_extra')
        item_fresh = types.InlineKeyboardButton(text='Все про фреш', callback_data='key_fresh')
        item_refresh = types.InlineKeyboardButton(text='Все про рефреш', callback_data='key_refresh')
        item_spec = types.InlineKeyboardButton(text='Все про спецкурсы', callback_data='key_spec')
        back = types.InlineKeyboardButton(text='Назад', callback_data='mainmenu')
        menu_course.add(item_osnova, item_spec, item_refresh, item_fresh, item_extra, back)
        bot.send_message(call.message.chat.id,'Про какой курс хочешь узнать побольше?',
                         reply_markup= menu_course)
    elif call.data == 'key_meme':
        menu_meme = types.InlineKeyboardMarkup(row_width=2)
        item_meme = types.InlineKeyboardButton(text='Начать смотреть мемы', callback_data='key_meme')
        back = types.InlineKeyboardButton(text='Назад', callback_data='mainmenu')
        menu_meme.add(item_meme, back)
        bot.send_message(call.message.chat.id,
                         'Устал от подготовки? Понимаю, я вот устаю от бесконечных отзывов от учеников, их очень много и нужно их всех обработать, кстати можешь познакомиться с ними здесь(*тут будет ссылка*), я вот отдыхаю, когда смотрю мемы, давай покажу и тебе парочку!',
                         reply_markup=menu_meme)
    elif call.data == 'key_test':
        menu_test = types.InlineKeyboardMarkup(row_width=2)
        item_test = types.InlineKeyboardButton(text='Выбрать тему теста', callback_data='item_test')
        back = types.InlineKeyboardButton(text='Назад', callback_data='mainmenu')
        menu_test.add(item_test, back)
        bot.send_message(call.message.chat.id,
                         'Практика, практика и еще раз практика, как говорит один прекрасный информатик - Коля Касперский! Давай порешаем, какую тему хочешь отработать?',
                         reply_markup=menu_test)
    elif call.data == 'key_video':
        menu_video = types.InlineKeyboardMarkup(row_width=2)
        item_video = types.InlineKeyboardButton(text='Видео', callback_data='item_video')
        item_web = types.InlineKeyboardButton(text='Вебинар', callback_data='item_web')
        back = types.InlineKeyboardButton(text='Назад', callback_data='mainmenu')
        menu_video.add(item_video, item_web, back)
        bot.send_message(call.message.chat.id,
                         'Мы с Эйджеем подготовили для тебя очень много полезного материала, что бы ты хотел посмотреть?',
                         reply_markup=menu_video)

bot.polling()



