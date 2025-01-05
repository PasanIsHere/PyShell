import sys

def handle_type(args):
    command = ""
    if args:
        command = args[0]
    if command in COMMANDS:
        print(f"{command} is a shell builtin")
    else:
        print(f"{command}: command not found")

COMMANDS = {
    'echo': lambda *args: print(*args),
    'exit': lambda code=0: exit(int(code)),
    'type': lambda *args: handle_type(args)
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
            print(f"{' '.join(user_input)}: command not found") 
    


if __name__ == "__main__":
    main()
