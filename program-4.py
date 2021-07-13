list=[]
count=0
dict={}
n=int(input("enter number of elements:"))
for i in range(0,n):
    ele=int(input())
    list.append(ele)
print(list)
for j in range(1,10):
    for i in range(len(list)):
        if list[i]%j==0:
            count=count+1
    for k in range(1):
        print(j,":",count,end=",")
        count=0


