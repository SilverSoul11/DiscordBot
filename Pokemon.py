'''Pokemon game for discord, this is the pokemon class which will have several
sub classes depending on the Pokemon name, and owner. Hp is each Pokemon's
hitpoint ap is the amount of attack points each move has.'''
import random
class Pokemon:
    def __init__(self, hp, ap, level):
        self.hp = hp
        self.ap = ap
        self.level = level
        hp += hp * random.randrange(0,0.2)

    def getHp(hp):
        return(hp)

    def getAp(ap):
        return(ap)

'''Creating an attackMove class so attackMove objects can have a damage, and ap
Value attached to them.'''
class attackMove:

    def getMoveAssets():
        return()

#Implementation of the first Pokemon Pikachu.
class Pikachu(Pokemon):
    def __init__(self, hp, ap, attack, attackMove,type, attackNumber)
        super().__init__(hp, ap, attack)
        self.attackMove = attackMove
        self.type = type
        moveList = ['Thunder Tackle', 'Lightning Bolt', 'Growl',
        'Tackle']
        for i in moveList:
            numberAssignmentVar = 1
            i = attackMove()
            i.ap = random.randrange(5,25)
            i.damage = random.randrange(10,20)
            i.attackNumber = numberAssignmentVar
            numberAssignmentVar += 1
        type = electric
#Optional: give a name to pokemon.
    def setName(self, name):
        self.name = name

    def attack(self, attackMove, otherPokemon):
#initilze MoveSet and save to localFile for reAccess.

#add code to save values to userID.pikachu file, by first grabbing the userID
#automatically.
