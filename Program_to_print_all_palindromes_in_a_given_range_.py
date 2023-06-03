a=int(input())
b=int(input())
lst=[]
for i in range(a,b+1):
    k=i
    #print(k)
    s=0
    while(i!=0):
        r=i%10
        s=s*10+r
        i=i//10
    if(k==s):
        lst.append(k)
print(*lst)