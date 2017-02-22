#Module "pyperclip" (install)

The pyperclip module has copy() and paste() functions that can send text to and receive text from your computer’s clipboard.

	>>> import pyperclip
	>>> pyperclip.copy('Hello world!')
	>>> pyperclip.paste()
	'Hello world!'

if something outside of your program changes the clipboard contents, the `paste()` function will return it.

#Running programs

1. The first line of all your Python programs should be a shebang line: 
On Windows, the shebang line is `#! python3`.

2. Type like the following into the file editor and save the file as `\pw.bat` in a folder like `C:\pathBat`:

    	@py.exe C:\pathPy\PasswordLocker.py %*
    	@pause

3. The `C:\pathBat` folder should be added to the system path on Windows. To do this, modify the `PATH` environment variable.

4. With this batch file created, running the password-safe program on Windows is just a matter of pressing WIN-R and typing `pw <account name>`. ( `'pw'` here is the name of the `.bat` file )