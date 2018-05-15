#Tess Porter
#April 26, 2018
#CS 172 - 068

from monster import *

class wildebeest(monster):
    def __init__(self,n):
        self.__name = n
        self.__health = 72
        self.__defense_mode = False
    def __str__(self):
        return "I am a wildebeest named " + self.__name + "."
    def getName(self):
        return self.__name
    def getDescription(self):
        return "The wildebeest is both courageous and daring."
    def basicAttack(self,enemy):
        self.__defense_mode = False
        enemy.doDamage(11)
    def basicName(self):
        return "Horn Jab"
    def defenseAttack(self,enemy):
        self.__defense_mode = True
	#Do no damage. just defend
    def defenseName(self):
        return "Dodge and Juke"
    def specialAttack(self,enemy):
        self.__defense_mode = False #Can't Defend and attack
        enemy.doDamage(18)
    def specialName(self):
        return "Super Speed Run and Stab"
    def getHealth(self):
        return self.__health
    def doDamage(self,damage):
        if(self.__defense_mode):
            #Half Damage
            self.__health = self.__health-(damage//2)
        else:
            self.__health = self.__health - damage
    def resetHealth(self):
        self.__health = 72    
