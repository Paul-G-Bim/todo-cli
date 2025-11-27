from functions import get_todos, store_todos

while True:
    user_action = input("Type add, show, edit, delete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:] + '\n'
        todos = get_todos()
        todos.append(todo)
        store_todos(todos)

    elif user_action.startswith('show'):
        todos = get_todos()
        [print(f"{index + 1}- {todo.strip('\n')}") for index, todo in enumerate(todos)]

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:]) - 1
            todos = get_todos()
            todos[number] = input("Edit the todo: ") + '\n'
            store_todos(todos)
        except ValueError:
            print("Invalid command, only numbers are allowed")
        except IndexError:
            print("Invalid command, number is not in the list")

    elif user_action.startswith('delete'):
        try:
            number = int(user_action[7:]) - 1
            todos = get_todos()
            todo_to_delete = todos[number].strip('\n')
            todos.pop(number)
            store_todos(todos)
            print(f"{todo_to_delete} was successfully deleted")
        except ValueError:
            print("Invalid command, only numbers are allowed")
        except IndexError:
            print("Invalid command, number is not in the list")

    elif user_action.startswith('exit'):
        break

    else:
        print("Invalid command")

print('Bye!')