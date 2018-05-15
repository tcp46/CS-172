#Tess Porter
#April 15, 2018
#CS 172 Lab Section 068
#Homework 1 - Main

from socialite import Socialite

print('Welcome to CS 172: Socialite Homework')

valid = True
while valid == True:
    num_socialites = input('How many Socialites do you want to create?\n')
    try:
        #will verify that the value entered is a number
        num_socialites = int(num_socialites)
        valid = False
    except ValueError as e:
        print('Enter a number please!')
        valid = True

count = 1
#list to hold all of the socialite objects
people = []

while count <= num_socialites:
    Person = Socialite()
    
    print('Enter Data for Socialite', count)
    
    f = input('Enter First Name:\n')
    Person.setFirstName(f)
    
    l = input('Enter Last Name:\n')
    Person.setLastName(l)
    
    u = input('Enter User ID:\n')
    Person.setUserID(u)
    
    pic_url = input('Enter URL for Picture:\n')
    Person.setPicture(pic_url)
    
    web_url = input('Enter URL for Website:\n')
    Person.setWebsite(web_url)
    
    web_des = input('Enter Website Description:\n')
    Person.setDescription(web_des)
    
    print('Socialite Created\n')
    people.append(Person)
    
    count += 1 #increment the counter to move on to the next socialite

print('=====Socialite Information=====')
num = 0
#iterate through the list of socialite objects to print out the description of each
while num < len(people):
    person = people[num]
    person.str()
    num += 1
    