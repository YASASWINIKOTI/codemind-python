n=int(input())
a=list(map(int,input().split()))
k=int(input())
s=0
for i in a:
    if(k==i):
        s=s+1
print(s)