# File to test reading lines.

# Built-in
import sys
import io
from pathlib import Path

# Custom
import setup_files
from src import interp

# Check that interp.run() works properly.
## Check object type
assert isinstance(interp.run("test"), str), "interp.run() NOT returning STR OBJECT"
## Check string contents
assert interp.run("W 1+2") == "3", "interp.run() did NOT PRINT CORRECT STRING"

# Check that interp.write_command() works properly.
# W[RITE][:tvexpr] expr|*intexpr|fcc[,...] (https://docs.yottadb.com/ProgrammersGuide/commands.html#write)
## Check Regular (Standard) expressions (`expr`)
# ### Check object type
# temp_stringio_output:all
# interp.write_command("W 2+3", temp_stringio_output)
# assert isinstance(temp_stringio_output, io.StringIO), ""
### Check correct output
temp_stringio_output = io.StringIO
interp.run("W 2+3", temp_stringio_output)
temp_str = temp_stringio_output.getvalue()
temp_stringio_output.close()
assert temp_str == "5", "Write Expression did NOT write correct value"
## Check ASCII



