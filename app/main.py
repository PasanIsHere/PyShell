import sys


def main():

    # Wait for user input
    while True:
        sys.stdout.write("$ ")
        user_input =  input()
        print(f"{user_input}: command not found\n") 
    


if __name__ == "__main__":
    main()
