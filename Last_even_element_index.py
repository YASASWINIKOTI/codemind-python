n=int(input())
s=list(map(int,input().split()))
res=None
for i in range(n):
    if(s[i]%2==0):
        res=i
print(res)