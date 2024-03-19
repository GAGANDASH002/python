'''del keyword'''
#used to delete object and its properties

class student:
    def __init__(self,name):
        self.name=name
s1=student("Gagan")
#del s1
print(s1.name)

'''private attributes and methods'''
class Account:
    def __init__(self,accno,password):
        self.accno=accno
        self.__password=password#private 
    def __hello():#private method
        print("hello")

acc1= Account("123","@002")
print(acc1.accno)
#print(acc1.__password)#we dont want password as public

'''INHERITANCE'''

#one class(child) derives the methods and properties of another class(parent)
#singlelevel inheritance
class car:
    @staticmethod
    def start():
        print("car start")
    
    @staticmethod
    def stop():
        print("car stopped")

class toyota (car):
    def __init__(self,name):
        self.name=name

car1=toyota("fortuner")

print(car1.name)
car1.start()#inherited method from parent class 'car'

#multilevel inheritance
class car:
    @staticmethod
    def start():
        print("car start")
    
    @staticmethod
    def stop():
        print("car stopped")

class toyota (car):
    def __init__(self,name):
        self.name=name

class Fortuner(toyota):
    def __init__(self,factory):
        self.factory=factory
car =Fortuner("toyota India")


car.start()
print(car.factory)

#multiple level inheritance

class A:
    varA="welcome to class A"

class B:
    varB="welcome to class B"


class C(A,B):
    varC="welcome to class C"

c=C()
print(c.varC)
print(c.varB)#inherited from class B
print(c.varA)#inherited from class A

'''super method-used to access methods of parent class'''

class car:
    def __init__ (self,type):
        self.type=type

    @staticmethod
    def start():
        print("car start")
    
    @staticmethod
    def stop():
        print("car stopped")

class toyota (car):
    def __init__(self,name,type):
        super().__init__(type)
        self.name=name
        super().start()

car=toyota("prius","EV")
print(car.type)


class person:
    
    name="anonymous"

    @classmethod#changes the class attribute as well
    def changename(cls,name):
        cls.name=name#cls is now referring to class
p1=person()
p1.changename("Karan")
print(p1.name)
print(person.name)#class attribute is now same as instance attribute

'''property decorator'''
class student:
    def __init__(self,phy,chem,math):
        self.phy=phy
        self.chem=chem
        self.math=math
    @property#property decorator is used to use a method as a property
    def percentage(self):
        return str((self.phy+self.math+self.chem)/3)+"%"
    
s=student(98,96,95)
print(s.percentage)

s.phy=89
print(s.percentage)

"""POLYmORPHISM"""
#operator overloading-same operator can have different meanings

print(1+2)#3
print("Gagan"+"Dash")#concatenate
print([1,2,3]+[4,5,6])#merge

class complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img
    def show(self):
        print(self.real,"i+",self.img,"j")
    def __add__ (self,num2):#__add__ is a dunder function
        newreal=self.real+num2.real
        newimg=self.img+num2.img
        return complex(newreal,newimg)
    
c1=complex(1,2)
c1.show()
c2=complex(2,3)
c2.show()
c3=c1+c2#direct sum of complex nums is done instead of using add function
print("sum of two complex nums are",c3.show())

'''PRACTICE'''

class circle:
    def __init__ (self,rad):
        self.rad=rad
    def area(self):
        return 3.14*self.rad*self.rad
        
    def perimeter(self):
        return 2*3.14*self.rad
       
cir=circle(4)
print(cir.area())
print(cir.perimeter())

class employee:
    def __init__(self,role,dept,sal):
        self.role=role
        self.dept=dept
        self.sal=sal
    def show(self):
        print("role",self.role)
        print("dept",self.dept)
        print("sal",self.sal)

class Engineer(employee):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        super().__init__("engineer","signals",150000)

e = employee("aviator","flying",200000)
e.show()
e1=Engineer("Goose","25")
e1.show()

class order:
    def __init__(self,item,price):
        self.item=item
        self.price=price
    def __gt__(self,odr2):
        return self.price>odr2.price  
    def __lt__(self,odr2):
         return self.price<odr2.price  


o1=order("table",2000)
o2=order("chair",4000)
print(o1>o2)
print(o1<o2)