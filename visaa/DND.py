n,m=map(int,input().split())
arr=list(map(int,input().split()))
sum1=0
sum2=0
for i in arr:
    if i%m==0:
        sum1+=i
    else:
        sum2+=i
print(sum1-sum2)
