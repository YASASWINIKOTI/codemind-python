n=int(input())
s=list(map(int,input().split()))
sum=0
cnt=0
for i in s:
    sum=sum+i
avg=sum//n
for i in s:
    if(i>=avg):
        cnt=cnt+1
print(cnt)