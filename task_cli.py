import sys
import json
import os
from datetime import datetime

FILE = 'tasks.json'

def load_tasks():
    if not os.path.exists(FILE):
        return []
    with open(FILE, 'r') as f:
        return json.load(f)

def save_tasks(tasks):
    with open(FILE, 'w') as f:
        json.dump(tasks, f, indent=4)

def add_task(description):
    tasks = load_tasks()
    task_id = max([task['id'] for task in tasks], default=0) + 1
    new_task = {
        'id': task_id,
        'description': description,
        'status': 'todo',
        'createdAt': datetime.now().isoformat(),
        'updatedAt': datetime.now().isoformat()
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task added successfully (ID: {task_id})")

def update_task(task_id, new_description):
    tasks = load_tasks()
    task = find_task(tasks, task_id)
    if not task:
        print("Task not found.")
        return
    task['description'] = new_description
    task['updatedAt'] = datetime.now().isoformat()
    save_tasks(tasks)
    print(f"Task {task_id} updated.")

def delete_task(task_id):
    tasks = load_tasks()
    tasks = [task for task in tasks if task['id'] != task_id]
    save_tasks(tasks)
    print(f"Task {task_id} deleted.")

def mark_status(task_id, status):
    tasks = load_tasks()
    task = find_task(tasks, task_id)
    if not task:
        print("Task not found.")
        return
    task['status'] = status
    task['updatedAt'] = datetime.now().isoformat()
    save_tasks(tasks)
    print(f"Task {task_id} marked as {status}.")

def list_tasks(status=None):
    tasks = load_tasks()
    filtered = tasks if status is None else [t for t in tasks if t['status'] == status]
    if not filtered:
        print("No tasks found.")
        return
    for task in filtered:
        print(f"[{task['id']}] {task['description']} — {task['status']} (Updated: {task['updatedAt']})")

def print_usage():
    print("""Usage:
  task-cli add "Task description"
  task-cli update <id> "New description"
  task-cli delete <id>
  task-cli mark-in-progress <id>
  task-cli mark-done <id>
  task-cli list [todo|in-progress|done]""")

def main():
    if len(sys.argv) < 2:
        print_usage()
        return

    command = sys.argv[1]

    try:
        if command == 'add' and len(sys.argv) >= 3:
            description = ' '.join(sys.argv[2:])
            add_task(description)

        elif command == 'update' and len(sys.argv) >= 4:
            task_id = int(sys.argv[2])
            new_description = ' '.join(sys.argv[3:])
            update_task(task_id, new_description)

        elif command == 'delete' and len(sys.argv) == 3:
            task_id = int(sys.argv[2])
            delete_task(task_id)

        elif command == 'mark-in-progress' and len(sys.argv) == 3:
            task_id = int(sys.argv[2])
            mark_status(task_id, 'in-progress')

        elif command == 'mark-done' and len(sys.argv) == 3:
            task_id = int(sys.argv[2])
            mark_status(task_id, 'done')

        elif command == 'list':
            if len(sys.argv) == 3:
                list_tasks(sys.argv[2])
            else:
                list_tasks()

        else:
            print("Invalid command or arguments.")
            print_usage()

    except ValueError:
        print("Invalid ID. ID must be an integer.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()
