class Composition:
    def __init__(self, name):
        self.goodAgainst = []
        self.badAgainst = []
        self.name = name
    
    def isGoodAgainst(self, compositions):
        self.goodAgainst = compositions 

    def isBadAgainst(self, compositions):
        self.badAgainst = Composition

    def __eq__(self, other):
        return self.name == other.name

ATTACK  = Composition("ATTACK")
PROTECT = Composition("PROTECT")
CATCH   = Composition("CATCH")
SIEGE   = Composition("SIEGE")
SPLIT   = Composition("SPLIT")

ATTACK.isGoodAgainst([SPLIT, SIEGE])
PROTECT.isGoodAgainst([CATCH, ATTACK])
CATCH.isGoodAgainst([ATTACK, SPLIT])
SIEGE.isGoodAgainst([PROTECT, CATCH])
SPLIT.isGoodAgainst([SIEGE, PROTECT])

ATTACK.isBadAgainst([CATCH, PROTECT])
PROTECT.isBadAgainst([SPLIT, SIEGE])
CATCH.isBadAgainst([SIEGE, PROTECT])
SIEGE.isBadAgainst([ATTACK, SPLIT])
SPLIT.isBadAgainst([CATCH, ATTACK])