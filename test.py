import datetime
import random
num=0
b=0
arr = []
for i in range(1, 126) :
    arr.append(i)
a=datetime.datetime.now()
while b<1:
    num=num+1
    x = random.randint(0,124)
    y = random.randint(0,124)
    while x==y :
        y = random.randint(1,125)
    v=arr[x]
    w=arr[y]
    arr[x]=w
    arr[y]=v
    print(arr[x],',',arr[y])
    print(num)
    b=(datetime.datetime.now()-a).seconds
for j in arr :
    print(j,end=" ")
    
def val(list) :
    total =0
    for j in arr :
        print(j,end=" ")