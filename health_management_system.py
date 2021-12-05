# 3 Clients - Harry, Rohan, Hammad
# Total 6 files:
# Write a function that when executed takes as input client_name
name = input("enter name: ")

def start():
    print("What do you want to do?")
    entry()

def meal_log():
    meal = input("What did you eat today? ")
    write_file("meal", meal)

def exercise_log():
    exercise = input("Which exercise did you do today? ")
    write_file("exercise", exercise)

def write_file(activity, activity_detail):
    with open(f"{name}.txt", "a") as file:
        file.write(f"{activity}: {activity_detail}\n")
    print(f"{activity} added successfully")

def read_file():
    try:
        with open(f"{name}.txt") as file:
            print(file.read())
    except Exception as e:
        print(e)
    finally:
        option = input("Do you want to continue? Y/N")
        if option == "y":
            start()
        elif option == "n":
            exit()
        else:
            print("Invalid input")

def entry():
    choice = int(input("1: Log\n2: Retrieve\n"))

    if choice == 1:
        option = int(input("What do you want to log?\n1: Meal\n2: Exercise"))
        if option == 1:
            meal_log()
        elif option == 2:
            exercise_log()
        else:
            print("Invalid input")

    elif choice == 2:
        read_file()

if __name__ == "__main__":
    start()