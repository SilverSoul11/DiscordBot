#imports the discord and asyncio libraries.
import discord
import asyncio
import PokemonUser
import pokemon
import re
import random
from AllFunctions import*

#discord authentication token for bot and initializing bot.
token = 'NTA1MTMwNjQwMTUzMzc4ODI4.Drp1bg.aR_p1wU8JED-0gLUWV-UGdZ9lts'


tachanka = discord.Client()

''' returns a generator with all the channels that tachanka can talk in, 
where cType is one of the Enumerations for discord.channelType which are
the strings text, voice, private, group and category. First part of the for loop
is taken from an example in the official documentation.'''

def getChannelWithPermission(cType): # Dict of type as key and actual property.
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
print(botDict)
botPartner = botDict["partner"]
bothpatstart = botPartner["object"].hp #I wont update these two so that I can restore the two players hp


@tachanka.event 
async def on_message(message):
	#become a pokemon trainer
	if message.content.startswith('$BecomeTrainer'):
		messContent = message.content
		user = message.author
		filteredMessList = re.split(r'\s', messContent)#checked docs for \s
		temp = PokemonUser.Puser(user,filteredMessList[1], filteredMessList[2])
		listOfTrainers.append(PokemonUser.createPuserDict(temp))
		await tachanka.send_message(message.channel, 'gz tachanka is happy for' +
			'you to become a trainer')




	if message.content.startswith('$Challenge'):
		for userDict in listOfTrainers: # 
			tmpDict = userDict['partner']
			pokemonObj = tmpDict['object']
			if userDict['Puserobj'].discordUObj == message.author:
				await tachanka.send_message(message.channel, 'pick a move ' + 
											str(pokemonObj.listOfMoveNames) + ' in this format $use XXX')


	if message.content.startswith('$use '):
		messContent = message.content
		messContent = str(messContent[5:])
		for userDict in listOfTrainers:
			if userDict['Puserobj'].discordUObj == message.author: #check for dictionary that matches the discord object
				tmpDict = userDict['partner']
				pokemonObj = tmpDict['object']
				for moveName in pokemonObj.listOfMoveNames:
					if messContent == moveName:
						attackMove = pokemonObj.moveList[messContent].damage


		
						bothp = botPartner["object"].hp #I will update this one
						print("bot hp before" + str(botPartner["object"].hp))

						await tachanka.send_message(message.channel, "Tachanka's charmander has " +
													str(botPartner["object"].hp) + " HP and " + str(pokemonObj.name) + " has " + str(pokemonObj.hp))


						await tachanka.send_message(message.channel, str(pokemonObj.name) + " inflicted " +
													str(int(attackMove)) + " damage")


						botPartner["object"].hp = int(botPartner["object"].hp - attackMove)
						print("bot hp after" + str(botPartner["object"].hp))
						#Bots turn to attack
						botChosenAttackList = random.sample(botPartner["object"].moveList.keys(), 1)
						print(botChosenAttackList)
						botChosenAttack = botChosenAttackList[0]		
						print(botPartner["object"].moveList[botChosenAttack])


						await tachanka.send_message(message.channel, "Tachanka Jr. strikes back with " +
													str(botChosenAttackList[0]) +" and inflicts " +
													str(int(botPartner["object"].moveList[botChosenAttack].damage)) + " damage")


						pokemonObj.hp = pokemonObj.hp - int(botPartner["object"].moveList[botChosenAttack].damage)


						await tachanka.send_message(message.channel, "Tachanka Jr. now has " + str(botPartner["object"].hp) +
													" and " + str(pokemonObj.name) + " has " + str(pokemonObj.hp))

						if pokemonObj.hp <= 0:
							botPartner["object"].hp = bothpatstart
							pokemonObj.hp = pokemonObj.hpatstart
							await tachanka.send_message(message.channel, "Tachanka WINS NO REMATCH HAHAHAHAHA")
							await tachanka.send_message(message.channel, "Psst just hit him again with $use xxx")


						elif botPartner["object"].hp <= 0:			
							botPartner["object"].hp = bothpatstart
							pokemonObj.hp = pokemonObj.hpatstart
							await tachanka.send_message(message.channel, "Tachanka Sleepy Zzzz")
							await tachanka.send_message(message.channel, "Psst just hit him again with $use xxx")

						else:
							await tachanka.send_message(message.channel, 'pick a move ' + 
															str(pokemonObj.listOfMoveNames) + ' in this format $use XXX')


tachanka.run(token)
