from telegram.bot import Bot

TOKEN = '1398340303:AAGuMpIxIurHmIUeQV-Y-v82K_Hp-iV0Hjs'
GROUP_ID = '-496730455'

bot = Bot(token=TOKEN)


def send_message(text):
    try:
        bot.send_message(GROUP_ID, text, parse_mode='html')
    except:
        pass
