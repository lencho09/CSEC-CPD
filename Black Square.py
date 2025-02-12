lst = [int(x) for x in input().split()]
n = input()
calories = 0
for i in n:
    if i == "1":
        calories += lst[0]
    elif i == "2":
        calories += lst[1]
    elif i == "3":
        calories += lst[2]
    else:
        calories += lst[3]

print(calories)
