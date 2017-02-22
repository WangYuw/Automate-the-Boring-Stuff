#! python3
# BulletPointAdder.py : Adds bullet points to the start of each line of text on the clipboard.

''' 
    This program will get the text from the clipboard, 
    add a star and space to the beginning of each line, 
    and then paste this new text to the clipboard. 
'''
# 1. Copy and paste from clipboard
import pyperclip
text = pyperclip.paste()

# 2. Separate lines and add stars
lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = '*' + ' ' + lines[i]

# 3. Join the lines
text = '\n'.join(lines)

pyperclip.copy(text)

'''
    you can want to automate some other kind of text manipulation, 
    such as:
        removing trailing spaces from the end of lines (strip(), lstrip(), rstrip())
        converting text to uppercase or lowercase (lower(), upper())
        justify text (rjust(), ljust(), center())
        ...
    Whatever your needs, you can use the clipboard for input and output.
'''
