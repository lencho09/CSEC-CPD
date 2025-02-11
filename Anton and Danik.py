n = int(input())

s = input()

win = 0
for i in s:
    if i == 'A':
        win += 1
    else:
        win -= 1

if win > 0:
    print("Anton")
elif win < 0:
    print("Danik")
else:
    print("Friendship")


