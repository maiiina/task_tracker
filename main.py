import json
import os

filename = "my_tasks.json"

# load existing tasks
def load_task():
    if os.path.exists(filename):
        try:
            with open(filename, "r") as file:
                return json.load(file)
            print(f"Loaded {len(my_tasks)} existing tasks.")
        except:
            print("Could not load existing tasks, starting fresh.")
        return[]

# Save back to file
def save_task(tasks):
    try:
        with open(filename, "w") as file:
            json.dump(tasks, file, indent=4)
        print(f"List successfully saved to {filename} ({len(tasks)} tasks total)")
    except Exception as e:
        print(f"Error saving file: {e}")

# View tasks
def view_task(task):
    print("Current tasks:")
    if not task:
        print("No tasks yet")
    else:
        for i, task in enumerate(task, start=1):
            print(f"  {i}. {task}")
        print()   

# Add new tasks
def add_task(task):
    new_task = input("Enter new task: ").strip()
    if task:
        task.append(new_task)
        print(f"{new_task} added")
    else:
        print("Empty! Task not added")
    return task

# Update tasks
def update_task(task):
    view_task(task)
    if not task:
        return task
    
    try:
        index = int(input("Enter task number to update "))-1
        if 0<= index <= len(task):
            new_task = input(f"{task[index]} updated to: ").strip()
            if new_task:
                old = task[index]
                task[index] = new_task
                print(f"{old} updated to {new_task}")
            else:
                print("Empty! Task not changed")
        else:
            print("invalid task number")
    except ValueError:
        print("Enter valid number")
    return task

# Delete tasks
def delete_task(task):
    if not task:
        return task
    
    try:
        index = int(input("enter task number to delete: "))-1
        if 0 <= index <= len(task):
            removed = task.pop(index)
            print(f"{removed} deleted")
        else:
            print("invalid task number")
    except ValueError:
        print("enter valid number")
    return task

#main (UI)
def main():
    tasks = load_task()

    while True:
        print("---MENU---")
        print("1. view task")
        print("2. add task")
        print("3. update task")
        print("4. delete task")
        print("5. exit")

        choice = input("choose 1-5: ").strip()

        if choice == "1":
            view_task(tasks)
        elif choice == "2":
            tasks = add_task(tasks)
            save_task(tasks)
        elif choice == "3":
            tasks = update_task(tasks)
            save_task(tasks)
        elif choice == "4":
            view_task(tasks)
            tasks = delete_task(tasks)
            save_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("invalid choice. Try again!")

#run
if __name__ == "__main__":
    main()
