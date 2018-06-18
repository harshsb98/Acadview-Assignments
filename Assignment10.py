#Q1
class Animal:
    def animal_attribute(self):
        print("Fourlegs")

class Tiger(Animal):
    def tigute(self):
        print("roar")
t=Tiger()
t.animal_attribute()
t.tigute()

#Q2
# A B
# A B

#Q3
class Cop:
    def __init__(self,name,age,work,designation,experience):
        self.name=name
        self.age=age
        self.work=work
        self.designation=designation
        self.experience=experience
    def add(self):
        x=str(input("Enter work"))
        y=str(input("enter designation"))
        z=int(input("Enter experience"))
        self.work=x
        self.designation=y
        self.experience=z
    def update(self):
        x = str(input("Enter work"))
        y = str(input("enter designation"))
        z = int(input("Enter experience"))
        a=str(input("enter name"))
        b=int(input("enter age"))
        self.work = x
        self.designation = y
        self.experience = z
        self.name=a
        self.age=b
    def display(self):
        print(self.age,self.name,self.work,self.experience,"years",self.designation)
C=Cop("harsh",20,"engineer","radaur","2")
C.display()

class Mission(Cop):
    def add_mission_details(self):
        self.n=C.name
        self.a=C.age
        self.w=C.work
        self.e=C.experience
        self.d=C.designation
    def DisplayDetails(self):
        print(self.n,self.a,self.w,self.e,self.d)
m=Mission("harsh",69,"engineer","radaur","5")
m.add_mission_details()
m.display()
m.DisplayDetails()

#Q4
class shape:
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def Area(self):
        return self.l*self.b
class rectangle(shape):
    def __init__(self,l,b):
        self.l=l
        self.b=b
class square(shape):
    def __init(self,l,b):
        self.l=l
        self.b=b
r=rectangle(4,6)
s=square(5,5)
print(r.Area(),s.Area())