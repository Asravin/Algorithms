numbers = [2, 5, 13, 7, 6, 4]
size = 6 
index = 0
max_idx = 0
maxx = numbers[max_idx]
while index < size:
    if numbers[index] > maxx:
        max_idx = index
        maxx = numbers[index]
    index += 1
numbers[max_idx] = numbers[size - 1]
numbers[size - 1] = maxx
print(numbers)