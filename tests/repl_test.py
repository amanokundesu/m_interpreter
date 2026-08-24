# Custom
import setup_files
from src import repl

def test_hello():
    assert repl.run('W 1+2') == '3', "EXPRESSION is FALSE"