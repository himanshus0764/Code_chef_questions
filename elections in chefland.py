a=int(input())
for i in range(a):
    arr=list(map(int,input().split()))
    if arr[0]>50:
        print("A")
    elif arr[1]>50:
        print("B")
    elif arr[2]>50:
        print("C")
    else:
        print("NOTA")