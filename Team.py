n = int(input())

lst = [[int(x) for x in input().split()] for i in range(n)]

count = 0
game = 0

for i in lst:
    for j in i:
        if j == 1:
            count += 1
    if count > 1:
        game += 1
    count = 0

print(game)
