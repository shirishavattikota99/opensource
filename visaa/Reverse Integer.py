n = int(input())
reverse = int(str(abs(n))[::-1]) * (-1 if n < 0 else 1)

if -(2**31) <= reverse <= 2**31 - 1:
    print(reverse)
else:
    print("0")
