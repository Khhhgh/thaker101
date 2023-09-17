# Programming By : RUKS and Ibrahem_Alkabby
# tele : @Ibrahem_Alkabby and @ruks3
#ruks3 =  Instagram: _v_go
#Ibrahem = insragram: 6e.2k
# Telegram : @DIBIBl
# Telegram2 : @TDTDI                   # YouTube : https://youtube.com/channel/UCUNbzQRjfAXGCKI1LY72DTA       # automatic reaction tool              # TOOL = FREE                         
"""
عزيزي اذا تغير حقوق تثبت انك فاشل ..لا تغير حقوق ..اذا تغير حقوق حتصير مطي ومتصير مطور ماشي !

"""
from secrets import choice
from typing import Text
import requests
import telebot
import random
from telebot import types
from user_agent import generate_user_agent
token = '6446376504:AAG1W2Rs6O-EuPRN3SGPMdramHqR3QgEjEc'
headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'ar,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
    'cache-control': 'max-age=0',
    'content-length': '132',
    'content-type': 'application/x-www-form-urlencoded',
    'cookie': 'FreeWHA-persistent=checked; FreeWHA-ID=ablys.ueuo.com; __gads=ID=c2bd83da020e5a31-22d771956bca00f4:T=1630487997:RT=1630487997:S=ALNI_MZnK7R6W9GucfOvMMG2id6FBpNZHw; FreeWHAreg=create',
    'origin': 'https://newserv.freewha.com',
    'referer': 'https://newserv.freewha.com/cgi-bin/create_ini.cgi',
    'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Microsoft Edge";v="92"',
    'sec-ch-ua-mobile': '?0',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': generate_user_agent()
}
# Programming By : RUKS and Brahim
char = "zxcvbnmasdfghjklqwertyuiop"
rand = str(''.join(random.choice(char)for i in range(9)))
bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def send_wel(message):
    inline = types.InlineKeyboardMarkup(row_width=3)
# Programming By : RUKS and Brahim
    start = types.InlineKeyboardButton("اضغط لصنع الاستضافه",callback_data='start')
    inline.add(start)
    bot.send_message(chat_id=(message.chat.id),text="مرحبا بك في بوت صنع الاستضافة",reply_markup=inline)
@bot.callback_query_handler(func=lambda call: True)
def make(call):
    if call.data == 'start':
        bot.edit_message_text(chat_id=(call.message.chat.id),message_id=(call.message.id),text='الان قم برسال اسم الاستضافة')
        @bot.message_handler(func=(lambda message: True))
        def send_message(message):
            
            if message.text:
                M=str(''.join(random.choice(char)for i in range(3)))
                print(M)
                data = {
                    'action': 'validate',
                    'domainName': '{}.orgfree.com'.format(message.text),
                    'email': '{}@gmail.com'.format(rand),
                    'password': 'ibrahem5ruks5{}'.format(M),
                    'confirmPassword': 'ibrahem5ruks5{}'.format(M),
                    'agree': '1'
                } 
                url = 'https://newserv.freewha.com/cgi-bin/create_ini.cgi'
                req = requests.post(url,headers=headers,data=data).text           # Programming By : RUKS and Brahim
                true = 'Create your account at Free Web Hosting Area'
                false = 'This account already exists!'
# Programming By : RUKS and Brahim    
                if true in req:       
                 bot.send_message((message.chat.id),text=f"""⌯  ʏᴏụʀ ʜᴏѕᴛɪɴɢ ɪɴғᴏʀᴍᴀᴛɪᴏɴ  ⌯
┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉
⌯ ᴜѕᴇʀɴᴀᴍᴇ : {message.text}.orgfree.com
⌯ ᴘᴀѕѕᴡᴏʀᴅ : ibrahem5ruks5{M}
⌯ ᴡᴇʙѕɪᴛᴇ : {message.text}.orgfree.com
⌯ ᴘᴀɴᴇʟ : https://newserv.freewha.com
┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉
• Tele : @DIBIBl . @TDTDI. ؟ ، 🔥""")
                elif false in req:
                    bot.send_message(chat_id=(call.message.chat.id),text="غير متاح")
# Programming By : RUKS and Brahim
bot.polling()
