#Tess Porter
#May 3, 2018

#Interface Class for a Stack
#Only allows access to the
#Stack commands of the built in list
class Stack:
    #Create a New Empty Stack
    def __init__(self):
        self.__S = []
    #Display the Stack
    def __str__(self):
        return str(self.__S)
    #Add a new element to top of stack
    def push(self,x):
        self.__S.append(x)
    #Remove the top element from stack
    def pop(self):
        return self.__S.pop()
    #See what element is on top of stack
    #Leaves stack unchanged
    def top(self):
        return self.__S[-1]

def postfix(exp):
    new_num = Stack()
    for num in exp.split():
        try:
            float(num)
            new_num.push(num)
        except ValueError as e:
            first = float(new_num.pop())
            second = float(new_num.pop())
            if num == '+':
                result = first+second
            elif num == '-':
                result = first-second
            elif num == '*':
                result = first * second
            else:
                result = first/second
            new_num.push(result)
    answer = new_num.pop()
    return answer
        

print('Welcome to Postfix Calculator\nEnter exit to quit.')

valid = True
while valid == True:
    user_input = input('Enter Expression:\n')
    if user_input.lower() == 'exit':
        valid = False
    else:
        print('Result:', postfix(user_input))
        
                