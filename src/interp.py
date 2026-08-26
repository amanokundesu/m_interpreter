"""
This file will contain the code to execute the provided commands. 
"""
import io
import expr

"""

"""
# TODO: Possibly add an exceptions class
# Later add multiline support 
def run(source: str) -> str:
    output = io.StringIO()
    for line in source.splitlines():
        exec_line(line, output)
    return output.getvalue()

"""

"""
def exec_line(line:str, output):
    line = line.strip()
    line = line.upper()
    if not line:
        return
    statement = line.split(' ') # <- TODO: error here in interp_test.py (2026-08-23)
    # TODO: Work around, better solution will come in the future. 
    command = statement[0]
    args = statement[1]
    match command[0]:
        case W:
            write_command(args, output)

"""
The M specification says that the WRITE command has this syntax: W[RITE][:tvexpr] expr|*intexpr|fcc[,...]

"""
def write_command(args: str, output):
    output.write(expr.evaluate(args))

