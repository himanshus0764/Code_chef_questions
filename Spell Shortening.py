for i in range(int(input)):
    n=int(input())
    s=list(input())
    f=1
    for i in range(n-1):
        if s[i]>s[i+1]:
            s[i]=''
            f=0
            break
    if f:s[-1]=''
    print(''.join(s))