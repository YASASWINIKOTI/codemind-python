n=int(input())
a=list(map(int,input().split()))
lste=[]
lsto=[]
for i in a:
    if(i%2==0):
        lste.append(i)
    else:
        lsto.append(i)
print(*lsto,*lste)      