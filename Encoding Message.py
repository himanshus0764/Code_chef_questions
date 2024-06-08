num = int(input())

for _ in range(num):
    length = int(input())
    string = input()
    lst = list(string)
    
    for y in range(0, length - 1, 2): 
        lst[y], lst[y + 1] = lst[y + 1], lst[y]
    
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    lst = [alphabet[25 - alphabet.index(ch)] for ch in lst]
    
    string = ''.join(lst)
    print(string)
