note_list = [500, 200, 100, 50, 20, 10, 5, 2, 1]

note_dict = {}

amount = int(input("ENTER THE AMOUNT: "))

for note in note_list:
    note_count = amount // note

    if note_count > 0:
        note_dict[note] = note_count

    amount = amount % note

print("\nMinimum Notes Required:")

for key, value in note_dict.items():
    print(f"{key} : {value}")