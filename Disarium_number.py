def length(n):
    l=0
    while(n!=0):
        l=l+1
        n=n//10
    return l
n=int(input())
s=0
k=n
len=length(n)
while(n!=0):
    r=n%10
    s=s+int(r**len)
    n=n//10
    len=len-1
if(s==k):
    print("True")
else:
    print("False")
