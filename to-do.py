tasks = []
def menu():
    print("\n ---- TO-DO List ----\n")
    print("1. VIEW TASKS")
    print("2. ADD TASK")
    print("3. REMOVE TASK")
    print("4. MARK TASK AS COMPLETED")
    print("5. EXIT")

def viewtask():
    if not tasks:
        print("No tasks yet entered")
    else:
        for index, task in enumerate(tasks):
            status = "DONE" if task['done'] else "NOT DONE"
            print(f"{index}. [{status}] {task['title']}")


def addtask():
    title = input("Enter task: ")
    tasks.append({"title": title, "done": False})
    print("TASK ADDED")

def removetask():
    viewtask()
    index = int(input("Enter task number to delete: "))
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        print(f"TASK REMOVED: {removed['title']}")
    else:
        print("TASK NOT FOUND")

def marktask():
    viewtask()
    index = int(input("Enter task number to mark done: "))
    if 0 <= index < len(tasks):
        tasks[index]['done'] = True
        print(f"TASK MARKED: {tasks[index]['title']}")
    else:
        print("TASK NOT FOUND")

while True:
    menu()
    choice = input("Enter your choice: ")
    if choice == "1":
        viewtask()
    elif choice == "2":
        addtask()
    elif choice == "3":
        removetask()
    elif choice == "4":
        marktask()
    elif choice == "5":
        print("THANK YOU FOR USING TO-DO LIST")
        break
