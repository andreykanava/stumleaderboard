import asyncio
import discord
from discord.ext import commands
import json
import time

client = commands.Bot(command_prefix='+', intents = discord.Intents(messages = True, guild_messages = True, members = True, guilds = True, voice_states = True))
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
    embed = discord.Embed(color=discord.Color.green())
    for i in range(3):
      keys_list = list(sorted_reyt)
      username = client.get_user(keys_list[i])
      reyting = sorted_reyt[keys_list[i]]
      embed.add_field(name=f"{i+1}", value=f'{username}, {reyting}')
    chat = client.get_channel(1005796493757780019)
    await chat.send(embed=embed)
    for guild in client.guilds:
      for member in guild.members:
        week[member.id] = {"voice": 0, "text": 0}
    await asyncio.sleep(60)


async def month_vipe():
  global month
  while True:
    reyt = {}
    for guild in client.guilds:
      for member in guild.members:
        voice = round(month[member.id]["voice"] / 120)
        reyt[member.id] = month[member.id]["text"] + voice
    sorted_reyt = {k: b for k, b in sorted(reyt.items(), key=lambda element: element[1], reverse=True)}
    embed = discord.Embed(color=discord.Color.green())
    for i in range(3):
      keys_list = list(sorted_reyt)
      username = client.get_user(keys_list[i])
      reyting = sorted_reyt[keys_list[i]]
      embed.add_field(name=f"{i+1}", value=f'{username}, {reyting}')
    chat = client.get_channel(1005796493757780019)
    await chat.send(embed=embed)
    for guild in client.guilds:
      for member in guild.members:
        month[member.id] = {"voice": 0, "text": 0}
    await asyncio.sleep(2592000)

client.run('MTAwNTQ3NDM3MzIzMjI1MDk3MQ.GzM1u6.27UKqUdBdJdqCFrqZI22_ThHOkM2z-BZqDszvU')
