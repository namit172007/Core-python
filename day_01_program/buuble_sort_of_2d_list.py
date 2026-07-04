list_of_list = [
    [1, 'abc', 1000],
    [2, 'xyz', 1100],
    [1, 'pqr', 500],
    [1, 'klm', 700]
]

n = len(list_of_list)

for i in range(n - 1):
    for j in range(n - 1 - i):
        if list_of_list[j][2] > list_of_list[j + 1][2]:
            list_of_list[j], list_of_list[j + 1] = list_of_list[j + 1], list_of_list[j]

print("Sorted List:")
for row in list_of_list:
    print(row)