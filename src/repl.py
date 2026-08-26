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
    prompt:str = prompt()
    if not prompt.strip():
        continue
    elif prompt == "exit":
        break