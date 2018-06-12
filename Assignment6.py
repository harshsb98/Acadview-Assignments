#Q1
for i in range(10):
    print("%d"%(int(input("enter no.%d"%(i+1)))))

#Q2
while(True):
    print("k")

#Q3
num=[]
sq=[]
for i in range(3):
    x=int(input("enter ur no."))
    num.append(x)
    sq.append(x*x)
print(sq,num)

#Q4
ints=[]
floats=[]
strings=[]
a=[1,2,"hello",1.223,"hey",3.4,"xXx",192]
for i in a:
    if(str==type(i)):
        strings.append(i)
    elif(int==type(i)):
        ints.append(i)
    else:
        floats.append(i)
print(ints,floats,strings)

#Q5
list=[]
for i in range(1,101):
    list.append(i)

#Q6
for i in range(1,5):
    print("*"*i)

#Q7
dict={'a':'1','b':'2','c':'3'}
for i in dict.keys():
    print(i)

#Q8
l=[]
for i in range(4):
    x=int(input("enter no."))
    l.append(x)
y=int(input("enter no. to be searched"))
for i in l:
    if(y==i):
        l.remove(i)
print(l)
