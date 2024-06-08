for _ in range(int(input())):
    x, h = map(int, input().split())
    for i in range(1000):
        if h <= 0:
            print(i)
            break
        h -= x // 2 if i < 5 else x
