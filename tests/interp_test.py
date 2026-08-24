# File to test reading lines.

# Built-in/imported
import sys
from pathlib import Path

# Custom
import setup_files
from src import interp

# Check that interp.run()
## Check objectype
assert isinstance(interp.run("test"), str), "interp.run() NOT returning STR OBJECT"
## Check string contents
assert interp.run("test") == "test", "interp.run() did NOT PRINT CORRECT STRING"