#! python3
# MapIt.py : Launch a map in the browser using an address from the command line or clipboard

'''
    This is what your program does:

        Gets a street address from the command line arguments or clipboard.
        Opens the web browser to the Google Maps page for the address.
    
    This means your code will need to do the following:
        Read the command line arguments from sys.argv.
        Read the clipboard contents.
        Call the webbrowser.open() function to open the web browser.
'''

import webbrowser, sys, pyperclip

if len(sys.argv)>1:
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

webbrowser.open('http://www.google.com/maps/places' + address)

'''
    As long as you have a URL, the webbrowser module lets users cut out the step of 
    opening the browser and directing themselves to a website.

        - Open all links on a page in separate browser tabs.
        - Open the browser to the URL for your local weather.
        - Open several social network sites that you regularly check.
'''