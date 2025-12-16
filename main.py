import json
import os

# adding and saving tasks
def add_task():

    filename = "my_tasks.json"
    my_tasks = []

    # Load existing tasks if file exists
    if os.path.exists(filename):
        try:
            with open(filename, "r") as file:
                my_tasks = json.load(file)
            print(f"Loaded {len(my_tasks)} existing tasks.")
        except:
            print("Could not load existing tasks, starting fresh.")

    # Add new task
    add_task = input("Enter task: ")
    my_tasks.append(add_task)

    # Save back to file
    try:
        with open(filename, "w") as file:
            json.dump(my_tasks, file, indent=4)
        print(f"List successfully saved to {filename} ({len(my_tasks)} tasks total)")
    except Exception as e:
        print(f"Error saving file: {e}")

    print("Current tasks:", my_tasks)


# test
add_task()



