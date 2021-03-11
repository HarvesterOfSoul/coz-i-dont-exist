#Forked plugin from Ultroid
#Original Plugin is here https://github.com/TeamUltroid/UltroidAddons/blob/main/AnimeChan.py
#If you use this plugin then please go and star the original developer repo (https://github.com/TeamUltroid/UltroidAddons)

from userge import userge, Message
import requests
import asyncio

@userge.on_cmd("aniquote", about={'header': "Get Anime Quote"})
async def aniquote(message: Message):
  await message.edit("Getting Anime Quote")
  try:
    resp = requests.get("https://animechan.vercel.app/api/random").json()
    return await message.edit(f"**{resp['quote']}**\n — __{resp['character']} ({resp['anime']})__")
  except:
    await message.edit("`Something went wrong, check logs ...`")
