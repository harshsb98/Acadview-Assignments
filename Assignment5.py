#Q1
y=int(input("enter a year"))
if(y%4==0):
    print("leap year")

#Q2
l=int(input("side1"))
b=int(input("side2"))
if(l==b):
    print("square");
else:
    print("rectangle")

#Q3
a=int(input("enter age of 1st person"))
b=int(input("Enter age of 2nd person"))
c=int(input("Enter age of 3rd person"))
if(a==b==c):
    print("same ages")
elif(a>b):
    if(a>c):
        print("a is oldest",a)
    else:
        print("c is oldest",c)
    if(b<c):
        print("b is youngest",b)
    else:
        print("c is youngest",c)
else:
    if(b>c):
        print("b is oldest",b)
    else:
        print("c is oldest",c)
    if(a<c):
        print("a is youngest",a)
    else:
        print("c is youngest",c)

#Q4
x=int(input("enter prize"))
if(x<=50):
    print("No prize")
elif(x>=51&x<=150):
    print("wooden Dog")
elif(x>=151&x<=180):
    print("Book")
else:
    print("chocolates")

#Q5
x=int(input("enter units"))
x=x*100
if(x>1000):
    x=x*100-x*0.1*100
print(x)