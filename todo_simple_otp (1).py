import heapq
import random

# ---------- STEP 1: LOGIN WITH OTP ----------

correct_username = "nancy"

print("===== LOGIN =====")
username = input("Enter username: ")

if username != correct_username:
    print("User not found. Exiting.")
    exit()

# Generate a random 6-digit OTP
otp = str(random.randint(100000, 999999))
print(f"Your OTP is: {otp}")   # in real app, this would be sent via SMS/email

entered_otp = input("Enter the OTP: ")

if entered_otp != otp:
    print("Wrong OTP. Exiting.")
    exit()

print("Login successful!\n")


# ---------- STEP 2: TODO APP (using heap) ----------

tasks = []   # this list will work as our priority queue

def add_task(name, priority):
    heapq.heappush(tasks, (priority, name))
    print(f"Added: {name} (priority {priority})")

def complete_task():
    if tasks:
        priority, name = heapq.heappop(tasks)
        print(f"Completed: {name}")
    else:
        print("No tasks left!")

def show_tasks():
    print("\n--- Your Tasks (priority order) ---")
    if not tasks:
        print("No tasks.")
    for priority, name in sorted(tasks):
        print(f"[{priority}] {name}")
    print()


# ---------- STEP 3: MENU ----------

while True:
    print("1. Add Task")
    print("2. Complete Top Priority Task")
    print("3. View All Tasks")
    print("4. Exit")

    choice = input("Choose (1-4): ")

    if choice == "1":
        name = input("Task name: ")
        priority = int(input("Priority (1 = most urgent): "))
        add_task(name, priority)

    elif choice == "2":
        complete_task()

    elif choice == "3":
        show_tasks()

    elif choice == "4":
        print("Bye!")
        break

    else:
        print("Invalid choice, try again.")
