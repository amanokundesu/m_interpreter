import io

# Later add multiline support 
def run(source:str) -> str:
    '''
    Run the commands written in `source` parameter,
    and returns the command run.
    '''
    output = io.StringIO()
    for line in source.splitlines():
        exec_line(line, output)
    return output.getvalue()

def exec_line(line:str, output):
    '''
    Executes the actual line into the output stream.
    '''
    line = line.strip()
    line = line.upper()
    if not line:
        return
    command, _, args = line.split(' ') # <- TODO: error here in interp_test.py (2026-08-23)
    match command[0]:
        case W:
            write_command(args, output)

"""
The M specification says that the WRITE command has this syntax: W[RITE][:tvexpr] expr|*intexpr|fcc[,...]

"""
def write_command(args:str, output):
    output.write(evaluate(args))

def evaluate(args:str) -> str:
    return "Placeholder"