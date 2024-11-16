n=int(input())
arr=list(map(int,input().split()))
def unique(arr):
    seen=set()
    result=[]
    for num in arr:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result
unique_elements=unique(arr)
print(*unique_elements)
