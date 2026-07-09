# def write():
#     with open ("../files/student.txt","w") as file:
#         file.write("NAMIT\t19\tCSE\n")
# write()


import os


def write():
    base_dir = os.path.dirname(__file__)
    path = os.path.join(base_dir, "..", "files", "student.txt")

    with open(path, "w") as file:
        file.write("NAMIT\tRATHI\t19\tCSE\n"
                   "NISHA\tRATHI\t33\tCSE\n"
                   "NITIN\tRATHI\t33\tME")


def read():
    base_dir = os.path.dirname(__file__)
    path = os.path.join(base_dir, "..", "files", "student.txt")

    with open(path, "r") as file:
        # text = file.read()
        # words=text.split()
        # print(text)
        # print(words)

        # first_ten=file.read(10)
        # print(f"THE FIRST TEN CHARACTERS ARE {first_ten}")

        # print(file.readline())
        # print(file.readline())
        # print(file.readline())

        # for line in file.readlines():
        #     print(line,end="")

        # count=0
        # for ch in file.read():
        #     count+=1
        # print(f"THE NUMBER OF CHARACTERS ARE {count}")

        # count = 0
        # for ch in file.read():
        #     if ch=="\t" or ch=="\n":
        #         count += 1
        # print(f"THE NUMBER OF WORDS ARE {count+1}")

        # count = 0
        # for ch in file.read():
        #     if ch=="\n":
        #         count += 1
        # print(f"THE NUMBER OF LINES ARE {count+1}")

        print(file.readlines())




write()
read()
