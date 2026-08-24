import io

# Later add multiline support 
def run(source: str) -> str:
    output = io.StringIO()
    for line in source.splitlines():
        exec_line(line, output)
    return output.getvalue()

def exec_line(line:str, out):
    line = line.strip()
    line = line.upper()
    if not line:
        return
    command, _, args = line.split(' ')
    match command[0]:
        case W:
            write_command(args)

"""
The M specification says that the WRITE command has this syntax: W[RITE][:tvexpr] expr|*intexpr|fcc[,...]

"""
def write_command(args: str):
    pass