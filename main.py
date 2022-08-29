import asyncio
import discord
from discord.ext import commands
import time
from discord.utils import get
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

client = commands.Bot(command_prefix='+', intents = discord.Intents(messages = True, guild_messages = True, members = True, guilds = True, voice_states = True))

myFont = ImageFont.truetype('e-UkraineHead-Light.otf', 30)
myDayFont = ImageFont.truetype('e-UkraineHead-Light.otf', 65)

ever = {}
week = {}
month = {}
day = {}
active = {}
top_month = 498547529374498849
top_week = 498547529374498849
ignore =[999289105621979247,999289269258563634,997467577653669960,997466988404277318,1006561978388590612,1001179252965785681,1006600381079486474,1001179275354964078,1001179309932822643,999297977740968066,1001498688545374238]
issent_week = 0
issent_day = 0
issent_month = 0
day_msg = {}
week_msg = {}
month_msg = {}
@client.event
async def on_ready():
  global ever
  global week
  global month
  global day
  print("Ready")
  for guild in client.guilds:
      for member in guild.members:
        ever[member.id] = {"voice": 0, "text": 0}
        week[member.id] = {"voice": 0, "text": 0}
        month[member.id] = {"voice": 0, "text": 0}
        day[member.id] = {"voice": 0, "text": 0}
  
  client.loop.create_task(error_for())
  print('waka waka')
  client.loop.create_task(month_vipe())
  client.loop.create_task(week_vipe())
  client.loop.create_task(day_vipe())
  client.loop.create_task(day_reset())
  client.loop.create_task(week_reset())
  client.loop.create_task(month_reset())
            

@client.event
async def on_member_join(member):
    ever[member.id] = {"voice": 0, "text": 0}
    week[member.id] = {"voice": 0, "text": 0}
    month[member.id] = {"voice": 0, "text": 0}
    day[member.id] = {"voice": 0, "text": 0}

@client.event
async def on_message(ctx):
  if ctx.channel.id not in ignore:
    ever[ctx.author.id]["text"] = ever[ctx.author.id]["text"] + 1
    week[ctx.author.id]["text"] = week[ctx.author.id]["text"] + 1
    month[ctx.author.id]["text"] = month[ctx.author.id]["text"] + 1
    day[ctx.author.id]["text"] = month[ctx.author.id]["text"] + 1

@client.event
async def on_voice_state_update(ctx, member, before, after):
  global ever
  global week
  global month
  global day
  user = member.id
  if ctx.channel.id not in ignore:
    if before.channel is None and after.channel is not None:
      print(f"{user} joined")
      active[user] = time.time()
  
    if after.channel is None and before.channel is not None:
      
      print(f"{user} left")
      ever[user]["voice"] += time.time() - active[user]
      week[user]["voice"] += time.time() - active[user]
      month[user]["voice"] += time.time() - active[user]
      day[user]["voice"] += time.time() - active[user]


@client.event
async def on_voice_state_update(member, before, after):
  global ever
  global week
  global month
  user = member.id
  if before.channel is None and after.channel is not None and after.channel.id not in ignore:
    print(f"{user} joined")
    active[user] = time.time()

  if after.channel is None and before.channel is not None:
    
    print(f"{user} left")
    ever[user]["voice"] += time.time() - active[user]
    week[user]["voice"] += time.time() - active[user]
    month[user]["voice"] += time.time() - active[user]
    day[user]["voice"] += time.time() - active[user]


async def week_vipe():
  global week
  global top_week
  global week_msg
  global issent_week
  while True:
    reyt = {}
    print('week vipr func')
    for guild in client.guilds:
      for member in guild.members:
        voice = round(week[member.id]["voice"] / 120)
        reyt[member.id] = week[member.id]["text"] + voice
    non_reyt = {k: b for k, b in sorted(reyt.items(), key=lambda element: element[1], reverse=True)}
    sorted_reyt = {}
    non_list = list(non_reyt)
    for i in non_list:
      if client.get_user(i).bot == True:
        continue
      else:
        sorted_reyt[i] = non_reyt[i]
    for i in range(11):
      keys_list = list(sorted_reyt)
      username = client.get_user(keys_list[i])
      reyting = sorted_reyt[keys_list[i]]
      if i+1 == 1:
        my_image = Image.open("week_maket.png")
        image_editable = ImageDraw.Draw(my_image)
        text = f"{username} - {reyting}"
        image_editable.text((381,490), text, (0, 0, 0), font=myFont)
        my_image.save("week_result.png")
      if i+1 == 2:
        my_image = Image.open("week_result.png")
        image_editable = ImageDraw.Draw(my_image)
        text = f"{username} - {reyting}"
        image_editable.text((381,597), text, (0, 0, 0), font=myFont)
        my_image.save("week_result.png")
      if i+1 == 3:
        my_image = Image.open("week_result.png")
        image_editable = ImageDraw.Draw(my_image)
        text = f"{username} - {reyting}"
        image_editable.text((381,693), text, (0, 0, 0), font=myFont)
        my_image.save("week_result.png")
      if i+1 == 4:
        my_image = Image.open("week_result.png")
        image_editable = ImageDraw.Draw(my_image)
        text = f"{username} - {reyting}"
        image_editable.text((381,797), text, (0, 0, 0), font=myFont)
        my_image.save("week_result.png")
      if i+1 == 5:
        my_image = Image.open("week_result.png")
        image_editable = ImageDraw.Draw(my_image)
        text = f"{username} - {reyting}"
        image_editable.text((381,896), text, (0, 0, 0), font=myFont)
        my_image.save("week_result.png")
      if i+1 == 6:
        my_image = Image.open("week_result.png")
        image_editable = ImageDraw.Draw(my_image)
        text = f"{username} - {reyting}"
        image_editable.text((980,490), text, (0, 0, 0), font=myFont)
        my_image.save("week_result.png")
      if i+1 == 7:
        my_image = Image.open("week_result.png")
        image_editable = ImageDraw.Draw(my_image)
        text = f"{username} - {reyting}"
        image_editable.text((980,597), text, (0, 0, 0), font=myFont)
        my_image.save("week_result.png")
      if i+1 == 8:
        my_image = Image.open("week_result.png")
        image_editable = ImageDraw.Draw(my_image)
        text = f"{username} - {reyting}"
        image_editable.text((980,692), text, (0, 0, 0), font=myFont)
        my_image.save("week_result.png")
      if i+1 == 9:
        my_image = Image.open("week_result.png")
        image_editable = ImageDraw.Draw(my_image)
        text = f"{username} - {reyting}"
        image_editable.text((980,797), text, (0, 0, 0), font=myFont)
        my_image.save("week_result.png")
      if i+1 == 10:
        my_image = Image.open("week_result.png")
        image_editable = ImageDraw.Draw(my_image)
        text = f"{username} - {reyting}"
        image_editable.text((980,898), text, (0, 0, 0), font=myFont)
        my_image.save("week_result.png")
      if i+1 == 11:
        my_image = Image.open("week_result.png")
        image_editable = ImageDraw.Draw(my_image)
        text = f"{client.get_user(top_week)} - {reyting}"
        image_editable.text((635,1026), text, (0, 0, 0), font=myFont)
        my_image.save("week_result.png")
    chat = client.get_channel(1007301750895677491)
    embed = discord.Embed(
            color=discord.Color.green()
        )
    file = discord.File("week_result.png", filename="image.png")
    embed.set_image(url="attachment://image.png")
    print('sending week reyt')
    if issent_week == 0:
      week_msg = await chat.send(file=file, embed=embed)
      issent_week = 1
    else:
      await week_msg.delete()
      week_msg = await chat.send(file=file, embed=embed)
    #await msg.edit(file=file, embed=embed)
    print('week reyt sent')
    await asyncio.sleep(3600)#604800

async def month_vipe():
  global month
  global top_month
  global month_msg
  global issent_month
  while True:
    reyt = {}
    print('month vipr func')
    for guild in client.guilds:
      for member in guild.members:
        voice = round(month[member.id]["voice"] / 120)
        reyt[member.id] = month[member.id]["text"] + voice
    non_reyt = {k: b for k, b in sorted(reyt.items(), key=lambda element: element[1], reverse=True)}
    sorted_reyt = {}
    non_list = list(non_reyt)
    for i in non_list:
      if client.get_user(i).bot == True:
        continue
      else:
        sorted_reyt[i] = non_reyt[i]
    for i in range(11):
      keys_list = list(sorted_reyt)
      username = client.get_user(keys_list[i])
      reyting = sorted_reyt[keys_list[i]]
      if i+1 == 1:
        my_image = Image.open("month_maket.png")
        image_editable = ImageDraw.Draw(my_image)
        text = f"{username} - {reyting}"
        image_editable.text((381,490), text, (0, 0, 0), font=myFont)
        my_image.save("month_result.png")
      if i+1 == 2:
        my_image = Image.open("month_result.png")
        image_editable = ImageDraw.Draw(my_image)
        text = f"{username} - {reyting}"
        image_editable.text((381,597), text, (0, 0, 0), font=myFont)
        my_image.save("month_result.png")
      if i+1 == 3:
        my_image = Image.open("month_result.png")
        image_editable = ImageDraw.Draw(my_image)
        text = f"{username} - {reyting}"
        image_editable.text((381,693), text, (0, 0, 0), font=myFont)
        my_image.save("month_result.png")
      if i+1 == 4:
        my_image = Image.open("month_result.png")
        image_editable = ImageDraw.Draw(my_image)
        text = f"{username} - {reyting}"
        image_editable.text((381,797), text, (0, 0, 0), font=myFont)
        my_image.save("month_result.png")
      if i+1 == 5:
        my_image = Image.open("month_result.png")
        image_editable = ImageDraw.Draw(my_image)
        text = f"{username} - {reyting}"
        image_editable.text((381,893), text, (0, 0, 0), font=myFont)
        my_image.save("month_result.png")
      if i+1 == 6:
        my_image = Image.open("month_result.png")
        image_editable = ImageDraw.Draw(my_image)
        text = f"{username} - {reyting}"
        image_editable.text((980,490), text, (0, 0, 0), font=myFont)
        my_image.save("month_result.png")
      if i+1 == 7:
        my_image = Image.open("month_result.png")
        image_editable = ImageDraw.Draw(my_image)
        text = f"{username} - {reyting}"
        image_editable.text((980,592), text, (0, 0, 0), font=myFont)
        my_image.save("month_result.png")
      if i+1 == 8:
        my_image = Image.open("month_result.png")
        image_editable = ImageDraw.Draw(my_image)
        text = f"{username} - {reyting}"
        image_editable.text((980,695), text, (0, 0, 0), font=myFont)
        my_image.save("month_result.png")
      if i+1 == 9:
        my_image = Image.open("month_result.png")
        image_editable = ImageDraw.Draw(my_image)
        text = f"{username} - {reyting}"
        image_editable.text((980,798), text, (0, 0, 0), font=myFont)
        my_image.save("month_result.png")
      if i+1 == 10:
        my_image = Image.open("month_result.png")
        image_editable = ImageDraw.Draw(my_image)
        text = f"{username} - {reyting}"
        image_editable.text((980,898), text, (0, 0, 0), font=myFont)
        my_image.save("month_result.png")
      if i+1 == 11:
        my_image = Image.open("month_result.png")
        image_editable = ImageDraw.Draw(my_image)
        text = f"{client.get_user(top_month)} - {reyting}"
        image_editable.text((635,1026), text, (0, 0, 0), font=myFont)
        my_image.save("month_result.png")
    chat = client.get_channel(1007301750895677491)
    embed = discord.Embed(
            color=discord.Color.green()
        )
    file = discord.File("month_result.png", filename="image.png")
    embed.set_image(url="attachment://image.png")
    print('sending month reyt')
    if issent_month == 0:
      month_msg = await chat.send(file=file, embed=embed)
      issent_month = 1
    else:
      await month_msg.delete()
      month_msg = await chat.send(file=file, embed=embed)
    #await msg.edit(file=file, embed=embed)
    await asyncio.sleep(3600)#2592000

async def day_vipe():
  global day
  global day_msg
  global issent_day
  while True:
    reyt = {}
    print('day vipr func')
    for guild in client.guilds:
      for member in guild.members:
        voice = round(day[member.id]["voice"] / 120)
        reyt[member.id] = day[member.id]["text"] + voice
    non_reyt = {k: b for k, b in sorted(reyt.items(), key=lambda element: element[1], reverse=True)}
    sorted_reyt = {}
    non_list = list(non_reyt)
    for i in non_list:
      if client.get_user(i).bot == True:
        continue
      else:
        sorted_reyt[i] = non_reyt[i]
    keys_list = list(sorted_reyt)
    username = client.get_user(keys_list[0])
    reyting = sorted_reyt[keys_list[0]]
    my_image = Image.open("day_maket.png")
    image_editable = ImageDraw.Draw(my_image)
    text = f"{username} - {reyting}"
    image_editable.text((271,573), text, (0, 0, 0), font=myDayFont)
    my_image.save("result.png")
    chat = client.get_channel(1007301750895677491)
    embed = discord.Embed(
            color=discord.Color.green()
        )
    file = discord.File("result.png", filename="image.png")
    embed.set_image(url="attachment://image.png")
    print('sending day reyt')
    if issent_day == 0:
      day_msg = await chat.send(file=file, embed=embed)
      issent_day = 1
    else:
      await day_msg.delete()
      day_msg = await chat.send(file=file, embed=embed)
    print('day reyt sent')
    await asyncio.sleep(3600)

async def error_for():
  chat = client.get_channel(1006561978388590612)
  await chat.send('waka waka')

async def week_reset():
  while True:
    global top_week
    role = get(client.get_guild(997438713770541127).roles, id = 1005955084074627262)
    await client.get_guild(997438713770541127).get_member(top_week).remove_roles(role)
    reyt = {}
    for guild in client.guilds:
      for member in guild.members:
        voice = round(week[member.id]["voice"] / 120)
        reyt[member.id] = week[member.id]["text"] + voice
    non_reyt = {k: b for k, b in sorted(reyt.items(), key=lambda element: element[1], reverse=True)}
    sorted_reyt = {}
    non_list = list(non_reyt)
    for i in non_list:
      if client.get_user(i).bot == True:
        continue
      else:
        sorted_reyt[i] = non_reyt[i]
    keys_list = list(sorted_reyt)
    top_week = keys_list[0]
    role = get(client.get_guild(997438713770541127).roles, id = 1005955084074627262)
    await client.get_guild(997438713770541127).get_member(top_week).add_roles(role)
    print('role added')
    
    for guild in client.guilds:
        for member in guild.members:
          week[member.id] = {"voice": 0, "text": 0}
    await asyncio.sleep(604800)

async def month_reset():
  while True:
    print('a')
    global top_month
    role = get(client.get_guild(997438713770541127).roles, id = 1008811674695901316)
    await client.get_guild(997438713770541127).get_member(top_month).remove_roles(role)
    reyt = {}
    for guild in client.guilds:
      for member in guild.members:
        voice = round(month[member.id]["voice"] / 120)
        reyt[member.id] = month[member.id]["text"] + voice
    non_reyt = {k: b for k, b in sorted(reyt.items(), key=lambda element: element[1], reverse=True)}
    sorted_reyt = {}
    non_list = list(non_reyt)
    for i in non_list:
      if client.get_user(i).bot == True:
        continue
      else:
        sorted_reyt[i] = non_reyt[i]
    keys_list = list(sorted_reyt)
    top_month = keys_list[0]
    new_top = client.get_user(top_month)
    role = get(client.get_guild(997438713770541127).roles, id = 1008811674695901316)
    await client.get_guild(997438713770541127).get_member(top_month).add_roles(role)
    print('role added')
      
    for guild in client.guilds:
        for member in guild.members:
          month[member.id] = {"voice": 0, "text": 0}
    await asyncio.sleep(2592000)

async def day_reset():
  while True:
    for guild in client.guilds:
        for member in guild.members:
          day[member.id] = {"voice": 0, "text": 0}
    await asyncio.sleep(86400)

client.run('')
