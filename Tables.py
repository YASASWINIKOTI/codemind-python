n,r=map(int,input().split())
pro=0
for i in range(1,r+1):
    if(i%2!=0):
        pro=n*i
        print("%d x %d = %d"%(n,i,pro))