#! python3
#EmailExtractor.py : Finds email addresses on the clipboard.

'''
    your phone and email address extractor will need to do the following:

    1. Get the text off the clipboard.
    2. Find all email addresses in the text.
    3. Paste them onto the clipboard.
'''
# 1. Create a regex for email
import re
mailRegex = re.compile(r'''(
        [\w.%+-]+           #username
        @                   #symbole@
        [\w.-]+             #domain name
        (\.[a-zA-Z]{2,4})   #.com,.eu,... 
    )''', re.VERBOSE)

# 2. Find all matched in the clipboard
import pyperclip
text = pyperclip.paste()
matches = []
for groups in mailRegex.findall(text):
    matches.append(groups[0])

# 3. Join the matches into a String to the clipboard
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard: '+ '\n'.join(matches))
else:
    print('No email address found.')

'''
    Identifying patterns of text 
    (and possibly substituting them with the sub() method):

        Find website URLs that begin with http:// or https://.
        Clean up dates in different date formats by replacing them with dates in a single, standard format.
        Remove sensitive information such as Social Security or credit card numbers.
        Find common typos such as multiple spaces between words, accidentally repeated words, 
            or multiple exclamation marks at the end of sentences.
'''