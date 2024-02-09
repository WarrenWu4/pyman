"""
helper file for switching logic when switch command is called
"""
import sys
import os
import subprocess

def brancher():
    """
    controls branching logic for pyman by sorting by os and then shell environment

    Returns:
        str: path to profile to be edited
    """
    unix = ["linux", "linux2", "darwin"]
    windows = ["win32", "win64", "cygwin", "msys"]
    opSys = sys.platform
    if (opSys in unix):
        shellPath = os.environ['HOME']+"/."+os.environ['SHELL'].split("/")[-1]+"rc"
    elif (opSys in windows):
        shellPath = subprocess.check_output("$PROFILE", shell = True, text=True)
    else:
        print(opSys, "is not supported by pyman")
        return None
    return shellPath

def writer(path, ver):
    """
    writes the commands to switch python versions in dotfiles/profile

    Args:
        path (str): path to dotfile/profile
        ver (str): python version to switch to

    Returns:
        bool: True if successful, False otherwise
    """
    pymanDir = os.environ['PWD'] + "/.pyman"

    # first check if there's already something written
    [pathFound, aliasFound] = [False, False]
    shellConfig = []
    with open(path) as f:
        shellConfig = f.readlines()
    for line in shellConfig:
        if line == f"""export PATH="$PATH:/home/warrenwu/acc/cli-tool/.pyman"\n""":
            pathFound = True
        elif line == f"""alias pie="pyman{ver}"\n""":
            aliasFound = True

    with open(path, "a") as f:
        if (not pathFound):
            f.write(f"""\nexport PATH="$PATH:{pymanDir}"\n""")
        if (not aliasFound):
            f.write(f"""alias pie="pyman{ver}"\n""")
    return True

def source(path):
    """
    properly sources edited dotfiles

    Args:
        path (str): path to dotfile
    """
    os.system(f"source {path}")

def switcher(ver):
    writer(brancher(), ver)
    source(brancher())

