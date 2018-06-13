
#Q1
r=float(input("Enter radius"))
def area(r):
    return 3.14*r*r
print(area(r))

#Q2

for x in range(1,1001):
    sum=1
    i=2
    while(i<=x/2):
        if(x%i==0):
            sum=sum+i
        i=i+1
    if(x==sum):
        print(x,"perfect")

#Q3
def table(a,i):
    if(i<=10):
        print("12*%d=%d"%(i,a*i))
        table(a,i+1)
table(12,1)


#Q4
x=int(input("Enter your base"))
y=int(input("enter your exponent"))
print(pow(x,y))
def pow(x,y):
    if(y>0):
        return x*pow(x,y-1)
    else:
        return 1


#Q5
def fact(a):
    if(a==1):
        return 1
    else:
        return a*fact(a-1)
x=int(input("enter no."))
y=int(input("enter no."))
dict={'%d'%(x):'%d'%(fact(x)),'%d'%(y):'%d'%(fact(y))}
print(dict)