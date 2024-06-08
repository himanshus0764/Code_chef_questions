c= []
for i in range(int(input())):
    a,b=map(int,input().split())
    withdraw_amount = list(map(int, input().split()))
    v=0
    for i in range(a):
        b-=withdraw_amount[i]
        if b<0:
            c.append(0)
            print(withdraw_amount[i-1],withdraw_amount[i])
        print(b)