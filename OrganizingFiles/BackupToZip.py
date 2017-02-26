#! python3
# BackupToZip.py : Copies an entire folder and its contents into a ZIP file whose filename increments.

import zipfile, os
'''
    The function will determine what filename to use for the ZIP file it will create; 
    then the function will create the file, walk the folder folder, 
    and add each of the subfolders and files to the ZIP file. 
'''

def backupToZip(folder):
    # 1. Figure out the ZIP file’s name
    folder = os.path.abspath(folder)
    number = 1
    while 1:
        zipFilename = os.path.basename(folder) + '(' + str(number) + ').zip'
        if not os.path.exists(zipFilename):
            break
        number+=1
    # 2. Create new ZIP file
    print('Creating %s...' % (zipFilename))
    backupZip = zipfile.ZipFile(zipFilename, 'w')

    # 3. Walk the directory tree and add to the ZIP file
    for foldername, subfolders, filenames in os.walk(folder):
        print('Adding files in %s...' % (foldername))
        backupZip.write(foldername)

        for filename in filenames:
            if filename.startswith(os.path.basename(folder) + '(') and filename.endswith(').zip'):
                continue
            print('Adding files %s...' % (filename))
            backupZip.write(os.path.join(foldername, filename))
    backupZip.close()
    print('Done.')

backupToZip('C:\\Users\\yuwei\\Desktop\\Automate-the-Boring-Stuff')

'''
    You can walk a directory tree and add files to compressed ZIP archives:
        Walk a directory tree and archive just files with certain extensions, such as .txt or .py, and nothing else
        Walk a directory tree and archive every file except the .txt and .py ones
'''
