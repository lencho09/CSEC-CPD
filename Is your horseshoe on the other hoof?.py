lst = [int(x) for x in input().split()]
double = []
for i in lst:
    if i not in double:
        double.append(i)

print(4 - len(double))
