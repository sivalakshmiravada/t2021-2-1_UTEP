num=int(input("enter a number"))
for i in range(1,num+1,2):
        if i+1<=num:
                for l in range(1,3,1):
                        odd=1
                        for j in range(i):
                                print(odd,end=",")
                                odd+=2
                        print("\n")
        else:
                odd=1
                for j in range(i):
                        print(odd,end=",")
                        odd+=2