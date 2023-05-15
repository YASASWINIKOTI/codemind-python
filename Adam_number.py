n=int(input())
s1=n**2
s=0
sum2=0
while(n>0):
    r=n%10
    s=s*10+r
    n=n//10
s2=s**2
while(s2>0):
    rev=s2%10
    sum2=sum2*10+rev
    s2=s2//10
if(sum2==s1):
    print("True")
else:
    print("False")
    