n=int(input())
a=list(map(int,input().split()))
s=0
cnt=0
for i in a:
    if(i%2==0):
        s=s+i
    elif(i%2!=0):
        cnt=cnt+i
dif=abs(cnt-s)
print("%d"%dif)
