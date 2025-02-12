s = input()
t = input()
x = 0

count = 1
current_stone = s[x] 

for i in range(len(t)):
    current_inst = t[i]

    if current_inst == current_stone:
        x += 1
        current_stone = s[x]
        count += 1
        
print(count)
