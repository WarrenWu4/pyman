"""
initialization step of pyman
"""
import subprocess
import os
import re

def getPaths():
    """
    gets all paths from the $PATH env var by executing "echo $PATH"

    Returns:
        list: paths from $PATH env var
    """
    paths = subprocess.check_output("echo $PATH", shell=True, text=True)
    return paths.strip().split(":")

def getPythonVersion(pythonFile):
    """
    runs the pythonfile via the direct path to get the version then returns the version 

    Args:
        pythonFile (str): path to the python executable/binary file

    Returns:
        str: version number in string format
    """
    try:
        version = subprocess.check_output(f"{pythonFile} -V", shell=True, text=True)
        # version should be in the format "Python x.x.x" if not well then ur fucked
        version = version.strip().split()[-1]
        return version
    except:
        print("Error getting version for:", pythonFile)
        return None

def parsePaths(paths):
    """
    parses paths to get paths to all python files

    Args:
        paths (list): list of directories to parse through

    Return:
        dict{version:path}: hash map where key is the version and path is the path 
    """
    validPaths = {} 
    for path in paths:
        files = os.listdir(path) if (os.path.isdir(path)) else []
        for file in files:
            if (re.search("^python(\d*\.*)+(exe)?$", file)):
                pythonPath = f"{path}/{file}"
                pythonVer = getPythonVersion(pythonPath)
                if pythonVer != None:
                    validPaths[pythonVer] = pythonPath
    return validPaths

def parseCommonPaths(paths=["", "", ""]):
    """
    does the same thing as parsePaths() except it recursively searches for specific paths that usually store python

    Return:
        list: paths to python files found
    """

def createCopies(pythonPaths):
    """
    creates copies of pythonfiles from parsed paths into .pyman directory and renames the files as pyman[ver]

    Args:
        pythonPaths (list): list from parsing paths
    
    Returns:
        None
    """
    dir = ".pyman"
    if (not os.path.isdir(dir))
        os.makedirs(dir) # make .pyman folder if it doesn't exist
    for ver, path in pythonPaths.items():
        os.popen(f"cp {path} {dir}/pyman{ver}")
