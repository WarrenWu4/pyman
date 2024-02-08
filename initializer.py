"""
startup script for pyman:
    1. find and return python binary file paths
        1a. search paths in path env var
        1b. recursively search default paths in os
    2. run binary file paths and return a dictionary of {ver: path}
    3. copy all binary files into ~/.pyman/python/python{ver}
"""
import subprocess
import os
import re

def getPythonPaths():
    """
    find and return all python binary files found within the $PATH env var & default paths

    Returns:
        list: path to python binary files
        int: -1 if error occurred and 1 if successful
    """
    pyPaths = []
    # try to get $PATH env var
    try:
        print("1. Getting paths from $PATH env var...")
        paths = os.environ['PATH'].strip().split(":")
        print("SUCCESS")
    except:
        print("ERROR")
        return [[], -1]

    # parse paths to see if python exists 
    try:
        print("2. Parsing paths from $PATH to find python files...")
        for path in paths:
            files = os.listdir(path) if (os.path.isdir(path)) else []
            for file in files:
                if (re.search("^python(\d*\.*)+(exe)?$", file)):
                    pyPaths.append(f"{path}/{file}")
        print("SUCCESS")
    except:
        print("ERROR")
        return [[], -1]

    # recursively searches common python installation paths
    try:
        print("3. Recursively searching common python installation paths...") 
        user = os.environ['USER']
        installPaths = [f"C:\\Users\\"+user+"\\AppData\\Local\\Programs\\Python"]
        def recursiveSearch(path):
            files = os.listdir(path) if (os.path.isdir(path)) else []
            for file in files:
                if (os.path.isdir(f"{path}/{file}")):
                    recursiveSearch(f"{path}/{file}")
                if (re.search("^python(\d*\.*)+(exe)?$", file)):
                    pyPaths.append(f"{path}/{file}")

        for installPath in installPaths:
            if (os.path.exists(installPath)):
                recursiveSearch(installPath)
        print("SUCCESS")
    except:
        print("ERROR")
        return [[], -1]

    return [pyPaths, 1]

def initialize():
    """
    runs the startup script and handles any errors
    """
    print("---Starting initialization script for pyman---")
    [paths, error] = getPythonPaths()
    if (error == -1):
        return
    print("---Successfully got python paths---")
    print("---Getting python versions for python paths---")
    try:
        pyman = {}
        for path in paths:
            version = getPythonVersion(path)
            pyman[version] = path
    except:
        print("ERROR")
        exit()
    print("---Successfully got python versions---")
    print("---Copying python files to ~/.pyman---")
    try:
        createCopies(pyman)
    except:
        print("ERROR")
        exit()
    print("---Successfully copied python files to ~/.pyman---")
    print("---Successfully initialized pyman---")

def getPythonVersion(pythonFile):
    """
    runs the pythonfile via the direct path to get the version then returns the version 
    version should be in the format "Python x.x.x" if not well then ur fucked

    Args:
        pythonFile (str): path to the python executable/binary file

    Returns:
        str: version number in string format
    """
    try:
        print("\t\t+ getting python version for", pythonFile)
        version = subprocess.check_output(f"{pythonFile} -V", shell=True, text=True)
        version = version.strip().split()[-1]
        return version
    except:
        raise Exception("***error getting python version for", pythonFile)

def createCopies(pythonPaths):
    """
    creates copies of pythonfiles from parsed paths into .pyman directory and renames the files as pyman[ver]

    Args:
        pythonPaths (dict): hash map with {version: path} key-value pair from parsing paths

    Returns:
        str: the directory all the copied python files are stored in 
    """
    dir = ".pyman"
    if (not os.path.isdir(dir)):
        os.makedirs(dir) # make .pyman folder if it doesn't exist
    for ver, path in pythonPaths.items():
        os.popen(f"cp {path} {dir}/pyman{ver}")
    return dir







