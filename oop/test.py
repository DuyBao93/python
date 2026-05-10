#!/usr/bin/env python
from multipledispatch import dispatch

class Person:
    def __init__(self, *args):
        print("Init class Person successfully")
        match len(args):
            case 3 : self.name, self.age, self.male = args[0], args[1], args[2]
            case 2 : self.name, self.age, self.male = args[0], args[1], "default"
            case 1 : self.name, self.age, self.male = args[0], 0 , "default"
            case 0 : print("Don't have any argument")
    
    def getName(self):
        print("Name: %s" %(self.name))
    
    def getAge(self):
        print("Age: %d" %(self.age))
    
    def getMale(self):
        print("Male: %s" %(self.male))

    # Use @dispatch overload for function printInformation(_) 
    # @dispatch(object)
    # def printInformation(self, name):
    #     print("Name : %s \n" %(name))

    # @dispatch(object, int)          
    # def printInformation(self, name, age):
    #     print("Name : %s , Age : %d \n" %(name, age))

    # @dispatch(object, int, object)  
    # def printInformation(self, name, age, male):
    #     print("Name : %s , Age : %d, Male : %s \n" %(name, age, male))
    # end use @dispatch 

    #Use function check
    def printInformation(self, name = None, age=None, male=None):
        if name != None and age == None and male == None:
            print("Name : %s \n" %(name))
        elif name != None and age != None and male == None:
            print("Name : %s , Age : %d \n" %(name, age))
        elif name != None and age != None and male != None:
            print("Name : %s , Age : %d, Male : %s \n" %(name, age, male))
        

    def getInFormation(self):
        match self.name, self.age, self.male:
            case "default", 0, "default" : print("Don't have information ")
            case _ , 0, "default" : 
                self.printInformation(self.name)
            case _ , _ , "default" : 
                self.printInformation(self.name, self.age)
            case _ : 
                self.printInformation(self.name, self.age, self.male)
    
    def __del__(self):
        print('Destroy class Person successfully')
        del self.name,self.age,self.male

person = Person("Vo Duy Bao", 30)
# person.getName()
# person.getAge()
# person.getMale()
person.getInFormation()