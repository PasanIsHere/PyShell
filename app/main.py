import sys

COMMANDS = {
    'exit': lambda code=0: exit(int(code)),
    'echo': lambda *args: print(*args)
}
def main():

    # Wait for user input
    while True:
        sys.stdout.write("$ ")
        user_input =  input().strip().split()

        command, *args = user_input
            
        handler = COMMANDS.get(command)
        if handler:
            handler(*args)
        else:
            print(f"{user_input}: command not found") 
    


if __name__ == "__main__":
    main()
