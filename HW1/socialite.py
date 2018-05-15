#Tess Porter
#April 15, 2018
#CS 172 Lab Section 068
#Homework 1 - Socialites

class Socialite:
    
    #constructor method with default parameters
    
    def __init__(self, l_name = '', f_name = '', p = '', w = '', d = '', u_id = ''):
        self.__last = l_name
        self.__first = f_name
        self.__pic = p
        self.__web = w
        self.__des = d
        self.__id = u_id
    
    #string method
    
    def str(self):
        print('Name:', self.__first, self.__last, '\nUser ID:', self.__id, '\nPicture:', self.__pic, '\nWebsite:', self.__web, '\nWebsite Description:', self.__des,'\n')
    
    #mutator methods
    
    def setLastName(self, l):
        self.__last = l
    
    def setFirstName(self, f):
        self.__first = f
    
    def setPicture(self, p):
        self.__pic = p
    
    def setWebsite(self, w):
        self.__web = w
    
    def setDescription(self, d):
        self.__des = d
        
    def setUserID(self, u):
        self.__id = u
    
    #accessor methods
    
    def getLastName(self):
        return self.__last
    
    def getFirstName(self):
        return self.__first
    
    def getPicture(self):
        return self.__pic
    
    def getWebsite(self):
        return self.__web
    
    def getDescription(self):
        return self.__des
    
    def getUserID(self):
        return self.__id