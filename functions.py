def get_todos(file_path='todos.txt'):
    """Returns a list of todos from the file"""
    with open(file_path, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def store_todos(todos_local, file_path='todos.txt'):
    """Stores the todos in the file"""
    with open(file_path, "w") as file_local:
        file_local.writelines(todos_local)