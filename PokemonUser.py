''' Pokemon User class defines a user with id and partner'''
import pokemon
import pokemonAttack

class Puser:


	def __init__(self, discordUObj, partnerName, partnerSpecies):
		self.discordUObj =  discordUObj
		self.partner = pokemon.pokemonConstructor(partnerName, partnerSpecies)


def createPuserDict(pUserObj):
	pUserDict = {}
	pUserDict["Puserobj"] = pUserObj
	pUserDict["partner"] = pUserObj.partner
	return pUserDict


def startChallenge(pUserObj, secondPUserObj):
	userDict = createPuserDict(pUserObj)
	otherDict = createPuserDict(secondPUserObj)
	userPokemon = userDict[partner]
	otherPokemon = otherDict[partner]