def isprime(a):
    s=0
    for i in range(1,a+1):
        if(a%i==0):
            s=s+1
    return s
    
n=int(input())
a=list(map(int,input().split()))
npro=1
pro=1
for i in a:
    if(isprime(i)==2):
        pro=pro*i
    else:
        npro=npro*i
print(npro-pro)
