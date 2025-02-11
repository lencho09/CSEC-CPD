str1 = input()
dict = {}

for i in str1:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1

total = 0

for keys, values in dict.items():
    total += 1

if total % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")

