n=int(input())
y=0
for i in range(n):
    if(i*i==n):
        y=i
if(y**2==n):
    print("True")
else:
    print("False")