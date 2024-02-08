installation process --> initialize pygame and create necessary files/folders

from there can freely, list, switch, or reset pyman

uninstall process --> remove files and folders, reset alias

add pretty warnings and styling and stuff

# pyman

a simple python version manager

## processes

**installation process**

1. get $PATH env paths

2. parse $PATH env paths and store in dictionary as {ver: path}

3. recursively search default file paths in each os system and store python files found in dictionary as {ver: path}

4. create a dir ~/.pyman and copy the python files after parsing to the dir

5. add pyman to path and set alias

**list process**

1. search for ~/.pyman and list python versions in the dir

2. add msg to inform user to refresh if version not found

**switch process**

1. if a version is supplied, switch pyman alias in dotfiles

2. if a version isn't supplied, create multiple-choice prompt for user to choose a version

**refresh proceess**

1. reinitializes pyman (basically reinstalls it)

**uninstall process**

1. delete alias and ~/.pyman folder

## usage

**5 commands**

1. install: initializes pyman and creates necessary/edits files

    1.

2. list: list different python versions from .pyman dir

3. switch [ver (optional)]: switches to different python version available in .pyman dir

4. refresh [paths (optional)]: reinitializes pyman when new python version is installed

5. uninstall: removes all changes pyman created

_need to first install pyman before using it_
