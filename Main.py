#imports the discord and asyncio libraries.
import discord
import asyncio
import Greet


#discord authentication token for bot and initializing bot.
token = 'NTA1MTMwNjQwMTUzMzc4ODI4.Drp1bg.aR_p1wU8JED-0gLUWV-UGdZ9lts'
prefix = "S2"




tachanka = discord.Client()

''' returns a generator with all the channels that tachanka can talk in, 
where cType is one of the Enumerations for discord.channelType which are
the strings text, voice, private, group and category.'''

def getChannelWithPermission(cType):
	values = {"text":discord.ChannelType.text,
			  "voice":discord.ChannelType.voice,
			  "private":discord.ChannelType.private,
			  "group":discord.ChannelType.group,
		}

	for server in tachanka.servers:
		for channel in server.channels:
			if cType in values:
				if channel.type == values[cType]:
					yield channel


'''event decorator passes on_ready coroutine to discord.client.event() which
is a decerator that registers an event to listen to and takes a coroutine
function as input.'''


@tachanka.event
async def on_ready():
	print("I'm actually top fragger in silver 2, I just can't get out.")



#@tachanka.event
#async def on_message():
	
tachanka.run(token)