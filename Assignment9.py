
#Q1
class Circle:
    def __init__(self,radius):
        self.r=radius
    def getArea(self):
        return 3.14*self.r*self.r
    def getCircumfrence(self):
        return 2*3.14*self.r
x=Circle(5)
print(x.getArea(),x.getCircumfrence())

#Q2
class Student:
    def __init__(self,n,r):
        self.n=n
        self.r=r
    def display(self):
        print(self.n,self.r)
S=Student(1,5)
S.display()

#Q3
class Temperature:
    def convertFahrenheit(self,celcius):
        print(celcius*9/5+32)
    def convertCelcius(self,f):
        print((f-32)*5/9)
t=Temperature()
t.convertCelcius(5)
t.convertFahrenheit(6)

#Q4
class MovieDetails:
    def __init__(self):
        self.MovieName="October-Sky"
        self.ArtistName=" Jake Gyllenhaal Chris Cooper Chris Owen Laura Dern"
        self.YearOfRelease=1999
        self.ratings=5
    def display(self):
        print("MovieName:",self.MovieName,"ArtistName:",self.ArtistName,"yearof release:",self.YearOfRelease,"Ratings:",self.ratings )
    def update(self):
        self.ratings=int(input("enter  the ratings"))
X=MovieDetails()
X.display()
X.update()
X.display()

#Q5
class Expenditure:
    def __init__(self,e,s):
        self.e=e
        self.s=s
    def ts(self):
        self.t=self.e+self.s
    def display(self):
        print("total salary:",self.t)
E=Expenditure(1233213,213123)
E.ts()
E.display()