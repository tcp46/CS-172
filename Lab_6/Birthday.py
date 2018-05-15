#Tess Porter
#May 9, 2018
#CS 172-064

class Birthday():
    def __init__(self, m, d, y):
        self.__day = d
        self.__month = m
        self.__year = y
    def __str__(self):
        return str(self.__month) + '/' + str(self.__day) + '/' + str(self.__year)
    def __hash__(self):
        hash = (int(self.__day) + int(self.__month) + int(self.__year)) % 12
        return hash
    def __eq__(self, other):
        return self.__day == other.__day and self.__month == other.__month and self.__year == other.__year
        
if __name__ == '__main__':
    mine = Birthday(9, 23, 1998)
    print(mine)
    print(hash(mine))
    yours = Birthday(6, 29, 2008)
    if mine == yours:
        print('Same!')
    else:
        print('Not same!')