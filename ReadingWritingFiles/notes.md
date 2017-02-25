#File Path

 1. `os.path.join()` function: If you pass it the string values of individual file and folder names in your path, `os.path.join() `will return a string with a file path using the correct path separators. 

	    >>> myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
    	>>> for filename in myFiles:
    	print(os.path.join('C:\\Users\\asweigart', filename))
    	C:\Users\asweigart\accounts.txt
    	C:\Users\asweigart\details.csv
    	C:\Users\asweigart\invite.docx

2. You can get the current working directory as a string value with the `os.getcwd()` function and change it with `os.chdir()`. 

3. Your programs can create new folders (directories) with the `os.makedirs()` function.

4. Handling absolute and relative paths

	- Calling `os.path.abspath(path)` will return a string of the absolute path of the argument. This is an easy way to **convert a relative path into an absolute one**.

	- Calling `os.path.isabs(path)` will return True if the argument is an absolute path and False if it is a relative path.
	
	- Calling `os.path.relpath(path, start)` will return a string of a relative path from the start path to path. If start is not provided, the current working directory is used as the start path. 

	- Calling `os.path.dirname(path)` will return a string of everything that comes before the last slash in the path argument. 
	
	- Calling `os.path.basename(path)` will return a string of everything that comes after the last slash in the path argument.
	
	- If you need a path’s dir name and base name together, you can just call `os.path.split(path)` to get a tuple value with these two strings.
		
		Also, note that `os.path.split()` does not take a file path and return a list of strings of each folder. For that, use the `split()` string method and split on the string in `os.sep`. 
		
		    >>> calcFilePath.split(os.path.sep)
    		['C:', 'Windows', 'System32', 'calc.exe']

5. Finding file sizes and folder contents

	- Calling `os.path.getsize(path)` will return the size in bytes of the file in the path argument.

	- Calling `os.listdir(path)` will return a list of filename strings for each file in the path argument. (Note that this function is in the `os` module, not `os.path`.)