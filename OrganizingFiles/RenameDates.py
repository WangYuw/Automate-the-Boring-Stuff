#! python3
# RenameDates.py : Renames filenames with American MM-DD-YYYY date format to Chinese YYYY-MM-DD.

'''
    Here’s what the program does:

        It searches all the filenames in the current working directory for American-style or European-style dates.
        When one is found, it renames the file with the month and day swapped to make it Chinese-style.
    
    This means the code will need to do the following:
        
        Create a regex that can identify the text pattern of American-style dates.
        Call os.listdir() to find all the files in the working directory.
        Loop over each filename, using the regex to check whether it has a date.
        If it has a date, rename the file with shutil.move().
'''
import shutil, os ,re

 # 1. Create a Regex for American-Style Dates
dateAPattern = re.compile(r'''
        ^(.*?)                  # all text before the date (1)
        ((0|1)?\d)(-|/)         # one or two digits for the month (2(3))(4)
        ((0|1|2|3)?\d)(-|/)     # one or two digits for the day (5(6))(7)
        ((19|20)\d\d)           # for digits for the year (8(9))
        (.*?)$                  # all text after the date (10)
    ''', re.VERBOSE)

# 2. Identify the date parts from the filenames
for aFilename in os.listdir('.'):
    matched = dateAPattern.search(aFilename)
    # Skip files without a date
    if matched == None:
        continue
    # Get the different parts of the filename
    beforePart = matched.group(1)
    monthPart = matched.group(2)
    connectPart1 = matched.group(4)
    dayPart = matched.group(5)
    connectPart2 = matched.group(7)
    yearPart = matched.group(8)
    afterPart = matched.group(10)
# 3. Form the new filename and rename the files
    cnFilename = beforePart + yearPart + connectPart2 + monthPart + connectPart1 + dayPart + afterPart

    absWorkingDir = os.path.abspath('.')
    aFilename = os.path.join(absWorkingDir, aFilename)
    cnFilename = os.path.join(absWorkingDir, cnFilename)

    print('Renaming %s to %s ...' % (aFilename, cnFilename))
    #shutil.move(amerFilename, euroFilename)   # uncomment after testing

'''
    There are many other reasons why you might want to rename a large number of files.

        To add a prefix to the start of the filename, such as adding spam_ to rename eggs.txt to spam_eggs.txt
        To change filenames with European-style dates to Chinese-style dates
        To remove the zeros from files such as spam0042.txt
'''



