x=int(input())
y=int(input())
for a in range(1,min(y,x//20)+1):
    for b in range(0,min(y,x//10)+1):
        for c in range(0,min(y,x//5)+1):
            if a*20+b*10+c*5==x:
                if a+b+c==y:
                    print(a,b,c)
