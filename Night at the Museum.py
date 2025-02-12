n = input() 
step = 0
pointer = ord("a")

for i in n:
    check = abs(ord(i) - pointer)
    if check < 13:
        step += check
    else:
        step += 26 - check
        
    pointer = ord(i)

print(step)
