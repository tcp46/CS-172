#Mark Boady and Matthew Burlick
#Drexel University 2018
#CS 172

from frog import *
from wildebeest import *
from ghost import *
from unicorn import *
import random

#This function has two monsters fight and returns the winner
def monster_battle(m1, m2):

    #first reset everyone's health!
    m1.resetHealth()
    m2.resetHealth()

    #next print out who is battling
    print("Starting Battle Between")
    print(m1.getName()+": "+ m1.getDescription())
    print(m2.getName()+": "+ m2.getDescription())
		
    #Whose turn is it?
    
    attacker = None
    defender = None
    
    #Select Randomly whether m1 or m2 is the initial attacker
    #to other is the initial definder
    ######TODO######
    num = random.randint(1, 101) #select a random number b/w 1 and 100
    if num <= 50:
        attacker = m1
        defender = m2
    else:
        attacker = m2
        defender = m1
	
    print(attacker.getName() +" goes first.")
    
    #Loop until either 1 is unconscious or timeout
    while m1.getHealth() > 0 and m2.getHealth() > 0:
        #Determine what move the monster makes
	#Probabilities:
	#60% chance of standard attack
	#20% chance of defense move
	#20% chance of special attack move

	#Pick a number between 1 and 100
        move = random.randint(1,101)
	#It will be nice for output to record the damage done
        before_health = defender.getHealth()
		
	#for each of these options, apply the appropriate attack and 
	#print out who did what attack on whom
        if(move >=1 and move <= 60):
            #Attacker uses basic attack on defender
	    ######TODO######
            attacker.basicAttack(defender)
            print(attacker.getName(), 'used', attacker.basicName(), 'on', defender.getName())
        elif move>=61 and move <= 80:
	    #Defend!
	    ######TODO######
            attacker.defenseAttack(defender)
            print(attacker.getName(), 'used', attacker.defenseName(), 'on', defender.getName())
        else:
            #Special Attack!
	    ######TODO######
            attacker.specialAttack(defender)
            print(attacker.getName(), 'used', attacker.specialName(), 'on', defender.getName())
		
        
        #Print the names and healths after this round
	######TODO######
        if attacker.getHealth() < 0:
            print(attacker.getName(), 'at 0')
        else: 
            print(attacker.getName(), 'at', attacker.getHealth())
        
        if defender.getHealth() < 0:
            print(defender.getName(), 'at 0')
        else:
            print(defender.getName(), 'at', defender.getHealth())
        
        #Swap attacker and defender
	######TODO######
        temp = attacker
        attacker = defender
        defender = temp
	
    #Return who won
    ######TODO######
    if attacker.getHealth() > defender.getHealth():
        return attacker
    else:
        return defender

#----------------------------------------------------
if __name__=="__main__":
    #Every battle should be different, so we need to start the random number generator somewhere "random".
    #With no input Python will set the seed
    
    random.seed(0)
    
    print('Battle One\n')
    first = frog("Green Man")
    second = wildebeest("Pumba")
    winner1 = monster_battle(first,second)
	
    #Print out who won
    ####TODO####
    print('\n', winner1.getName(), 'is victorious!\n')
    
    print('Battle Two\n')
    third = ghost('Spooky Boy')
    fourth = unicorn('Glittery Rainbow')
    winner2 = monster_battle(third,fourth)
    print('\n', winner2.getName(), 'is victorious!\n')
    
    print('Championship Battle\n')
    champion = monster_battle(winner1, winner2)
    print('\n', champion.getName(), 'is the tournament champion!')