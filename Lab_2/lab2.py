#Tess Porter
#April 12, 2018
#CS 172 - Lab Section 068

import datetime

class Item:
    
    def __init__(self, n = '', p = 0, t = False):
        self.__name = n
        self.__price = p
        self.__taxable = t
    
    def __str__(self):
        return str(self.__name)
    
    def getPrice(self):
        return self.__price
    
    def getTax(self,tax_rate):
        tax = self.__price * tax_rate
        return tax

class Receipt:
    def __init__(self, t = 0, p = []):
        self.__tax_rate = t
        self.__purchases = p
    
    def __str__(self):
        print("----- Receipt", str(datetime.datetime.now()), '-----')
        i = 0
        sub_total = 0
        tax = 0
        while i < len(self.__purchases):
            
            if self.__purchases[i]._Item__taxable == True:
                tax += self.__purchases[i].getTax(0.06)
            
            item = self.__purchases[i].__str__()
            price = self.__purchases[i].getPrice()
            
            sub_total += price
            
            print('{:_<30}{:.2f}'.format(item,price))
            i += 1

        print('\nSub Total_____________________{:.2f}'.format(sub_total))
        print('Tax___________________________{:.2f}'.format(tax))
        print('Total_________________________{:.2f}'.format(sub_total + tax))
    
    def addItem(self, newItem):
        self.__purchases.append(newItem)

#------------------------------------------------------------------------------------
print('Welcome to Receipt Creator')

receipt = Receipt(0.06)

shopping = True
while shopping:
    name = input('Enter Item Name: ')
    price = float(input('Enter Item Price: '))
    taxable = input('Is the item taxable (yes/no): ')
    if taxable.lower() == 'yes':
        tax = True
    else:
        tax = False

    a = Item(name, price, tax)
    receipt.addItem(a)
    
    another = input('Add another item (yes/no): ')
    if another.lower() == 'yes':
        shopping = True
    else:
        shopping = False
        
receipt.__str__()
