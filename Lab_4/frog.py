#Tess Porter
#April 26, 2018
#CS 172 - 068

from monster import *

class frog(monster):
    def __init__(self,n):
        self.__name = n
        self.__health = 55
        self.__defense_mode = False
    def __str__(self):
        return "I am a frog named " + self.__name + "."
    def getName(self):
        return self.__name
    def getDescription(self):
        return "The frog is both stealthy and skilled in combat."
    def basicAttack(self,enemy):
        self.__defense_mode = False
        enemy.doDamage(8)
    def basicName(self):
        return "Long tongue noose"
    def defenseAttack(self,enemy):
        self.__defense_mode = True
	#Do no damage. just defend
    def defenseName(self):
        return "Lily Pad Shelter"
    def specialAttack(self,enemy):
        self.__defense_mode = False #Can't Defend and attack
        enemy.doDamage(16)
    def specialName(self):
        return "Super Leap and Karate Kick"
    def getHealth(self):
        return self.__health
    def doDamage(self,damage):
        if(self.__defense_mode):
            #Half Damage
            self.__health = self.__health-(damage//2)
        else:
            self.__health = self.__health - damage
    def resetHealth(self):
        self.__health = 55