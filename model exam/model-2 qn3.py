student1=[41,40,41,45,40]
student2=[35,75,37,25,32]
mean1=sum(student1)/len(student1)
mean2=sum(student2)/len(student2)
a=[]
c=[]
e=[]
f=[]
for i in student1:
    if (i>mean1-4 and i<mean1+4):
        a.append(i)
        #b=len(a)
    elif (i>=mean1+4 or i<=mean1-4):
        c.append(i)
        
if len(c)>len(a):
    print("high deviation")
else:
    print("low deviation")

for i in student2:
    if (i>mean1-4 and i<mean1+4):
        e.append(i)
        #b=len(a)
    elif (i>=mean1+4 or i<=mean1-4):
        f.append(i)
        
if len(f)>len(e):
    print("high deviation")
else:
    print("low deviation")

