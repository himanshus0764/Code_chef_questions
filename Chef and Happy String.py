lolmf=['a','e','i','o','u']
count=0
for i in range(int(input())):
    s=input()
    if s ==lolmf[i]:
        count+=1
    if count>=2:
        print("happy")
    else:
        print("sad")

    