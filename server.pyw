import time
import os
import string
import subprocess
CREATE_NO_WINDOW = 0x08000000
_DRIVES = ['%s:' % d for d in string.ascii_uppercase if os.path.exists('%s:' % d)]
def run_server(_drive, _subport):
    #subprocess.Popen("C:\\args.exe " + _drive + " " + _subport, creationflags=CREATE_NO_WINDOW)
    subprocess.Popen("pythonw C:\\args.pyw " + _drive + " " + _subport, creationflags=CREATE_NO_WINDOW)

for _DRIVE in range(len(_DRIVES)):
    run_server(_DRIVES[_DRIVE], str(_DRIVE))
    time.sleep(3)
