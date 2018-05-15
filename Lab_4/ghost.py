# Erin Ingram
# Lab section 68

from monster import *

class ghost(monster):
    def __init__(self, n):
        self.__name = n
        self.__health = 50
        self.__defense_mode = False

    def __str__(self):
        return "I am a Ghost named " + self.__name + "."

    def getName(self):
        return self.__name

    def getDescription(self):
        return "A restless spirit back for more. Boo!"

    def basicAttack(self, enemy):
        self.__defense_mode = False  # Can't defend and attack
        enemy.doDamage(5)

    def basicName(self):
        return "Haunt"

    def defenseAttack(self, enemy):
        self.__defense_mode = True

    # Do no damage. just defend
    def defenseName(self):
        return "Go invisible"

    def specialAttack(self, enemy):
        self.__defense_mode = False  # Can't Defend and attack
        enemy.doDamage(10)

    def specialName(self):
        return "Ghostly Possession"

    def getHealth(self):
        return self.__health

    def doDamage(self, damage):
        if self.__defense_mode:
            # Half Damage
            self.__health = self.__health - (damage // 2)
        else:
            self.__health = self.__health - damage

    def resetHealth(self):
        self.__health = 50

