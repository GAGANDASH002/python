#to map with real world scenarios , we started using objects in code.

'''class and object'''
#default constructor
class student:#creation of class
    name="kunal"
    def __init__(self):#self is the reference of created object
        print(self) 
        print("adding new student in database")
s1=student()#creation of object
print(s1.name)

#CONStRUCTOR

#parameterized constructor
class student:
    def __init__(self,name):
        self.name=name
        print("adding new student in database")
s1=student("Kunal Kapoor")
print(s1.name)

s2=student("Arjun")
print(s2.name)

'''class and instance attributes'''

'''data different for each object is called instance attributes
values same for all objects of a class are called class attributes'''

class student:
    college="MIT"#class attribute
    def __init__(self,name):
        self.name=name#instance attribute
        print("adding new student in database")
s1=student("Kunal Kapoor")
print(s1.name)
print(s1.college)

s2=student("Arjun")
print(s2.name)
print(s2.college)

#if name of instance and class attributes are same then instance attr. has higher priority

'''METHoDS'''

class student:
        def __init__ (self,name,marks):
             self.name=name
             self.marks=marks
        def show(self):
            print("welcome student",self.name)
        def get_marks(self):
             return self.marks
        
s1= student("Varun",90)
s1.show()

print("marks of ",s1.name,"are",s1.get_marks())

'''STATIC METHODS'''#methods that dont use self parameter

class student:
    @staticmethod
    def college():
        print("My college")

s1 = student()
s1.college()

#abstraction: hiding implementation details of class and only show essential features
#encapsulation: wrapping of data and functions in one unit(object).

class car:
     def __init__(self):
          self.acc=False
          self.brk=False
          self.clutch=False
     def start(self):
          self.clutch=True
          self.acc=True
          print("car has started")#other details were hidden

car1=car()
car1.start()

'''PRACTICE'''
"""Create Account class with 2 attributes -balance and accno
Create methods for debit credit and printing balance"""

class Account:
    def __init__(self,bal,accno):
        self.balance=bal
        self.accno=accno
    
    #credit method
    def credit(self,cash):
        self.balance+=cash
        print("Rs.",cash,"credited into your account",self.accno)
    
    #debit method
    def debit(self,amt):
         self.balance-=amt
         print("Rs",amt,"debited from your account",self.accno)

    #print details
    def show(self):
         print("account ",self.accno,"has balance",self.balance)

a = Account(2000,1234)
a.show()

a.debit(200)
a.show()

a.credit(100)
a.show()