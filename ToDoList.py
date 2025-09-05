print("-------------To Do List Menu--------------")
print("1. Display To Do List")
print("2. Add a task")
print("3. Task is done")
print("4. Exit")
print("-------------------------------------")
task=[]
def menu(task):
    choice=input("Choose a number from the menu: ")
    match choice:
        case "1":
            print("Option 1 selected")
            print("To Do List:")
            for i in task:
                print(i)
            menu(task)
        case "2":
            print("Option 2 selected")
            x=input("Add your new task: ")
            task.append(x)
            print("Task was added")
            menu(task)
        case "3":
            print("Option 3 selected")
            x=int(input("Add the number of task you want to take off: "))
            task.pop(x-1)
            print("Task was deleted")
            menu(task)
        case "4":
            print("Goodbye!")
        case _:
            print("Invalid choice")
            menu(task)

menu(task)

        
