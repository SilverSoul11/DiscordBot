'''Pokemon game for discord, this is the pokemon class which will have several
sub classes depending on the Pokemon name, and owner. Hp is each Pokemon's
hitpoint ap is the amount of attack points each move has.'''

import PokemonAttack

class Pokemon_Abstract:

    def __init__(self, hp, ap, level,moveList):
        self.hp = hp
        self.ap = ap
        self.level = level
        self.movelist = moveList
        moveList = []
        hp += hp * random.randrange(0,0.2)

    def getHp(hp):
        return(hp)

    def getAp(ap):
        return(ap)


#Implementation of the first Pokemon Pikachu.
class Pikachu(PokemonAbstract):

    def __init__(self)
        super().__init__()
        self.attackMove = attackMove
        self.type = type
        moveList = ['Thunder Tackle', 'Lightning Bolt', 'Growl',
        'Tackle']
        type = electric

        for i in moveList:
            numberAssignmentVar = 1
            i = attackMove()
            i.ap = random.randrange(5,25)
            i.damage = random.randrange(10,20)
            i.attackNumber = numberAssignmentVar
            numberAssignmentVar += 1

        
#Optional: give a name to pokemon.
    def setName(self, name):
        self.name = name

    def attack(self, attackMove, otherPokemon):
#initilze MoveSet and save to localFile for reAccess.

#add code to save values to userID.pikachu file, by first grabbing the userID
#automatically.
