a=int(input())
n=0
m=0
t=0
for i in range(a):
    if n==0:
        print(n)
        n+=1
    else:
        print(n)
        t=n
        n+=m
        m=t
