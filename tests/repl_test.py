# Import packages
## Custom
import setup_files
from src import repl
# from src import interp # TODO: <- Fix not recognizing interp package (2026-08-25)

# def test_hello():
#     assert repl.run('W 1+2') == '3', "EXPRESSION is FALSE"

# Test repl prompting
assert isinstance(repl.prompt(""), str), "Did NOT return string object!"
assert not repl.prompt(""), "Blank prompt was NOT empty!"
assert repl.prompt("prompt") == "prompt", "prompt() did NOT return accurate prompt!"