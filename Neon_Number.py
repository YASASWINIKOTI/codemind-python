def sum(a):
    s=0
    while(a>0):
        r=a%10
        s=s+r
        a=a//10
    return s
n=int(input())
sqr=n**2
if(sum(sqr)==n): 
    print("Neon Number")
else:
    print("Not Neon Number")