for i in range(int(input())):
    st=[]
    a,b=map(int,input().split())
    for i in range(a):
        w,h,p=map(int,input().split())
        if p<=b:
            st.append(w*h)
    if len(st)==0:
        print("no tablet")
    else:
        print(max(st))
"""problem number 1037 bough a new table """