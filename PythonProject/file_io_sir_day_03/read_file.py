def readFile():
    file = open("../files/hii.txt", "r")
    text = file.read()  # Read all data
    print(text)
    file.close()  # Close a file


readFile()