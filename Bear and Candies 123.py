for _ in range(int(input())):
    a, b = map(int, input().split())
    for i in range(1, 1000):
        if i % 2 == 1:
            a -= i
            if a < 0:
                print("Bob")
                break
        else:
            b -= i
            if b < 0:
                print("Limak")
                break
