with open('data.txt', encoding='utf-8') as file_obj:

    contents = file_obj.read()
    print(contents.rstrip())
