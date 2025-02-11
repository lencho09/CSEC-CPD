n = input()

count = 0

for i in n:
    if ord(i) in range(65,91):
        count += 1
    else:
        count -= 1
if count > 0:
    print(n.upper())
else:
    print(n.lower())
