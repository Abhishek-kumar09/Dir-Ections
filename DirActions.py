import os
import shutil

print ("welcome in File Handling Wizard!!")
print ("You can delete all the files with the certain extension e.g. .mp4")

path = os.getcwd()
print (f'You are inside the Directory {path}')

print ("Use this directory as the working-directory! | Y or N |")
choice1 = input()

if (choice1 == 'y' or choice1 == 'Y'):
    print ("Path selected!")
else:
    print ("Enter the full path of parent-folder in which the extension is to be searched ")
    path = input()

print ("Enter your file extension to delete!!")
print ("Format: e.g. \".txt\", \".mp4\" ")
extension = input()

# Declaring a list that would hold our files to work on.
Files = []
folderName = path

# Traverse tree to check each file for the given file type
def traversetree(path):
    global folderName
    if (type(path) == str):
        if (path.startswith('/')):
            folderName = path
        if (path.endswith(extension)):
            Files.append(folderName +"/"+ path)        

    if (type(path) == list):
        for r in path:
            traversetree(r)
    

noSuchDirectory = True

if (type(extension) == str and type(path) == str):
    for files in os.walk(path):
        noSuchDirectory = False
        for file in files:
            traversetree(file)

# The affected files
for file in Files:
    os.remove(file)    

if (noSuchDirectory):
    print ("Wrong Path Provided: No such File or Directory!!")
