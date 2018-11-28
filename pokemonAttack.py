'''Creating an attackMove class so attackMove objects can have a damage, and ap
Value attached to them.'''
import random

class attack_Move:
	
	def __init__(self, ap, damage):
		self.ap = ap
		self.damage = damage
		


	def getMoveAssets(self):
		assets_List = dir(self)


#Interactive Move creator, returns a list moveList with attack moveobjects.

def create_Move_List(moveNames, level):
	moveList = {}
	for i in moveNames:
		ap = random.randrange(5,25)
		damage = random.randrange(10,20) * (level ** (1/2))
		moveList[i] = attack_Move(ap, damage)
	return moveList
