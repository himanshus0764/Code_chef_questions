t = int(input("Enter the number of test cases: "))
for _ in range(t):
    a, b = map(int, input().split())
    
    if (a % 2 == 0 and b % 2 == 0 and abs(a - b) == 2) or \
       (a % 2 != 0 and b % 2 != 0 and abs(a - b) == 2) or \
       (max(a, b) % 2 == 0 and abs(a - b) == 1):
        print("YES")
    else:
        print("NO")
