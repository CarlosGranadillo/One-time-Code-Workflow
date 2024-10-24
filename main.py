import sys

def parse_changes(file_path):
    messages = []
    with open(file_path, 'r') as f:
        for line in f.readlines():
            status, path = line.strip().split("\t")
            if path.startswith("iterable_asset_definitions/"):
                task = "create" if status == "A" else "update" if status == "M" else None
                if task:
                    messages.append({"task": task, "path": path})
    return messages

def process_changes(messages):
    for message in messages:
        task = message['task']
        path = message['path']
        print(f"Task: {task}, Path: {path}")
        # In the future, you would replace the print statements with API calls:
        # if task == "create":
        #     call_create_endpoint(path)
        # elif task == "update":
        #     call_update_endpoint(path)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <changes_file>")
        sys.exit(1)

    changes_file = sys.argv[1]
    messages = parse_changes(changes_file)
    process_changes(messages)
