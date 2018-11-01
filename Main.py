#imports the discord and asyncio libraries.
import discord
import asyncio

#discord authentication token for bot and initializing bot.
token = 'NTA1MTMwNjQwMTUzMzc4ODI4.Drp1bg.aR_p1wU8JED-0gLUWV-UGdZ9lts'
prefix= "S2"

#set tachanka to  an instance of discord.Client so that we can pass class
#specific methods to it and contact the discord websocket.
tachanka = discord.Client()

#event decorator passes on_ready to event() which calls setattr() on to it.
@tachanka.event
async def on_ready():
    print("I'm actually top fragger in silver 2, I just can't get out.")

#@tachanka.event



tachanka.run(token)
