print("===== Creating a List =====")
lst = [10, 20, 30, 40, 20]
print("Original List:", lst)

print("\n===== Accessing Elements =====")
print("First Element:", lst[0])
print("Last Element:", lst[-1])
print("THIRD Element:", lst[3])

print("\n===== Slicing =====")
print("lst[1:4] =", lst[1:4])
print("lst[:3] =", lst[:3])
print("lst[2:] =", lst[2:])
print("Reversed using slicing:", lst[::-1])
print("Reversed  slicing operation manipulation:", lst[4:2:-1])

print("\n===== Updating Element =====")
lst[1] = 25
print(lst)

print("\n===== append() =====")
lst.append(50)
print(lst)

print("\n===== extend() =====")
lst.extend([60, 70])
print(lst)

print("\n===== insert() =====")
lst.insert(2, 99)
print(lst)

print("\n===== remove() =====")
lst.remove(20)          # Removes first occurrence of 20
print(lst)

print("\n===== pop() =====")
removed = lst.pop()
print("Removed:", removed)
print(lst)

removed = lst.pop(2)
print("Removed at index 2:", removed)
print(lst)

print("\n===== index() =====")
print("Index of 30:", lst.index(30))

print("\n===== count() =====")
print("Count of 20:", lst.count(20))

print("\n===== Membership =====")
print("30 in list?", 30 in lst)
print("100 not in list?", 100 not in lst)

print("\n===== Length =====")
print("Length:", len(lst))

print("\n===== Sum, Max, Min =====")
print("Sum:", sum(lst))
print("Maximum:", max(lst))
print("Minimum:", min(lst))

print("\n===== Sorting =====")
temp = lst.copy()
temp.sort()
print("Ascending:", temp)

temp.sort(reverse=True)
print("Descending:", temp)

print("\n===== sorted() =====")
print(sorted(lst))
print(sorted(lst,reverse=True))

print("\n===== reverse() =====")
temp = lst.copy()
temp.reverse()
print(temp)

print("\n===== copy() =====")
copy_list = lst.copy()
print("Copied List:", copy_list)

print("\n===== Concatenation =====")
list2 = [100, 200]
print(lst + list2)

print("\n===== Repetition =====")
print(list2 * 3)

print("\n===== Iteration =====")
for item in lst:
    print(item, end=" ")
print()

print("\n===== enumerate() =====")
for index, value in enumerate(lst):
    print(index, "->", value)

print("\n===== Nested List =====")
nested = [[1, 2], [3, 4]]
print(nested)
print("nested[1][0] =", nested[1][0])

print("\n===== List Comprehension =====")
square = [x*x for x in range(1, 6)]
print(square)

even = [x for x in range(1, 11) if x % 2 == 0]
print(even)



print("\n===== del =====")
temp = lst.copy()
del temp[1]
print(temp)

print("\n===== clear() =====")
temp.clear()
print(temp)

print("\n===== Assignment vs Copy =====")
a = [1, 2, 3]
b = a
c = a.copy()

b.append(4)

print("a =", a)
print("b =", b)
print("c =", c)

print("\n===== End of Demonstration =====")


