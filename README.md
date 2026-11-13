# To-do Argparse

A small command-line to-do list written in Python with `argparse`. Add tasks, list them, mark them done, set priorities and delete them, all from the terminal. Tasks are saved to a `tasks.json` file, so they stay there between runs.

This is my Week 1 project for [Hack Club](https://hackclub.com/) Resolution (Python).

## Features

- Add tasks with a single command
- List all tasks with their status and priority
- Mark tasks as complete
- Set a priority (`high`, `medium` or `low`) on any task
- Delete tasks by ID
- No dependencies, only the Python standard library

## Requirements

- Python 3.8 or newer

## Installation

Clone the repository and install it with pip. This adds a `todo` command to your terminal.

```bash
git clone https://github.com/Spiyse/To-do-Argparse.git
cd To-do-Argparse
pip install .
```

Install it inside a virtual environment so it stays separate from your system Python:

```bash
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install .
```

You can also run the script directly without installing:

```bash
python src/resolution_week1_spiyse/main.py --help
```

## Usage

```
todo [task] [-l] [-c ID] [-d ID] [-i ID -p {high,medium,low}]
```

| Command | What it does |
| --- | --- |
| `todo "Task text"` | Add a new task |
| `todo -l` / `todo --list` | List all tasks |
| `todo -c ID` / `todo --complete ID` | Mark a task as complete |
| `todo -i ID -p LEVEL` / `todo --id ID --priority LEVEL` | Set a task's priority (`high`, `medium` or `low`) |
| `todo -d ID` / `todo --delete ID` | Delete a task |
| `todo -h` / `todo --help` | Show help |

Running `todo` with no arguments prints the help message.

### Example

```console
$ todo "Buy milk"
Task Buy milk added with ID of 1

$ todo "Finish homework"
Task Finish homework added with ID of 2

$ todo -i 2 -p high
Task 2 priority set to high

$ todo -c 1
Task 1 marked as complete

$ todo -l
[x] 1: Buy milk (none)
[ ] 2: Finish homework (high)

$ todo -d 1
Task with ID of 1 deleted
```

In the list, `[x]` means done and `[ ]` means not done yet. The value in brackets at the end is the priority (`none` until you set one).

## How tasks are stored

Tasks are saved in `tasks.json` in the folder you run the command from. Each task looks like this:

```json
{
  "id": 1,
  "task": "Buy milk",
  "done": false,
  "priority": "none"
}
```

Because the file is created in the current folder, running `todo` from a different folder gives you a separate task list. The file is listed in `.gitignore`, so your tasks won't be committed.

## Notes

- Each run does one action. If you pass several flags, only the first one in this order is used: list, complete, priority, delete, add.
- New task IDs are the last task's ID plus one, so IDs of deleted tasks aren't reused unless you delete the last one.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
