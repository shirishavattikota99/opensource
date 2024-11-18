X,N=map(int,input().split())
T=X*100
l=N-T
res=l/100
if res>int(res):
    print(int(res)+1)
else:
    print(int(res))
