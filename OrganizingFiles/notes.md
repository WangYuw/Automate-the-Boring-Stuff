#shutil Module

This module has functions to let you copy, move, rename, and delete files in your Python programs. 

    import shutil

1. Copying files and folders

	- Calling `shutil.copy(source, destination)` will copy the file at the path source to the folder at the path destination.

	- Calling `shutil.copytree(source, destination)` will copy the folder at the path source, along with all of its files and subfolders, to the folder at the path destination.

2. Moving and renaming files and folders

	- Calling `shutil.move(source, destination)` will move the file or folder at the path source to the path destination and will return a string of the absolute path of the new location.

		The folders that make up the destination must already exist

3. Permanently deleting files and folders

	- Calling `os.unlink(path)` will delete the file at path.

	- Calling `os.rmdir(path)`will delete the folder at path. This folder must be empty of any files or folders.

	- Calling `shutil.rmtree(path)` will remove the folder at path, and all files and folders it contains will also be deleted.

#send2trash Module (pip install)

It will send folders and files to your computer’s trash or recycle bin instead of permanently deleting them.  Use the `send2trash.send2trash()` function to delete files and folders.

#Walking a directory tree

You can use `os.walk(path)` in a for loop statement to walk a directory tree, it will return three values on each iteration through the loop:

- foldername: A string of the current folder’s name

- subfolders: A list of strings of the folders in the current folder

- filenames: A list of strings of the files in the current folder

#zipfile Module

