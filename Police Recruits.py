n = int(input())

lst = [int(x) for x in input().split()]
police = 0
crime = 0
for i in range(n):
    if lst[i] > 0:
        police += lst[i]
    else:
        if police <= 0:
            crime += 1
        else:
            police -= 1

print(crime)
