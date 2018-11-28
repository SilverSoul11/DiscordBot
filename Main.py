#imports the discord and asyncio libraries.
import discord
import asyncio
import PokemonUser
import pokemon
import re

#discord authentication token for bot and initializing bot.
token = 'NTA1MTMwNjQwMTUzMzc4ODI4.Drp1bg.aR_p1wU8JED-0gLUWV-UGdZ9lts'


tachanka = discord.Client()

''' returns a generator with all the channels that tachanka can talk in, 
where cType is one of the Enumerations for discord.channelType which are
the strings text, voice, private, group and category. First part of the for loop
is taken from an example in the official documentation.'''

def getChannelWithPermission(cType):
	values = {"text":discord.ChannelType.text,
			  "voice":discord.ChannelType.voice,
			  "private":discord.ChannelType.private,
			  "group":discord.ChannelType.group,
		}

	for server in tachanka.servers: #from here 
		for channel in server.channels:#to here
			if cType in values:
				if channel.type == values[cType]:
					yield channel



'''event decorator is a decerator that registers an event to listen to and 
takes a coroutine function as input.'''


@tachanka.event #looked at the "guess" example on github to see how it's structured
async def on_ready():
	print("I'm actually top fragger in silver 2, I just can't get out.")


listOfTrainers = []

#Bot initialization
opponent = PokemonUser.Puser("bot", "TachankaChar", "charmander")
listOfTrainers.append(PokemonUser.createPuserDict(opponent))
botDict = listOfTrainers[0]
print(str(botDict)) 




@tachanka.event 
async def on_message(message):

	#become a pokemon trainer
	if message.content.startswith('$BecomeTrainer'):
		messContent = message.content
		user = message.author
		filteredMessList = re.split(r'\s', messContent)#checked docs for \s
		temp = PokemonUser.Puser(user,filteredMessList[1], filteredMessList[2])
		listOfTrainers.append(PokemonUser.createPuserDict(temp))
		print(str(listOfTrainers))
		await tachanka.send_message(message.channel, 'gz tachanka is happy for' +
			'you to become a trainer')



	if message.content.startswith('$Challenge'):
		for userDict in listOfTrainers:
			print(str(userDict['Puserobj'].discordUObj))
			print(str(message.author))
			if userDict['Puserobj'].discordUObj == message.author:
				tmpDict = userDict['partner']
				pokemonObj = tmpDict['object']
				hpBefore = pokemonObj.hp
				await tachanka.send_message(message.channel, 'pick a move ' + 
				str(pokemonObj.listOfMoveNames) + ' in this format $use XXX')


	if message.content.startswith('$use '):
		messContent = message.content
		messContent = messContent[4:]
		counter = 0

		for userDict in listOfTrainers:
			tmpDict = userDict['partner']
			pokemonObj = tmpDict['object']

			for moveName in pokemonObj.listOfMoveNames:
				if messContent == moveName:
					moveProp = pokemonObj.moveList[counter]
				else:
					counter += 1




	
tachanka.run(token)