from pyrogram import * 
from pyrogram.types import * 
from pyromod import listen
import time
import requests

api_id = 25996320 
api_hash = "772cefc3a92ed382b6c24adbd0d3ea26"
token = "6393751475:AAFR2BWat1NiV6zY7WcjYXtFfnX0Eo0gmF8"


bot_id = token.split(":")[0]

owner = int(1310488710)

app = Client("N00",api_id=api_id,api_hash=api_hash,bot_token=token)

try:
	open(f"channel{bot_id}.json","r")
except FileNotFoundError:
	open(f"channel{bot_id}.json","w")
	
def is_user(id):
		result = False
def show_channel() -> str:
	with open(f"channel{bot_id}.json","r") as file:
		return file.readline()
	
@app.on_message(filters.command("start")&filters.private)
async def app_start(c:Client,m:Message):
	do = requests.get(f"https://api.telegram.org/bot{token}/getChatMember?chat_id=@{show_channel()}&user_id={m.from_user.id}").text
	user = m.from_user.id
	
	if do.count("left") or do.count("Bad Request: user not found") or is_user(id=user) and not is_band(user):
          await m.reply_text(f"**اهـلا بـك فـي بـوت مـاريا 200𝐊 اشـترك فـي قنـاة البـوت [𝐇𝐄𝐑𝐄](t.me/{show_channel()}) بعـدين /start **",disable_web_page_preview=True,reply_markup=InlineKeyboardMarkup(
[[
InlineKeyboardButton("Join Channel",
url=f'https://t.me/{show_channel()}'),
],
]))
	
	else:
	    await app.send_message(text=f"اهـلا عـزيزي \n كـل مـا عليـك ارفـع البـوت ادمـن فـي الكـروب \n وارســرل تفـعل 🌿لعرض الاوامر ارسل كلمه الاوامر💕",
	    chat_id = m.chat.id, 
        reply_to_message_id=m.id,
      disable_web_page_preview = True) 
app.run()
