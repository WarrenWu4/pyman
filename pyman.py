import typer
import os
from initializer import initialize 
from switcher import switcher
from uninstaller import uninstall

app = typer.Typer()

@app.command()
def install():
    try:
        print("\n------------------------------")
        print("Starting pyman installation...")
        initialize()
    except Exception as error:
        print("\tError ocurred while installing:", error)
        exit("Exiting....")


@app.command()
def list():
    # check if ~/.pyman exists
    if (os.path.exists(".pyman")):
        print("Pyman detected the following python versions:")
        versions = os.listdir(".pyman")
        # print out versions
        for version in versions:
            ver = version[5:]
            print(f"\tPython: {ver}")
    else:
        print("No .pyman directory found, make sure to install pyman first")
        exit("Exiting....")

@app.command()
def switch(version):
    if (os.path.exists(".pyman")):
        try:
            switcher(version)
        except Exception as error:
            print("Error occurred switching versions:", error)
            exit("Exiting...")
    else:
        print("No .pyman directory found, make sure to install pyman first")
        exit("Exiting....")


@app.command()
def refresh():
    try:
        print("\n------------------------------")
        print("Refreshing pyman initialization script...")
        initialize()
    except Exception as error:
        print("\tError ocurred while :", error)
        exit("Exiting....")

    
@app.command()
def uninstall():
    try:
        print("\n------------------------------")
        print("Uninstalling pyman...")
        uninstall()
    except Exception as error:
        print("\tError ocurred while uninstalling:", error)
        exit("Exiting....")

if __name__ == "__main__":
    app()
