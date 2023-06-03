n,k=map(int,input().split())
s=list(map(int,input().split()))
cnt=0
for i in s:
    l=int(i)
    if(l%k!=0):
        cnt=cnt+1
print(cnt)