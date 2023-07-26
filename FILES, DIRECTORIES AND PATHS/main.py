with open("FILES, DIRECTORIES AND PATHS\\text_file.txt") as file:
    contents = file.read()
    print(contents)

with open("FILES, DIRECTORIES AND PATHS\\text_file.txt", mode="a") as file:
    file.write("\nNew text.")