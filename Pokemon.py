'''Pokemon game for discord, this is the pokemon class which will have several
sub classes depending on the Pokemon name, and owner. Hp is each Pokemon's
hitpoint ap is the amount of attack points each move has.'''

import PokemonAttack

class Pokemon_Abstract:

    def __init__(self, hp, ap, level):
        self.hp = hp
        self.ap = ap
        self.level = level
        hp += hp * random.randrange(0,0.2)

    def getHp(hp):
        return(hp)

    def getAp(ap):
        return(ap)


#Implementation of the first Pokemon Pikachu.
class Pikachu(PokemonAbstract):

    def __init__(self, moveList):
        super().__init__()
        self.type = type
        type = Electric
        listOfMoveNamesP = ["Lightning Bolt"."Thunder tackle".
        "Tail Whip"."Thunder Bolt"]

        
class Charmander(PokemonAbstract):

    def __init__(self, moveList):
        super().__init__()
        self.type = type
        type = Fire
        listOfMoveNamesC = ["Explosion"."Blast Burn".
        "Tail Whip"."Over Heat"]

#Use this method to create a pikachu.
    def pokemonConstructor(name, species, listOfMoveNames):
        if species == "pikachu":
            name = pikachu()
            pikachuMl= PokemonAttack.create_Move_List(listOfMoveNamesP)
            name.moveList = pikachuMl

        elif speicies == "Charmander":
            name = Charmander()
            charmanderMl= PokemonAttack.create_Move_List(listOfMoveNamesP)
            name.moveList = charmanderML


    def attack(self, attackMove, otherPokemon):
#initilze MoveSet and save to localFile for reAccess.

#add code to save values to userID.pikachu file, by first grabbing the userID
#automatically.
