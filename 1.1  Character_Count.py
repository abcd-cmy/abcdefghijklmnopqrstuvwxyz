n=int(input("Enter the no of frames "))
l=[]
l2=[]
for i in range(0,n):
    x=input()
    l.append(x)
    l2.append(len(x)+1)
sender=''
for i in range(0,n):
    sender+=str(l2[i])+l[i]
print(sender)
data=input("enter message\n")
i=0
inv=0
while(i<len(data)):
    if(data[i].isnumeric()==True):
      print(data[i+1:int(data[i])+i])
      i+=int(data[i])