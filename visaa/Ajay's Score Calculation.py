T=int(input())
for i in range(T):
    X,N=map(int,input().split())
    
    score=X//10
    total=score*N
    
    print(total)
