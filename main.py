import asyncio
import discord
from discord.ext import commands
import json
import time
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

client = commands.Bot(command_prefix='+', intents = discord.Intents(messages = True, guild_messages = True, members = True, guilds = True, voice_states = True))

myFont = ImageFont.truetype('minecraft.ttf', 55)

ever = {}
week = {}
month = {}
active = {}

@client.event
async def on_ready():
  global ever
  global week
  global month
  print("Ready")
  for guild in client.guilds:
      for member in guild.members:
        ever[member.id] = {"voice": 0, "text": 0}
        week[member.id] = {"voice": 0, "text": 0}
        month[member.id] = {"voice": 0, "text": 0}
  client.loop.create_task(week_vipe())
  client.loop.create_task(month_vipe())
            

@client.event
async def on_member_join(member):
    ever[member.id] = {"voice": 0, "text": 0}
    week[member.id] = {"voice": 0, "text": 0}
    month[member.id] = {"voice": 0, "text": 0}

@client.event
async def on_message(ctx):
  ever[ctx.author.id]["text"] = ever[ctx.author.id]["text"] + 1
  week[ctx.author.id]["text"] = week[ctx.author.id]["text"] + 1
  month[ctx.author.id]["text"] = month[ctx.author.id]["text"] + 1

@client.event
async def on_voice_state_update(member, before, after):
  global ever
  global week
  global month
  user = member.id
  if before.channel is None and after.channel is not None:
    print(f"{user} joined")
    active[user] = time.time()

  if after.channel is None and before.channel is not None:
    
    print(f"{user} left")
    ever[user]["voice"] += time.time() - active[user]
    week[user]["voice"] += time.time() - active[user]
    month[user]["voice"] += time.time() - active[user]


async def week_vipe():
  global week
  while True:
    reyt = {}
    for guild in client.guilds:
      for member in guild.members:
        voice = round(week[member.id]["voice"] / 120)
        reyt[member.id] = week[member.id]["text"] + voice
    sorted_reyt = {k: b for k, b in sorted(reyt.items(), key=lambda element: element[1], reverse=True)}
    for i in range(3):
      keys_list = list(sorted_reyt)
      username = client.get_user(keys_list[i])
      reyting = sorted_reyt[keys_list[i]]
      if i+1 == 1:
        my_image = Image.open("maket.png")
        image_editable = ImageDraw.Draw(my_image)
        text = f"{i+1}. {username}"
        image_editable.text((620,211), text, (125, 95, 53), font=myFont)
        my_image.save("result.png")
      if i+1 == 2:
        my_image = Image.open("result.png")
        image_editable = ImageDraw.Draw(my_image)
        text = f"{i+1}. {username}"
        image_editable.text((620,429), text, (125, 95, 53), font=myFont)
        my_image.save("result.png")
      if i+1 == 3:
        my_image = Image.open("result.png")
        image_editable = ImageDraw.Draw(my_image)
        text = f"{i+1}. {username}"
        image_editable.text((620,647), text, (125, 95, 53), font=myFont)
        my_image.save("result.png")
    chat = client.get_channel(1005796493757780019)
    await chat.send(file=discord.File('result.png'))
    for guild in client.guilds:
      for member in guild.members:
        week[member.id] = {"voice": 0, "text": 0}
    await asyncio.sleep(604800)


async def month_vipe():
  global month
  while True:
    reyt = {}
    for guild in client.guilds:
      for member in guild.members:
        voice = round(month[member.id]["voice"] / 120)
        reyt[member.id] = month[member.id]["text"] + voice
    sorted_reyt = {k: b for k, b in sorted(reyt.items(), key=lambda element: element[1], reverse=True)}
    for i in range(3):
      keys_list = list(sorted_reyt)
      username = client.get_user(keys_list[i])
      reyting = sorted_reyt[keys_list[i]]
      if i+1 == 1:
        my_image = Image.open("maket.png")
        image_editable = ImageDraw.Draw(my_image)
        text = f"{i+1}. {username}"
        image_editable.text((620,211), text, (125, 95, 53), font=myFont)
        my_image.save("result.png")
      if i+1 == 2:
        my_image = Image.open("result.png")
        image_editable = ImageDraw.Draw(my_image)
        text = f"{i+1}. {username}"
        image_editable.text((620,429), text, (125, 95, 53), font=myFont)
        my_image.save("result.png")
      if i+1 == 3:
        my_image = Image.open("result.png")
        image_editable = ImageDraw.Draw(my_image)
        text = f"{i+1}. {username}"
        image_editable.text((620,647), text, (125, 95, 53), font=myFont)
        my_image.save("result.png")
    chat = client.get_channel(1005796493757780019)
    await chat.send(file=discord.File('result.png'))
    for guild in client.guilds:
      for member in guild.members:
        month[member.id] = {"voice": 0, "text": 0}
    await asyncio.sleep(2592000)

client.run('MTAwNTQ3NDM3MzIzMjI1MDk3MQ.GzM1u6.27UKqUdBdJdqCFrqZI22_ThHOkM2z-BZqDszvU')
