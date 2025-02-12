n = int(input())
birds = [int(x) for x in input().split()]
m = int(input())
shoots = [[int(x) for x in input().split()] for i in range(m)]

for i in range(m):
    if n != 1:
        wire = shoots[i][0]
        target = shoots[i][1]

        if wire != 1 and wire != n:
            birds[wire - 2] += target - 1
            birds[wire] += birds[wire - 1] - target
        elif wire == 1:
            birds[1] += birds[0] - target
        else:
            birds[n - 2] += target - 1

        birds[wire - 1] = 0
    else:
        birds[0] = 0

for i in birds:
    print(i)
