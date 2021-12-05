# 3 Clients - Harry, Rohan, Hammad
# Total 6 files:
# Write a function that when executed takes as input client_name
name = input("enter name: ")

def start():
    print("What do you want to do?")
    entry()

def write_file():
    content = input("Enter your log detail")
    with open(f"{name}.txt", "a") as file:
        file.write(f"{content}\n")

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
        write_file()

    elif choice == 2:
        read_file()

if __name__ == "__main__":
    start()