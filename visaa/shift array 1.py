n=int(input())
arr=list(map(int,input().split()))
rotation=arr[1:]+arr[:1]
print(*rotation)
