from get_info import get_info

# записали введенные данные в файл в строку

def write_file_string():
    info = get_info()
    with open('Phonebook_string.csv', 'a', encoding='utf-8', newline='') as file:
        file.write(f'{info[0]},{info[1]},{info[2]},{info[3]}\n')
#write_file_string()

# записали введенные данные в файл в столбец

def write_file_column():
    info = get_info()
    with open('Phonebook_column.csv', 'a', encoding='utf-8', newline='') as file:
        file.write(f'{info[0]}\n{info[1]}\n{info[2]}\n{info[3]}\n\n')
#write_file_column()

# Считываем из файла построчно

def read_file_string():
    with open ('Phonebook_string.csv', 'r', encoding='utf-8', newline='') as file:
        list = file.read()
        some_list = list.replace(','," ")
        return(some_list)

# Считываем из файла столбцами  Зачем???

def read_file_column():
    with open ('Phonebook_column.csv', 'r', encoding='utf-8', newline='') as file:
        list = file.read()
        return(list)

# def print_file():
#     print ()

