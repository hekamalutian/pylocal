import sys
import subprocess
_CREATE_NO_WINDOW = 0x08000000
_DIRECTORY = sys.argv[1]
_SUB_PORT = sys.argv[2]
_COMMAND = "python -m http.server --directory " + _DIRECTORY + " 4916" + _SUB_PORT
subprocess.call(_COMMAND, creationflags=_CREATE_NO_WINDOW)