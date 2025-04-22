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

def main():
    if len(sys.argv) < 2:
        print("Usage: task-cli <command> [arguments]")
        return
    command = sys.argv[1]
    if command == 'add' and len(sys.argv) >= 3:
        description = ' '.join(sys.argv[2:])
        add_task(description)
    else:
        print("Unknown command or missing arguments.")

if __name__ == '__main__':
    main()
