def read_file(filename=""):
    with open('my_file_0.txt', "r", encoding="utf-8") as file:
        print(f"{file.read()}", end ="")
