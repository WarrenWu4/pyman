"""
uninstall script to remove pyman crap from your pc
"""
import os
from switcher import brancher, source

def findPymanDir():
    """
    Finds the pyman directory after it's been added to path

    Returns
        path (str): path to .pyman directory
    """
    try:
        print("1. Getting pyman from $PATH env var...")
        paths = os.environ['PATH'].strip().split(":")
        for path in paths:
            if (".pyman" == path[-6:]):
                return path
        print("SUCCESS")
    except:
        print("ERROR")
        exit("Exiting...")
    

def removePymanDir(path):
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
    print(findPymanDir())
    # removePymanDir(findPymanDir())
    # removeConfigChanges()
