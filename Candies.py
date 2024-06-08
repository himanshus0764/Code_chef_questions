for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    count=0
    c=0
    for j in l:
        k=l.count(j)
        if k>=3:
            c+=1
    if c>1:
        print("NO")
    else:
        print("yes")