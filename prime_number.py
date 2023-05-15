def isprime(a):
    s=0
    for i in range(1,a+1):
        if(a%i==0):
            s=s+1
    return s
n=int(input())
r=isprime(n)
if(r==2):
    print("prime")
else:
    print("not a prime")