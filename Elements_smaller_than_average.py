n=int(input())
a=list(map(int,input().split()))
s=0
cnt=0
for i in a:
    s=s+i
avg=s//n
for i in a:
    if(i<=avg):
        cnt=cnt+1
print(cnt)
        