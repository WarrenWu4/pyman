import typer
from initializer import getPaths, parsePaths, parseCommonPaths
from switcher import switcher

app = typer.Typer()

@app.command()
def install():
    try:
        print("\n------------------------------")
        print("Starting pyman installation...")
        paths = getPaths()
        paths = parsePaths(paths)
        morePaths = parseCommonPaths()
    except Exception as error:
        print("\tError ocurred while installing:", error)
        exit("Exiting....")


@app.command()
def list():
    pass

@app.command()
def switch(version):
    pass


@app.command()
def refresh():
    pass

    
@app.command()
def uninstall():
    pass

if __name__ == "__main__":
    app()
