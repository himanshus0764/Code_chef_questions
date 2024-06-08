for i in range(int(input())):
    st = input()
    vowels = ['A', 'E', 'I', 'O', 'U']
    if all(st[j] in vowels for j in [1, 3, 5]) and all(st[k] not in vowels for k in [0, 2, 4, 6, 7]):
        print("YES")
    else:
        print("NO")
