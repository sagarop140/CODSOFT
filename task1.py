# To-Do List with Save Option

tasks = []  # List to store tasks

# Function to show the menu options
def show_menu():
    print("\n1. Add a Task")
    print("2. View Tasks")
    print("3. Remove a Task")
    print("4. Save and Exit")

# Function to add a task
def add_task():
    task = input("Enter the task: ")
    tasks.append(task)  # Add the task to the list
    print("Task added!")

# Function to view all tasks
def view_task():
    if len(tasks) == 0:
        print("No tasks yet.")
    else:
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task}")

# Function to remove a task
def remove_task():
    view_task()  # Show tasks before removing
    task_num = int(input("Enter task number to remove: "))
    if 0 < task_num <= len(tasks):
        tasks.pop(task_num - 1)  # Remove the task
        print("Task removed!")
    else:
        print("Invalid task number.")

# Function to save tasks to a file
def save_tasks_to_file():
    with open("tasks.txt", "w") as file:  # Open the file in write mode
        for task in tasks:
            file.write(task + "\n")  # Write each task to a new line
    print("Tasks saved to tasks.txt!")


def main():
    while True:
        show_menu()  # Display the menu
        choice = input("Choose an option: ")

        if choice == '1':
            add_task()  # Add a new task
        elif choice == '2':
            view_task()  # Show the task list
        elif choice == '3':
            remove_task()  # Remove a task
        elif choice == '4':
            save_tasks_to_file()  # Save the tasks before exiting
            print("Goodbye!")
            break  # Exit the program
        else:
            print("Invalid choice, try again.")

# Start the program
main()
