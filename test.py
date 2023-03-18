import requests

API_URL = "http://localhost:5000/Todo/"

def update():
    task_name = input("Enter the task name to update: ")
    response = requests.patch(API_URL + task_name)
    if response.status_code == 202:
        task = response.json()
        if task["status"] == True :
            task["status"] = False
            response = requests.put(API_URL + task_name, json=task)
            if response.status_code == 404:
                print("Unable to update task.")
            else:
                print(f"Task '{task_name}' marked as Completed.")
        elif task["status"] == False :
            task["status"] = True
            response = requests.put(API_URL + task_name, json=task)
            if response.status_code == 404:
                print("Unable to update task.")
            else:
                print(f"Task '{task_name}' updated to Not Completed.")
    else:
        print(f"Task '{task_name}' not found in the to-do list.")


def add():
    task_name = input("Enter the task name to add: ")
    task = {"name": task_name, "status": False}
    response = requests.post(API_URL + task_name, json=task)
    if response.status_code == 201:
        print(f"Added {task_name} in the list!")
    else:
        print("Unable to add task. Please don't use the same name and it has to be text only!")


def delete():
    task_name = input("Enter the task name to delete: ")
    response = requests.delete(API_URL + task_name)
    if response.status_code == 404:
        print(f"Task '{task_name}' not found in the to-do list.")
    else:
        print(f"Task '{task_name}' deleted.")


def view():
    response = requests.get(API_URL + "I love myself!")
    if response.status_code == 200:
        tasks = response.json()
        if tasks:
            for task in tasks:
                print(f"{task['name']}: {'Completed' if task['status'] else 'Not Completed'}")
        else:
            print("The to-do list is empty.")
    else:
        print("Unable to view tasks.")


def main():
    while True:

        print("Welcome to 'TO DO LIST' program! ")
        print("1. Add a new task")
        print("2. View all tasks")
        print("3. Update a task")
        print("4. Delete a task")
        print("5. Quit the program")

        try:
            user_choice = int(input("Choose the number : "))
            if user_choice > 5 or user_choice < 1:
                print("Please choose only 1-5 ")
                print("______________________")
            else:
                if user_choice == 1:
                    add()
                    print("______________________")
                elif user_choice == 2:
                    view()
                    print("______________________")
                elif user_choice == 3:
                    update()
                    print("______________________")
                elif user_choice == 4:
                    delete()
                    print("______________________")
                elif user_choice == 5:
                    print("Good bye!")
                    break

        except:
            print("Please input only number!")


if __name__ == '__main__':
    main()
