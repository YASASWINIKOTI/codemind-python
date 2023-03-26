s=int(input())
h=s//3600
m=(s-(h*3600))//60
ss=s-(m*60)-(h*3600)
print("H:M:S-%d:%d:%d"%(h,m,ss))