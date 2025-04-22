# TaskTrack

TaskTrack is a command-line interface (CLI) application for tracking and managing tasks. It is designed to be simple, efficient, and dependency-free. The application uses a local JSON file for persistent storage and supports common task management operations from the command line.

## Features

- Add, update, and delete tasks
- Mark tasks as todo, in-progress, or done
- List all tasks or filter by status
- Stores data in a local JSON file
- Requires no external libraries or frameworks

## Getting Started

### Project at:
https://roadmap.sh/projects/task-tracker

### Clone the Repository

```
git clone https://github.com/your-username/tasktrack.git
cd tasktrack
chmod +x task_cli.py
```

### Running the Application

Use the following syntax to execute commands:

```
./task_cli.py <command> [arguments]
```

## Commands and Usage

### Add a Task

```
./task_cli.py add "Buy groceries"
```

### Update a Task

```
./task_cli.py update <id> "New description"
```

### Delete a Task

```
./task_cli.py delete <id>
```

### Mark a Task as In Progress

```
./task_cli.py mark-in-progress <id>
```

### Mark a Task as Done

```
./task_cli.py mark-done <id>
```

### List All Tasks

```
./task_cli.py list
```

### List Tasks by Status

```
./task_cli.py list todo
./task_cli.py list in-progress
./task_cli.py list done
```

## Data Structure

All tasks are stored in a file named `tasks.json` in the current directory. This file is automatically created if it does not exist.

Each task has the following structure:

```json
{
  "id": 1,
  "description": "Sample task",
  "status": "todo",
  "createdAt": "2025-04-22T14:30:00",
  "updatedAt": "2025-04-22T14:30:00"
}
```

## Notes

- The application handles basic validation and edge cases.
- It is implemented using only the standard library of the chosen programming language (Python).

## Repository
https://github.com/1ndrayu/tasktrack
