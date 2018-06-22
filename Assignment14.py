#Q1

f=open("/home/harsh/PycharmProjects/Acadview-assignments/n","r")
l=f.readlines()
n=int(input("Enter the no. of last n lines of a file"))
c=0
for i in l:
    c+=1
print(c)
print(l[c-n:c])
