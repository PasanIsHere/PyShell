import sys


def main():

    # Wait for user input
    while True:
        sys.stdout.write("$ ")
        user_input =  input()
        if user_input == "exit 0":
            exit(0)
        print(f"{user_input}: command not found") 
    


if __name__ == "__main__":
    main()
