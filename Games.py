n = int(input())
lst = [[int(x) for x in input().split()] for i in range(n)]
change = 0
point = 0
for i in range(n):
    for i in range(n):
        if lst[point][0] == lst[i][1]:
            change += 1
    point += 1

print(change)
