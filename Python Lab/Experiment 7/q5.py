class FileEmptyError(Exception):
    pass

try:
    f = open("data.txt", "r")
    content = f.read()
    f.close()

    if content == "":
        raise FileEmptyError("File is empty")

    print(content)

except FileNotFoundError:
    print("File not found")

except FileEmptyError as e:
    print(e)