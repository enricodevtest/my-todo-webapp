# a Function that reads the todo list from a file.
def readTodos(fn):
    with open(fn, "r") as myfile:
        todoList = myfile.readlines()
    return sorted(todoList)
# End of readTodos

def writeTodos(fn, tdl):
    with open(fn, "w") as myfile:
        myfile.writelines(sorted(tdl))
    return None
# End of writeTodos