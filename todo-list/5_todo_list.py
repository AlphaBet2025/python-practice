"""
PROJECT 5 (simplified): TO-DO LIST
=====================================
Teaches: storing tasks in a list, and saving/loading that list to a
file so it's still there next time you run the program.
"""

import json

FILENAME = "tasks.json"


def load_tasks():
    # try to open the file; if it's not there yet, just start empty
    try:
        with open(FILENAME, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def save_tasks(tasks):
    with open(FILENAME, "w") as f:
        json.dump(tasks, f)


def show_tasks(tasks):
    if not tasks:
        print("No tasks yet.")
    for i, task in enumerate(tasks):
        print(i, "-", task)


def main():
    tasks = load_tasks()

    while True:
        print("\n1) Show tasks  2) Add task  3) Delete task  4) Quit")
        choice = input("Choose: ")

        if choice == "1":
            show_tasks(tasks)

        elif choice == "2":
            new_task = input("Task: ")
            tasks.append(new_task)   # add() puts it on the end of the list
            save_tasks(tasks)        # save right away so it isn't lost

        elif choice == "3":
            show_tasks(tasks)
            index = int(input("Number to delete: "))
            tasks.pop(index)         # pop() removes by position
            save_tasks(tasks)

        elif choice == "4":
            break

        else:
            print("Not a valid option.")


if __name__ == "__main__":
    main()
