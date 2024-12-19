n = int(input())
base = 1

while 0<n:
    for i in range(3):
        if i ==0:
            print(base,end=" ")
        elif i==1:
            print(base*base, end=" ")
        else:
            print(base*base*base)
    base+=1
    n-=1