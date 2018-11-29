'''Pokemon game for discord, this is the pokemon class which will have several
sub classes depending on the Pokemon name, and owner. Hp is each Pokemon's
hitpoint ap is the amount of attack points each move has.'''

import pokemonAttack
import random

class pokemon():
    def __init__(self):  
        self.level = random.randrange(1,5)
        self.hp = int(100 * (self.level ** (1 / 2)))
        self.hpatstart = self.hp


class pikachu(pokemon):
    def __init__(self):
        super().__init__()
        self.type = "Electric"
        self.species = "pikachu"
        self.listOfMoveNames = ("Lightning Bolt","Thunder tackle",
        "Tail Whip","Thunder Bolt")


class charmander(pokemon):
    def __init__(self):
        super().__init__()
        self.type = "Fire"
        self.species = "charmander"
        self.listOfMoveNames = ("Explosion","Blast Burn",
        "Tail Whip","Over Heat")


#Use this method to create a pokemon and assign a name to it
def pokemonConstructor(pname, species):
    partnerDict = {}
    if species.lower() == "pikachu":
        pObject = pikachu()
        pObject.name = pname
        pikachuMl= pokemonAttack.create_Move_List(pObject.listOfMoveNames,
        pObject.level)
        pObject.moveList = pikachuMl
        partnerDict["object"] = pObject
        return partnerDict

    elif species.lower() == "charmander":
        pObject = charmander()
        charmanderMl= pokemonAttack.create_Move_List(pObject.listOfMoveNames,
        pObject.level)
        pObject.moveList = charmanderMl
        partnerDict["object"] = pObject
        return partnerDict



'''giving None  to hp and level so that I can generate a random number for it in 
__init__ this idea was taken from a stack overflow question with the following 
url = https://stackoverflow.com/questions/19473185/what-is-a-none-value '''