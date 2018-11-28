import os

user_input = input('Введите фразу, содержащуюся в искомом файле: ')

migrations = 'Migrations'

current_dir = os.path.dirname(os.path.abspath(__file__))

migrations_dir = os.path.join(current_dir, migrations)
#
# print(migrations_dir)

files_list = os.listdir(migrations_dir)


new_list = list()


def find_sql():
    for names in files_list:
        if '.sql' in names:
            new_list.append(names)
    # print('New list {}\n Всего файлов: {}'.format(new_list, len(new_list)))

# find_sql() # Составили список файлов sql

def search_sql(user_input):
    input_list = list()
    for file in new_list:
        file_path = os.path.join(current_dir, migrations, file)
        with open (file_path, 'r') as f:
            a = f.read()
            if user_input in a:
                input_list.append(file)
    print('С фразой {}, нашлось {} файлов.'.format(user_input, len(input_list)))

# search_sql(user_input) # Ищем фразы в файлах и добавляем их в список, а также учитываем их кол-во

find_sql()
while True:
    search_sql(user_input)
    if len(input_list) == 0:
        exit()
       
