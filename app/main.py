import sys


def main():
    sys.stdout.write("$ ")

    # Wait for user input
    while True:
        user_input =  input()
        print(f"{user_input}: command not found\n") 
    


if __name__ == "__main__":
    main()
