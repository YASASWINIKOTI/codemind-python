def sum(n):
    s=0
    while(n>0):
        r=n%10
        s=s+r
        n=n//10
    return s
def pro(n):
    p=1
    while(n>0):
        r=n%10
        p=p*r
        n=n//10
    return p
a=int(input())
if (sum(a)==pro(a)):
    print("Spy Number")
else:
    print("Not Spy Number")

        
    

    