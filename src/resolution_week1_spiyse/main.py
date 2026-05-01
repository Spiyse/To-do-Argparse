import argparse
import sys
import os
import json

TASKS_FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r", encoding="utf-8") as file:
        return json.load(file)

def save_task(tasks):
    with open(TASKS_FILE, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=2)

parser = argparse.ArgumentParser()
parser.add_argument("task", type=str, nargs="?", help="Task to add")
parser.add_argument("-l", "--list", help="List all tasks", action="store_true")
parser.add_argument("-c", "--complete", type=int, help="Mark a task as complete by ID")
parser.add_argument("-d", "--delete", type=int, help="Delete a task by ID")
parser.add_argument("-i", "--id", type=int, help="Task ID to update priority")
parser.add_argument("-p", "--priority", choices=["high", "medium", "low"], help="Set task priority")
args = parser.parse_args()

if len(sys.argv) == 1:
    parser.print_help(sys.stderr)
    sys.exit(1)

if args.list:
    tasks = load_tasks()
    if tasks:
        for task in tasks:
            status = "x" if task["done"] else " "
            priority = task.get("priority", "none")
            print(f"[{status}] {task['id']}: {task['task']} ({priority})")
    else:
        print("There are no tasks!")
    sys.exit(0)

elif args.complete is not None:
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == args.complete:
            task["done"] = True
            save_task(tasks)
            print(f"Task {args.complete} marked as complete")
            break

elif args.priority:
    tasks = load_tasks()
    found = False
    for task in tasks:
        if task["id"] == args.id:
            task["priority"] = args.priority
            save_task(tasks)
            print(f"Task {args.id} priority set to {args.priority}")
            found = True
            break
    if not found:
        print(f"No task found with ID {args.id}")

elif args.delete is not None:
    tasks = load_tasks()
    new_task = [task for task in tasks if task["id"] != args.delete]
    if len(new_task) == len(tasks):
        print(f"No task found with ID {args.delete}")
    else:
        save_task(new_task)
        print(f"Task with ID of {args.delete} deleted")

elif args.task:
    tasks = load_tasks()
    new_id = 1 if len(tasks) == 0 else tasks[-1]["id"] + 1
    tasks.append({
        "id": new_id,
        "task": args.task,
        "done": False,
        "priority": "none"
    })
    save_task(tasks)
    print(f"Task {args.task} added with ID of {new_id}")