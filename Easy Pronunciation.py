t = int(input())

for _ in range(t):
    n = int(input())
    s = input().lower()

    consecutive_consonants = 0
    result = "YES"

    for char in s:
        if char.isalpha() and char.lower() not in "aeiou":
            consecutive_consonants += 1
            if consecutive_consonants >= 4:
                result = "NO"
                break
        else:
            consecutive_consonants = 0

    print(result)
