import math

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

for i in range(int(input())):
    x,y=map(int,input().split())
    print(gcd(x, y))
