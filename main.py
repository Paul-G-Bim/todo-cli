while True:
    user_action = input("Type add, show, edit, delete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:] + '\n'
        with open("todos.txt", "r") as file:
            todos = file.readlines()
        todos.append(todo)
        with open("todos.txt", "w") as file:
            file.writelines(todos)

    elif user_action.startswith('show'):
        with open("todos.txt", "r") as file:
            todos = file.readlines()
        [print(f"{index + 1}- {todo.strip('\n')}") for index, todo in enumerate(todos)]

    elif user_action.startswith('edit'):
        number = int(user_action[5:]) - 1
        with open("todos.txt", "r") as file:
            todos = file.readlines()
        todos[number] = input("Edit the todo: ") + '\n'
        with open("todos.txt", "w") as file:
            file.writelines(todos)

    elif user_action.startswith('delete'):
        number = int(user_action[7:]) - 1
        with open("todos.txt", "r") as file:
            todos = file.readlines()
        todo_to_delete = todos[number].strip('\n')
        todos.pop(number)
        with open("todos.txt", "w") as file:
            file.writelines(todos)
        print(f"{todo_to_delete} was successfully deleted")

    elif user_action.startswith('exit'):
        break

    else:
        print("Invalid command")

print('Bye!')