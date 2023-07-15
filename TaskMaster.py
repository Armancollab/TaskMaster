import sys

tasks = []

def save_tasks():
    with open("todo.txt", "w") as file:
        for task in tasks:
            file.write(f"{task}\n")

def load_tasks():
    try:
        with open("todo.txt", "r") as file:
            for line in file:
                task = line.strip()
                tasks.append(task)
    except FileNotFoundError:
        pass

def show_menu():
    print("\n===== To-Do List Menu =====")
    print("1. Add a Task")
    print("2. View Tasks")
    print("3. Delete a Task")
    print("4. Exit")
    print("===========================")

def add_task():
    title = input("Enter the title of the task: ")
    tasks.append(title)
    save_tasks()
    print(f"Task '{title}' added successfully!")

def view_tasks():
    if tasks:
        print("\n===== Current Tasks =====")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
        print("=========================")
    else:
        print("\nNo tasks found!")

def delete_task():
    if not tasks:
        print("\nNo tasks found!")
        return
    
    view_tasks()
    index = input("Enter the index of the task to delete: ")
    try:
        index = int(index)
        if index < 1 or index > len(tasks):
            print("Invalid index!")
        else:
            deleted_task = tasks.pop(index - 1)
            save_tasks()
            print(f"Task '{deleted_task}' deleted successfully!")
    except ValueError:
        print("Invalid index!")

def exit_program():
    save_tasks()
    print("Exiting the program. Goodbye!")
    sys.exit()

def main():
    load_tasks()
    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ")
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            exit_program()
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
