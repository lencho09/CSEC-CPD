n, h = [int(x) for x in input().split()]

lst = [int(x) for x in input().split()]

width = 0 

for i in lst:
    if i > h:
        width += 2
    else:
        width += 1
print(width)
