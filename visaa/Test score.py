n, x, y = map(int, input().split())
if y % x == 0 and y // x <= n:
    print("YES")
else:
    print("NO")
