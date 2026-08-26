"""
This file will contain the code to execute the provided commands. 
"""
import io
from src import expr

"""

"""
# TODO: Possibly add an exceptions class
# Later add multiline support 
def run(source:str) -> str:
    '''
    Run the commands written in `source` parameter,
    and returns the command run.
    '''
    output = io.StringIO()
    for line in source.splitlines():
        exec_line(line, output)x
    return output.getvalue()

"""

"""
def exec_line(line:str, output):
    '''
    Executes the actual line into the output stream.
    '''
    line = line.strip()
    if not line:
        return
    statement = line.split(' ') # <- TODO: error here in interp_test.py (2026-08-23)
    # TODO: Work around, better solution will come in the future. 
    command = statement[0].upper()
    args = statement[1]
    match command[0]:
        case W:
            write_command(args, output)

"""
The M specification says that the WRITE command has this syntax: W[RITE][:tvexpr] expr|*intexpr|fcc[,...]

"""
def write_command(args:str, output):
    output.write(expr.evaluate(args))

"""
From https://docs.yottadb.net/ProgrammersGuide/commands.html#set

SET assigns values to variables or to a selected portion of a variable.

The format of the SET command is:

S[ET][:tvexpr] setleft=expr | (setleft[,...])=expr | *lvn=lname | aliascontainer[,...]
where

setleft == glvn | $EXTRACT(glvn,[,intexpr1[,intexpr2]]) | $PIECE(glvn,expr1[,intexpr1[,intexpr2]]) | isv
and

aliascontainer == lvn | exfunc | exvar

"""
def set_command(args:str, output):
    x = args
    output.write("Set " + x)
"""
From https://docs.yottadb.net/ProgrammersGuide/commands.html#kill

The KILL command deletes local or global variables and their descendant nodes.

The format of the KILL command is:

K[ILL][:tvexpr] [glvn | (lvn[,...]) | *lname | *lvn ]

"""
def kill_command(args:str, output):
    output.write("Kill command")
"""
From https://docs.yottadb.net/ProgrammersGuide/commands.html#quit

Except when a QUIT appears on a line after a FOR, the QUIT command terminates the execution of the current YottaDB invocation stack level initiated by a DO, XECUTE, extrinsic function or special variable, and returns control to the next "lower" level. In this case, QUIT restores any values stacked at the current level by NEWs or by parameter passing. A QUIT command terminates any closest FOR command on the same line. Note that M overloads the QUIT command to terminate DO, FOR, XECUTE and extrinsics ($$) of which FOR is the most different.

The format of the QUIT command is:

Q[UIT][:tvexpr] [expr | *lname | *lvn]
"""
def quit_command(args:str, output):
    output.write("Quit command")

"""
Command table
"""
COMMANDS = {
    'W': write_command,  'WRITE': write_command,
    'S': set_command,    'SET':   set_command,
    'K': kill_command,   'KILL':  kill_command,
    'Q': quit_command,   'QUIT':  quit_command
}
