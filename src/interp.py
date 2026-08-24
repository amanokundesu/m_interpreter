import io

def run(source: str) -> str:
    output = io.StringIO()
    for line in source.splitlines():
        exec_line(line, out)

def exec_line(line:str, out):
    line = line.strip()
    if not line:
        return
    command, _, args = line.split(' ')
    
