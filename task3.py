import os
def readfile(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        file_content = f.read()
        return file_content
def count_file_strings(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        file_content = f.read()
        count_strings = file_content.count('\n') + 1
        return count_strings
def task3(dir_path):
    total_list = os.listdir(dir_path)
    cwd = os.getcwd()
    os.chdir(dir_path)
    total_list.sort(key=count_file_strings)
    for file in total_list:
        print(file)
        print(count_file_strings(file), 'строк(а/и)')
        print(readfile(file),'\n')
    os.chdir(cwd)
    return

# print(task3('sorted'))
task3('sorted')