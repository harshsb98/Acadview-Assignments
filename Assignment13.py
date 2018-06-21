'''
#Q1 ZeroDivision Error
try:
    a = 3
    if(a<4):
        a=a/(a-3)
    print(a)
except ZeroDivisionError:
    print("Division by zero, not possible")

#Q2
try:
    l=[1,3,2]
    print(l[3])
except IndexError:
    print("Index Not Found")

#Q3 An exception

#Q4
# -5
# 6/0 result in 0

#Q5
l = [1, 3, 2]
try:
    import x
    a=int(input("Enter Index"))
    print(l[a])

except ImportError:
    print("Import error")

try:
    a=int(input("enter a no."))
    print(a)
except ValueError:
    print("enter an integer only")
try:
    l=[1,3,2]
    print(l[3])
except IndexError:
    print("Index Not Found")
'''
#Q6
class AgeTooSmallError(Exception):
    pass
while(True):
    try:
        x=int(input("Enter Age"))
        if(x<18):
            raise AgeTooSmallError
    except AgeTooSmallError:
        print("Enter an appropriate age")
    else:
        break


