#Task Manager console app

task_list = {}

def options_menu():
    options = {"a": "add task to the list",
              "b": "delete task from the list",
              "c": "show all tasks",
              "d": "exit"}
    return options
    
def add_task(task_list):
    if not task_list:
        print("You have no tasks yet. Don't worry, let's write the first one!")
        number = int(input("Write a number of task: "))
        priority = input("Choose priority: ")
        name = input("Write the name of your task: ")
        date = input("Write a date of task complition: ") 
        task_list[number] = {
            "date": date,
            "priority": priority,
            "name": name}
        print("\nGreat! Your task was written!")
        print(task_list)
    else: 
        print("\nYou can choose another options. What's next?")

    if number in task_list:
        print(f"You already have task number {number}. Please choose another number.")
    

def delete_task():
    return None

def show_tasks():
    print("You have no tasks yet." 
          if not task_list else task_list)

def mark_task_done():
    return None

def save_by_priority():
    return None

def sorting():
    return None
    
options = options_menu()

print("Welcome to your Task List.")
print("You can choose one of the options below:")
print(options)      
user_input = input()
    
while True:
    try:
        if user_input == "a":
            add_task(task_list)
            
        elif user_input == "b":
            delete_task()
            print("You can choose another option or exit the program. What's next?")
            
        elif user_input == "c":
            show_tasks()
            print("You can choose another option or exit the program. What's next?")
            
        elif user_input == "d":
            print("Thanks for your time. If you want to write a new task, feel free to use this script again!")
            break
    except (ValueError, SyntaxError, NameError):
        print ("Please choose options from the list")
        break
     
    # Print Menu
    # Ask for user choice
    # other