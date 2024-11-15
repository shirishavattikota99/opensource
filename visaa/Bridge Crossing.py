x,y,z=list(map(int,input().split()))

if y>=z:
    mangoes=0
else:
    mangoes=(z-y)//x
print(mangoes)
