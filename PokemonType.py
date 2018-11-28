
import PokemonAbs
#Implementation of the first Pokemon Pikachu.

class Pikachu(Pokemon_Abstract):

    def __init__(self):
        super().__init__()
        self.type = "Electric"
        self.species = "pikachu"
        self.listOfMoveNames = ["Lightning Bolt","Thunder tackle",
        "Tail Whip","Thunder Bolt"]


class Charmander(Pokemon_Abstract):

    def __init__(self):
        super().__init__()
        self.type = "Fire"
        self.species = "charmander"
        self.listOfMoveNames = ["Explosion","Blast Burn",
        "Tail Whip","Over Heat"]
