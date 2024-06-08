for _ in range(int(input())):
    a, b = map(int, input().split())
    ls = list(map(int, input().split()))
    x = 1

    coun = 0
    for i in range(a - 1):  
        x = ls[i]-b
        x += ls[i+1]
    if b>x:
        coun += 1
        print("NO " + str(coun))
        break
    else:
        print("YES")