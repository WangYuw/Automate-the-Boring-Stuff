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

1. Read zip file

	- To create a ZipFile object, call the `zipfile.ZipFile()` function, passing it a string of the `.zip` file’s filename. 

	- A ZipFile object has a `namelist()` method that returns a list of strings for all the files and folders contained in the ZIP file. 	
	
	- These strings can be passed to the `getinfo()` ZipFile method to return a ZipInfo object about that particular file. 
	
	- ZipInfo objects have their own attributes, such as `file_size` and `compress_size` in bytes, which hold integers of the original file size and compressed file size


			>>> exampleZip = zipfile.ZipFile('example.zip')
			>>> exampleZip.namelist()
			['spam.txt', 'cats/', 'cats/catnames.txt', 'cats/zophie.jpg']
			>>> spamInfo = exampleZip.getinfo('spam.txt')
			>>> spamInfo.file_size
			13908
			>>> spamInfo.compress_size
			3828
			>>> exempleZip.close()

2. Extract from zip file

	- The `extractall()` method for ZipFile objects extracts all the files and folders from a ZIP file into the current working directory.

	- you can pass a folder name to `extractall()` to have it extract the files into a folder other than the current working directory. If the folder passed to the `extractall()` method does not exist, it will be created.

	- The `extract(name, path)` method for ZipFile objects will extract a single file from the ZIP file. 

3. Create and add to zip files

	- To create your own compressed ZIP files, you must open the ZipFile object in write mode by passing `'w' / 'a'` as the second argument.

	- When you pass a path to the `write()` method of a ZipFile object, Python will compress the file at that path and add it into the ZIP file. The `write()` method’s first argument is a string of the filename to add. The second argument is the compression type parameter, which tells the computer what algorithm it should use to compress the files; you can always just set this value to `zipfile.ZIP_DEFLATED.`
	
		    >>> import zipfile
    		>>> newZip = zipfile.ZipFile('new.zip', 'w')
    		>>> newZip.write('spam.txt', compress_type=zipfile.ZIP_DEFLATED)
    		>>> newZip.close() 
