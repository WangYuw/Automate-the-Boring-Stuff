#! python3
# Multiclipboard.py : Saves and loads pieces of text to the clipboard.

'''
    The .pyw extension means that Python won’t show a Terminal window when it runs this program.
    
    The program does:
        The command line argument for the keyword is checked.
        If the argument is save, then the clipboard contents are saved to the keyword.
        If the argument is list, then all the keywords are copied to the clipboard.
        Otherwise, the text for the keyword is copied to the clipboard.
    
    The code will need to do the following:
        Read the command line arguments from sys.argv.
        Read and write to the clipboard.
        Save and load to a shelf file.
'''

'''
    Usage: 
        py.exe mcb.pyw (mcb) save <keyword> - Saves clipboard to keyword.
        py.exe mcb.pyw (mcb) <keyword> - Loads keyword to clipboard.
        py.exe mcb.pyw (mcb) list - Loads all keywords to clipboard.
'''
# 1. Shelf Setup
import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

# 2. Save clipboard content with a keyword
# shelve like a key-value database
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    # 3. List keywords and load a keyword’s content
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()