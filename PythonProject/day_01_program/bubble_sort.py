numbers = [5, 3, 8, 4, 2]

n = len(numbers)

for i in range(n - 1):    # the count of how many time the bracket shifts
    for j in range(n - 1 - i):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print(numbers)