n=int(input())
s=list(map(int,input().split()))
res=None
for i in s:
    if(i%2==0):
        res=i
print(res)
        