def get_todos(filepath="todos.txt"):
    with open(filepath, "r") as file:
        todos = file.readlines()
    return todos
