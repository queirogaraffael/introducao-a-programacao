n = int(input())

base = 1

while 0<n:
    for i in range(4):
        if i==3:
            print("PUM")
        else:
            print(base, end= " ")
            base+=1
    base+=1
    n-=1