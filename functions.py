FILEPATH = 'todos.txt'


def print_list(mylist):
    # mylist = [item.strip('\n') for item in mylist]
    enu = enumerate(mylist)
    for index, item in enu:
        item = item.strip('\n')
        item = item.title()
        print(f"{index + 1}-{item}")


def get_todos(filepath=FILEPATH):
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH
                ):
    with open(filepath,'w') as file:
        file.writelines(todos_arg)
