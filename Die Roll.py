lst = [int(x) for x in input().split()]

numerator = 7 - max(lst)
denominator = 6
for i in range(1, 7):
    if numerator % i == 0 and denominator % i == 0:
        numerator /= i
        denominator /= i

print(f"{int(numerator)}/{int(denominator)}")
