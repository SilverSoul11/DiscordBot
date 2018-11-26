'''Creating an attackMove class so attackMove objects can have a damage, and ap
Value attached to them.'''
import random

class attack_Move:
	
	def __init__(self, ap, damage, attackNumber):
		self.ap = ap
		self.damage = damage
		self.attackNumber = attackNumber

	def getMoveAssets(self):
		assets_List = dir(self)



def createMoveList(listOfMoves):
	for i in listOfMoves:
		numberAssignmentVar = 1
		randomAp = random.randrange(5,25)
		randomDmg = random.randrange(10,20)
		randomAn = numberAssignmentVar
		i = attack_Move(randomAp, randomDmg, randomAn)
		numberAssignmentVar += 1