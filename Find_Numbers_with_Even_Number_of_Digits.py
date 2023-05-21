n=int(input())
a=list(map(int,input().split()))
cnt=0
for i in a:
    #x=str(i)
    r=len(str(i))
    if(r%2==0):
        cnt=cnt+1
print(cnt)