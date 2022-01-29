from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


# *** Main menu ***
btnWeather = KeyboardButton('Weather')
btnTime = KeyboardButton('Time for notifications')
btnLanguage = KeyboardButton('Language')
mainMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(btnWeather, btnTime, btnLanguage)