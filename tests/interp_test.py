# File to test reading lines.

# Built-in/imported
import sys
from pathlib import Path

# Custom
import setup_files
from src import interp

if interp.run("test") != "test":
    print('FAIL')

print('ALL PASS')