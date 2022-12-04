from datetime import datetime, date

from telegram.ext import CommandHandler, Updater, Filters, MessageHandler
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
import days as d

updater = Updater(token='5726232380:AAGuXK1rqbapBSmwJ-QZzX3Nrn9NXgQM2Fw')
date_ = date.today().weekday()
week_number = datetime.today().isocalendar()[1]
days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']


def wake_up(update, context):
	chat = update.effective_chat
	button = ReplyKeyboardMarkup(
		[
		['Расписание на сегодня', 'Расписание на завтра', 'Общее расписание']
		],
		resize_keyboard=True)
	context.bot.send_message(chat_id=chat.id,
		text='_',
		reply_markup=button
		)


def say_hi(update, context):
	global week_number
	chat = update.effective_chat	
	if update.message.text == 'Общее расписание':
		button = ReplyKeyboardRemove()
		butto = ReplyKeyboardMarkup([['1 подгруппа', '2 подгруппа']], resize_keyboard=True)
		context.bot.send_message(chat_id=chat.id,
		text='Общее расписание',
		reply_markup=button
		)
		context.bot.send_message(chat_id=chat.id,
		text='Подгруппа:',
		reply_markup=butto
		)
	if update.message.text == '1 подгруппа':
		button = ReplyKeyboardRemove()
		butto = ReplyKeyboardMarkup(
			[
			['Расписание на сегодня', 'Расписание на завтра', 'Общее расписание']
			],
			resize_keyboard=True)
		context.bot.send_message(chat_id=chat.id,
		text='Общее расписание',
		reply_markup=button
		)
		context.bot.send_message(chat_id=chat.id,
		text=update.message.text,
		reply_markup=butto
		)
		if week_number % 2 == 0:
			d.monday_1z(update, context)
			d.tuesday_1z(update, context)
			d.wednesday_1z(update, context)
			d.thursday_1z(update, context)
			d.friday_1z(update, context)
			d.saturday_1z(update, context)
			d.sunday(update, context)
		elif week_number % 2 != 0:
			d.monday_1c(update, context)
			d.tuesday_1c(update, context)
			d.wednesday_1c(update, context)
			d.thursday_1c(update, context)
			d.friday_1c(update, context)
			d.saturday_1c(update, context)
			d.sunday(update, context)
	elif update.message.text == '2 подгруппа':
		button = ReplyKeyboardRemove()
		butto = ReplyKeyboardMarkup(
			[
			['Расписание на сегодня', 'Расписание на завтра', 'Общее расписание']
			],
			resize_keyboard=True)
		context.bot.send_message(chat_id=chat.id,
		text='_',
		reply_markup=button
		)
		context.bot.send_message(chat_id=chat.id,
		text='_',
		reply_markup=butto
		)
		if week_number % 2 == 0:
			d.monday_2z(update, context)
			d.tuesday_2z(update, context)
			d.wednesday_2z(update, context)
			d.thursday_2z(update, context)
			d.friday_2z(update, context)
			d.saturday_2z(update, context)
			d.sunday(update, context)
		elif week_number % 2 != 0:
			d.monday_2c(update, context)
			d.tuesday_2c(update, context)
			d.wednesday_2c(update, context)
			d.thursday_2c(update, context)
			d.friday_2c(update, context)
			d.saturday_2c(update, context)
			d.sunday(update, context)


def say(update, context):
	global week_number
	chat = update.effective_chat	
	if update.message.text == 'Расписание на сегодня':
		button = ReplyKeyboardRemove()
		butto = ReplyKeyboardMarkup([['1 подгруппа', '2 подгруппа']], resize_keyboard=True)
		context.bot.send_message(chat_id=chat.id,
		text='Расписание на сегодня',
		reply_markup=button
		)
		context.bot.send_message(chat_id=chat.id,
		text='Подгруппа:',
		reply_markup=butto
		)
	if update.message.text == '1 подгруппа':
		button = ReplyKeyboardRemove()
		butto = ReplyKeyboardMarkup(
			[
			['Расписание на сегодня', 'Расписание на завтра', 'Общее расписание']
			],
			resize_keyboard=True)
		context.bot.send_message(chat_id=chat.id,
		text='Расписание на сегодня',
		reply_markup=button
		)
		context.bot.send_message(chat_id=chat.id,
		text=update.message.text,
		reply_markup=butto
		)
		if week_number % 2 == 0:
			if days[date_] == 'Понедельник':
				d.monday_1z(update, context)
			if days[date_] == 'Вторник':
				d.tuesday_1z(update, context)
			if days[date_] == 'Среда':
				d.wednesday_1z(update, context)
			if days[date_] == 'Четверг':
				d.thursday_1z(update, context)
			if days[date_] == 'Пятница':
				d.friday_1z(update, context)
			if days[date_] == 'Суббота':
				d.saturday_1z(update, context)
			if days[date_] == 'Воскресенье':
				d.sunday(update, context)
		if week_number % 2 != 0:
			if days[date_] == 'Понедельник':
				d.monday_1c(update, context)
			if days[date_] == 'Вторник':
				d.tuesday_1c(update, context)
			if days[date_] == 'Среда':
				d.wednesday_1c(update, context)
			if days[date_] == 'Четверг':
				d.thursday_1c(update, context)
			if days[date_] == 'Пятница':
				d.friday_1c(update, context)
			if days[date_] == 'Суббота':
				d.saturday_1c(update, context)
			if days[date_] == 'Воскресенье':
				d.sunday(update, context)


updater.dispatcher.add_handler(CommandHandler('start', wake_up))
updater.dispatcher.add_handler(MessageHandler(Filters.text, (say, say_hi)))

updater.start_polling()
updater.idle()

print(date.today().weekday() + 1)