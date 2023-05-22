n=int(input())
y=0
for i in range(1,n+1):
    if(i*i==n):
        y=i

if(y*y==n):
    print("True")
else:
    print("False")