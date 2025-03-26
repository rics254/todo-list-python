def add_task(task):
    with open("tasks.text", "a") as file:
        file.write(task + "\n")
        print(f"Task '{task}' added successfully!")

def view_tasks():
    try:

        with open("tasks.txt", "r") as file:
         task = file.readlines()
         if not tasks:
             print("No tasks found!")
         else:
             print("\nYour To-Do List:")
             for i, task in enumerate(tasks, start=1):
                  print(f"{i}.{task.strip}")
    except FileNotFoundError:
        print("No tasks found! Start by adding a task") 

    def remove_task(task_number):
        try:
            with open("tasks.txt", "r") as file:
                tasks = file.readlines()

            if 0 <task_number <= len(tasks):
                removed_task = tasks.pop(task_number - 1)
                with open("tasks.txt", "w") as file:
                    file.writelines(tasks)
                print(f"Removed task: {removed_task.strip()}")
            else:
                print("Invalid task number!")
        except FileNotFoundError:
            print("No tasks file found!")
    def main():
        while True:
            print("\nTo-Do List Menu:")
            print("1. Add Task")
            print("2. View Tasks")
            print("3. Remove Task")
            print("4. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                task = input("Enter task: ")
                add_task(task)
            elif choice == "2":
                view_tasks()
            elif choice == "3":
                task_number = int(input("Enter the task number to remove: "))
                remove_task(task_number)
            elif choice == "4":
                break
            else:
                print("Invalid choice. Try again!")

    if __name__ == "__main__":
        main()
