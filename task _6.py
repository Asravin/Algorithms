numbers = [1, 8, 3, 8, 2, 6, 8, 8]
index = 0
size = 8
maximum = numbers[index]
count_maximal = 0
while index < size:
    if numbers[index] > maximum:
        maximum = numbers[index]
        count_maximal = 1
    else:
        if numbers[index] == maximum:
            count_maximal += 1
        index += 1
print(count_maximal)