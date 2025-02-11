limack, bob = map(int, input().split())

count = 0
while bob >= limack:
    bob *= 2
    limack *= 3
    count += 1

print(count)
