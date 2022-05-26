import discord, os, asyncio
import random
import time
from discord.ext import commands, tasks
from flask import Flask
from threading import Thread



token = 'TOKEN HERE'
st = 1
#Bot prefix, like ?help

prefix = "?"


def endSong(guild, path):

    os.remove(path)






#Colors


def RandomColor():

    randcolor = discord.Color(random.randint(0x000000, 0xFFFFFF))

    return randcolor



client = discord.Client()

client = commands.Bot(command_prefix=prefix, self_bot=True)

client.remove_command('help')





@client.command(name='hello', aliases=['h', 'hh'])
#test command
async def hello(ctx):

    #await ctx.message.delete()
    await ctx.send("world")


@client.command(name="help")
async def help(ctx):
    await ctx.send('''
                 ```
DankFarmer 2
Bot Status: ✓ Online
Commands: FarmDank, Help, StopFarm (Takes a little while)
Made with ♥ by AppleCraxkhead
                 ```''')

@client.command(name="stopfarm")
async def stopfarm(ctx):
  global st
  st = 2
  print('Farm Mode Deactivated.')
  await ctx.send(f"🧑‍🌾Farm mode deactivated. Farming will cease after cycle is complete.")

async def farmMode(ctx):
    global st
    rev = 0
    while 1 == 1:
      time.sleep(30)
      await ctx.send("pls hunt")
      random_number = random.randint(1, 10)
      time.sleep(random_number)
      await ctx.send("pls fish")
      random_number = random.randint(1, 10)
      time.sleep(random_number)
      await ctx.send("pls dig")
      random_number = random.randint(1, 10)
      time.sleep(random_number)
      await ctx.send("pls beg")
      rev = rev + 1
      print(f"Cycle #{str(rev)} Completed")
      dis = st
      print(dis)
      if dis == 2:
        time.sleep(1)
        await ctx.send(f"Farming Complete after {str(rev)} cycles  ")
        break
      else: 
        pass
      


@client.command(name="dankfarm")
async def dankfarm(ctx):
    print("Farming Mode Activated: Beginnning farming tasks")
    await ctx.send(
        "🧑‍🌾 Farm mode activated. Farming will begin in 30 seconds.  Sit back and Relax 😎"
    )
    await farmMode(ctx)

@tasks.loop(minutes=300)
async def farmDaily():
    channel = client.get_channel(ID OF TARGET CHANNEL HERE)
    await channel.send("pls daily")


@client.event
async def on_ready():
    print("Starting Tasks...")
    farmDaily.start()
    print(f"Connection Successful")


try:
  time.sleep(5)
  client.run(token, bot=False)
except:
    os.system("kill 1")
