n=int(input())
a=list(map(int,input().split()))
cnt=0
for i in a:
    if(i%2==0):
        cnt=cnt+1
if(cnt==n):
    print("True")
else:
    print("False")