# setup_paths.py
from pathlib import Path
import sys

# Import using built-in Path object
PROJ_ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(PROJ_ROOT_DIR))