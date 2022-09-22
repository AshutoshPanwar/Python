import os

for folderName, subFolders, filenames in os.walk('/Users/iamashu/Workdir/Python/Automating_Boring_Stuff_with_python/test'):     # Enter path of you folder in which you want to see tree structure.
    print("The current folder is " + folderName)        # Current folder path

    for subFolder in subFolders:
        print("SubFolder of " + folderName + ': ' + subFolder)      # All sub folder name
    for filename in filenames:
        print('File Inside ' + folderName + ': ' + filename)        # All file name
    print('')