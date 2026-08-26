"""
File: repl.py
"""
# Import packages

## Built-in

## Custom
import interp

def prompt() -> str:
    '''
    Prompt to collect input
    '''
    print("MINTERP REPL> ", end="")
    try:
        return input()
    except EOFError as eoferror:
        print(eoferror)
        return ""

# Start main loop
loop_run:bool = True
while loop_run:
    try:
        line:str = prompt()
        if not line.strip():
            continue
        elif line == "exit":
            break
        else:
            # Execute commands run, passing into interp.py
            # TODO: Consider exceptions later
            try:
                interp.run()
            except Exception as e:
                print(e)
    except KeyboardInterrupt as keyboardinterrupt:
        # TODO: Find a way to gracefully kill running processes.
        try:
            print(" Caught keyboard interrupt.")
            while True:
                temp_confirm:str = input("Confirm? [y/n]: ")
                match temp_confirm.strip().lower():
                    case "y"|"yes":
                        loop_run = False
                    case "n"|"no":
                        print("continuing...")
                    case _:
                        print("Please write an accurate option")
                        continue
                break
        except KeyboardInterrupt as keyboardinterrupt2:
            print("Confirming keyboard interrupt.")
            loop_run = False