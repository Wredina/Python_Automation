n = int(input())
max1 = 0
max2 = 0

for _ in range(n+1):
    a = int(input())
    if a > max1:
        max1 = a
    elif a > max2 < max1:
        max2 = a

print(max1, max2, sep='\n')
