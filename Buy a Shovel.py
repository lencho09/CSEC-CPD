lst = [int(x) for x in input().split()]

i = 1
while True:
    if (lst[0] * i) % 10 == 0:
        break
    if (lst[0] * i - lst[1]) % 10 == 0:
        break
    i += 1 

print(i)
