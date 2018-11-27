'''Creating an attackMove class so attackMove objects can have a damage, and ap
Value attached to them.'''
import random

class attack_Move:
	
	def __init__(self, name, ap, damage):
		self.name = name
		self.ap = ap
		self.damage = damage
		


	def getMoveAssets(self):
		assets_List = dir(self)


#Interactive Move creator, returns a list moveList with attack moveobjects.

def create_Move_List(moveNames):
	moveList = []
	for i in moveNames:
		ap = random.randrange(5,25)
		damage = random.randrange(10,20)
		moveList.append(attack_Move(i, ap, damage))
	return moveList
