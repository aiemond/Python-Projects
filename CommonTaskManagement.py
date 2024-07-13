#The Task Management App is a command-line interface (CLI) Python 
# application that allows users to manage tasks effectively.
#  Users can add, update, delete, and view tasks using simple text-based commands. 
# The app operates in a continuous loop, processing user commands until the user exits.


def initialize_tasks():
    tasks = []
    total_task = int(input("Enter how many tasks you want to add: "))
    for i in range(1, total_task + 1):
        task_name = input(f"Enter task {i}: ")
        tasks.append(task_name)
    return tasks

def add_task(tasks):
    new_task = input("Enter the task you want to add: ")
    tasks.append(new_task)
    print(f"Task '{new_task}' has been successfully added.")
    return tasks

def update_task(tasks):
    old_task = input("Enter the task name you want to update: ")
    if old_task in tasks:
        new_task = input("Enter the new task: ")
        index = tasks.index(old_task)
        tasks[index] = new_task
        print(f"Updated task '{old_task}' to '{new_task}'.")
    else:
        print("Task not found.")
    return tasks

def delete_task(tasks):
    task_to_delete = input("Enter the task name you want to delete: ")
    if task_to_delete in tasks:
        tasks.remove(task_to_delete)
        print(f"Task '{task_to_delete}' has been deleted.")
    else:
        print("Task not found.")
    return tasks

def view_tasks(tasks):
    print("Today's tasks are:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

def task_management():
    print("----WELCOME TO THE TASK MANAGEMENT APP----")
    tasks = initialize_tasks()
    view_tasks(tasks)
    
    while True:
        try:
            operation = int(input("\nEnter an operation: \n1 - Add\n2 - Update\n3 - Delete\n4 - View\n5 - Exit\n"))
            if operation == 1:
                tasks = add_task(tasks)
            elif operation == 2:
                tasks = update_task(tasks)
            elif operation == 3:
                tasks = delete_task(tasks)
            elif operation == 4:
                view_tasks(tasks)
            elif operation == 5:
                print("Closing the program....")
                break
            else:
                print("Invalid input. Please enter a number from 1 to 5.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

task_management()
