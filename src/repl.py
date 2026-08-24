"""
File: repl.py


"""
def core_loop():
    # Thread support later
    flag = True
    while(flag):
        line = input("M_Interpreter: ")
        process_line(line)

# placeholder
def process_line(line: str):
    print("Line processed")