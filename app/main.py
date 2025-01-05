import sys
import os

PATH = os.environ.get("PATH")
#Ensure the path seperator is correct based on Operating System (i.e if windows or not) 
PATH_SEPARATOR = ';' if os.name == 'nt' else ':' #
def handle_type(args):
    command = ""
    if args:
        command = args[0]
    if command in COMMANDS:
        print(f"{command} is a shell builtin")
        return
    
    #Search for the command in each directory in the Path
    for dir in PATH.split(PATH_SEPARATOR):
        p =f"{dir}/{command}"
        if os.path.exists(p):
            print(f"{command} is {p}")
            return
    
    print(f"{command}: not found")

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
