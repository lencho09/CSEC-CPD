n = int(input())

lst = [input() for i in range(n)]
count = 1

for i in range(n - 1):
    if lst[i][-1] == lst[i + 1][0]:
        count += 1

print(count)
