import json
from datetime import date
import sys

# Define ANSI escape codes for foreground colors and reset
RED = '\033[91m'
GREEN = '\033[92m'
BLUE = '\033[94m'
YELLOW = "\033[33m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
RESET = '\033[0m'  # Resets text attributes to default

def main():
   
   while True:
        entry = input(f'{YELLOW}task-cli{RESET} ')
        entry_list = entry.split(' ')
        option = entry_list.pop(0)

        if option == 'quit':
           sys.exit()

        elif option == 'add':
            task = ' '.join(entry_list).capitalize()
            add_task(task)

        elif option == 'update':
            id = entry_list.pop(0)
            task = ' '.join(entry_list).capitalize()
            update_task(id, task)

        elif option == 'delete':
            id = entry_list.pop()
            delete_task(id)

        elif (option == 'mark-in-progress') or (option == 'mark-done'):
            id = entry_list.pop()

            status = 'in-progress' if option == 'mark-in-progress' else 'done'

            set_status(status, id)
        elif option == 'list':
            status = None if not entry_list else entry_list.pop()
            list_tasks(status)

        else:
            print(f'{RED}Command not found{RESET}')

def add_task(task: str):
    try:
        with open("data.json", "r") as file:
            loaded_data = json.load(file)
            keys = list(loaded_data.keys())
            keys = sorted(keys)
            id = int(keys[-1]) + 1
    except:
        loaded_data = {}
        id = 1

    loaded_data[str(id)] = {"description": task,
                            "status": "todo",
                            "created_at": str(date.today()),
                            "updated_at": "None"}
    
    with open("data.json", "w") as file:
        json.dump(loaded_data, file, indent=4)
    
    print(f"{GREEN}Task added successfully (ID: {id}){RESET}")

def update_task(id: str, task: str):
    with open("data.json", "r") as file:
        loaded_data = json.load(file)
    
    loaded_data[id]['description'] = task
    loaded_data[id]['updated_at'] = str(date.today())

    with open("data.json", "w") as file:
        json.dump(loaded_data, file, indent=4)
    
    print(f"{BLUE}Task updated successfully (ID: {id}){RESET}")


def delete_task(id: str):
    with open("data.json", "r") as file:
        loaded_data = json.load(file)
    del loaded_data[id]
    with open("data.json", "w") as file:
        json.dump(loaded_data, file, indent=4)
    
    print(f"{RED}Task deleted successfully{RESET}")

def set_status(status: str, id: str):
    # Marking a task as in progress or done
    with open("data.json", "r") as file:
        loaded_data = json.load(file)
    
    loaded_data[id]['status'] = status
    loaded_data[id]['updated_at'] = str(date.today())

    with open("data.json", "w") as file:
        json.dump(loaded_data, file, indent=4)
    
    print(f"{BLUE}Task updated successfully (ID: {id}){RESET}")

def list_tasks(status: str):
    with open("data.json", "r") as file:
        loaded_data = json.load(file)

    keys = list(loaded_data.keys())
    print('ID\tSTATUS\t\tCREATE AT\tUPDATE AT\tDESCRIPTION')
    if status != None:
        for key, value in loaded_data.items():
            properties = list(value.values())
            if properties[1] == status: 
                print(f'{key:8}{properties[1]:16}{properties[2]:16}{properties[3]:16}{properties[0]}')
    else:
        for key, value in loaded_data.items():
            properties = list(value.values())           
            print(f'{key:8}{properties[1]:16}{properties[2]:16}{properties[3]:16}{properties[0]}')
        
        


if __name__ == '__main__':
    main()
    



