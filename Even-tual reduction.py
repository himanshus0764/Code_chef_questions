for i in range(int(input())):
    a=int(input())
    element=input()
    c=0
    for i in element:
        c=element.count(i)
        if c%2==0:
            c=1
        else:
            c=0
            break
    if c!=0:
        print("YES")
    else:print("NO")