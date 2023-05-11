import os
import re

def rename_file(directory, pattern, newname):
    files = os.listdir(directory)
    # counter for new file names, start at 1 for readability
    counter = 1
    for file in files:
        if re.match(pattern, file):
            # get the file extension, last '.' at end of file
            filetype = file.split('.')[-1]
            os.rename(directory + '/' + file, directory + '/' + newname + str(counter) + '.' + filetype)
            # print out newest file name
            print("Renaming " + file + " to " + newname + str(counter) + '.' + filetype)
            # increment counter for name
            counter += 1

# re is used for regex patterns
# ".*" means any character any number of times
# ".*.txt" means any character any number of times followed by .txt
# ".*[0-9].*" means including any number
rename_file(
    "C:\\Users\\kaide\\Visual Studio\\Bulk File Rename\\testing",
    ".*.txt",
    "myASDF")