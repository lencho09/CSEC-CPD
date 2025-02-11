matrix = [[int(x) for x in input().split()] for i in range(5)]


def find_one(mat):
    for i in range(5):  
        for j in range(5):  
            if matrix[i][j] == 1:  
                return (i, j)


first, second = find_one(matrix)
count = 0          

count += abs(first - 2)
count += abs(second - 2)

print(count)



