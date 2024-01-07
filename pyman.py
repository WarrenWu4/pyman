import sys
import os
import subprocess
from windows import find_py_root, list_py_ver, switch_py_ver

# get user information
op_sys = sys.platform
shell = os.getenv("SHELL")
python_executable = sys.executable
# print("System Information:", op_sys, shell, python_executable)

# print("The operating system is:", op_sys)

# # get all versions of python on device
# py_versions = sys.version
# print("The python version is:", py_versions)

# # get the path of python on device
# py_path = sys.executable
# print("The python path is:", py_path)


def runCommand(command):
    process = subprocess.Popen(
        command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, text=True
    )
    stdout, stderr = process.communicate()
    return stdout, stderr


# list of all python versions
def listPyVer():
    versions = []
    out = f"Python versions:\n"

    if op_sys == "win32" or op_sys == "win64":
        # find location of python versions
        location = find_py_root()
        versions = list_py_ver(location)

    for version in versions:
        out += f"{version}"
    return out


# switch <version> to change python version
def switchPyVer(version):
    pass


def main():
    if len(sys.argv) < 2:
        print("Usage: python pyman.py list | switch <version>")
    elif sys.argv[1] == "list":
        print(listPyVer())
    elif sys.argv[1] == "switch":
        print(switchPyVer(sys.argv[2]))
    else:
        print("Usage: python pyman.py list | switch <version>")

from verifier import verify
if __name__ == "__main__":
    if (!verify()):
        print("Error: no Python interpreter detected\n")
    else:
        print("python doesn't exist")
