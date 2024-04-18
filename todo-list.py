todos = []
id_counter = 1

def add_todo():
    global id_counter
    task = input("Enter your task/work: ")
    date = input("Enter the date: ")
    priority = input("Enter priority level (high, medium, low): ").lower()
    todo = {"id": id_counter, "task": task, "date": date, "priority": priority}
    todos.append(todo)
    print("Task added successfully. ID:", id_counter)
    id_counter += 1

def delete_todo():
    task_id = int(input("Enter the ID of the task to be deleted: "))
    for todo in todos:
        if todo["id"] == task_id:
            todos.remove(todo)
            print("Task with ID {} deleted successfully.".format(task_id))
            return
    print("Task with ID {} not found.".format(task_id))

def update_todo():
    task_id = int(input("Enter the ID of the task to be updated: "))
    for todo in todos:
        if todo["id"] == task_id:
            print("Task:", todo["task"])
            print("Date:", todo["date"])
            print("Priority:", todo["priority"])
            update_choice = input("What would you like to update? (task/date/priority/all): ").lower()
            if update_choice == "task":
                new_task = input("Enter the new task: ")
                todo["task"] = new_task
            elif update_choice == "date":
                new_date = input("Enter the new date: ")
                todo["date"] = new_date
            elif update_choice == "priority":
                new_priority = input("Enter the new priority level (high, medium, low): ").lower()
                todo["priority"] = new_priority
            elif update_choice == "all":
                new_task = input("Enter the new task: ")
                new_date = input("Enter the new date: ")
                new_priority = input("Enter the new priority level (high, medium, low): ").lower()
                todo["task"] = new_task
                todo["date"] = new_date
                todo["priority"] = new_priority
            else:
                print("Invalid choice.")
                return
            print("Task with ID {} updated successfully.".format(task_id))
            return
    print("Task with ID {} not found.".format(task_id))

def show_todos():
    if todos:
        for todo in todos:
            print("ID: {}, Task: {}, Date: {}, Priority: {}".format(todo["id"], todo["task"], todo["date"], todo["priority"]))
    else:
        print("No tasks in the to-do list.")

def todolist():
    print("Press 1 to add Todo")
    print("Press 2 to delete Todo")
    print("Press 3 to update Todo")
    print("Press 4 to show all Todos")
    print("Press 5 to exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_todo()
    elif choice == "2":
        delete_todo()
    elif choice == "3":
        update_todo()
    elif choice == "4":
        show_todos()
    elif choice == "5":
        print("Exiting...")
        return
    else:
        print("Invalid choice")
    todolist()

todolist()
