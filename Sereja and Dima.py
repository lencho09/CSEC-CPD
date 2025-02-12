n = int(input())
 
lst = [int(x) for x in input().split()]
 
seraja = 0
dima = 0
turn = 1
 
for i in range(n):
    if turn == 1:
        if lst[0] > lst[-1]:
            seraja += lst.pop(0)
        else:
            seraja += lst.pop()
        turn = 1 - turn
    else:
        if lst[0] > lst[-1]:
            dima += lst.pop(0)
        else:
            dima += lst.pop()
        turn = 1 - turn
 
print(seraja,  end=' ')
print(dima)
