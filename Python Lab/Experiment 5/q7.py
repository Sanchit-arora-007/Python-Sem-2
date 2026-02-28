tasks = []

while True:
    print("\n1.Add Task 2.View Tasks 3.Remove Task 4.Exit")
    ch = int(input("Enter choice: "))

    if ch == 1:
        task = input("Enter task: ")
        tasks.append(task)

    elif ch == 2:
        for i, task in enumerate(tasks, 1):
            print(i, task)

    elif ch == 3:
        num = int(input("Enter task number to remove: "))
        if 1 <= num <= len(tasks):
            tasks.pop(num - 1)

    elif ch == 4:
        break