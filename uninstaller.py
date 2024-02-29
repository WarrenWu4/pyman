"""
uninstall script to remove pyman crap from your pc
"""
import os
from switcher import brancher, source

def removePymanDir(path=".pyman"):
    """
    Removes the pyman directory created during initialization

    Args
        path (str): defaults to the current working directory, but user can pass in the direct path
    """
    if (os.path.isdir(path)):
        print("Valid pyman directory found...")
        print("Deleting pyman files")
        files = os.listdir(path)
        for file in files:
            print(f"\tDeleting {file}")
            os.remove(file)
        print("Deleting .pyman folder")
        os.rmdir(path)
    else:
        print("Pyman directory not found...")
        exit("Exiting...")

def removeConfigChanges():
    """
    Deletes lines written in config files
    """
    path = brancher()
    if (path == None):
        print("Profile path not found...")
        return

    # first check if there's already something written
    shellConfig = []
    with open(path) as f:
        shellConfig = f.readlines()
    # then fucking eat shit
    with open(path, "w") as f:
        for line in shellConfig:
            if line == f"""export PATH="$PATH:/home/warrenwu/acc/cli-tool/.pyman"\n""":
                continue
            if "alias pie=\"pyman" == line[:16]:
                continue
            f.write(line)

    source(path)

def uninstall():
    removePymanDir()
    removeConfigChanges()
