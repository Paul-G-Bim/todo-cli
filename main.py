while True:
    user_action = input("Type add, show, edit, delete or exit: ")
    user_action = user_action.strip().casefold()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + '\n'
            with open("todos.txt", "r") as file:
                todos = file.readlines()
            todos.append(todo)
            with open("todos.txt", "w") as file:
                file.writelines(todos)

        case 'show' | 'display':
            with open("todos.txt", "r") as file:
                todos = file.readlines()
            [print(f"{index + 1}- {todo.strip('\n')}") for index, todo in enumerate(todos)]

        case 'edit':
            number = int(input("Enter the number of the todo you want to edit: ")) - 1
            with open("todos.txt", "r") as file:
                todos = file.readlines()
            todos[number] = input("Edit the todo: ") + '\n'
            with open("todos.txt", "w") as file:
                file.writelines(todos)

        case 'delete':
            number = int(input("Enter the number of the todo you want to delete: ")) - 1
            with open("todos.txt", "r") as file:
                todos = file.readlines()
            todo_to_delete = todos[number].strip('\n')
            todos.pop(number)
            with open("todos.txt", "w") as file:
                file.writelines(todos)
            print(f"{todo_to_delete} was successfully deleted")

        case 'exit':
            break

        case _:
            print("Incorrect input")

print('Bye!')