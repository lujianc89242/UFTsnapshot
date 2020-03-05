import os
import shutil

# Create a folder named "snapshots_vbs" that contains result vbs files in current folder 
# Open folders with name "Action<a number>"
#   -Copy file named "Scipt.mts" and rename the copied file as "<current action name>.vbs"
#   -(optional)rename the copied file with the first line in mts file
#   -Save the copied file into "snapshots_vbs" folder
# Sanitizing the vbs file by deleting string start with @@ 

# detect the current working directory
rootdir = os.getcwd()
#print("current directory: %s" % path)
path = rootdir + "\\snapshots_vbs"
try:
    os.mkdir(path)
except OSError:
    print("**Creation of the directory %s failed, folder may already exists" % path)
    print("Deleting the snapshots_vbs folder....")
    shutil.rmtree(path)
    os.mkdir(path)
else:
    print("Successfully created the directory %s" % path)

# find all folders with name start with "Action"
actionNames = []
for subdir, dirs, files in os.walk(rootdir):
    for dir in dirs:
        if dir[:6] == "Action":
            actionNames.append(dir)

# copy the "Script.mts" file in each "Action" folder and put into destionation folder with a new name
for name in actionNames:
    src = rootdir + "\\" + name + "\\Script.mts"
    shutil.copy2(src,path)
    os.rename(path + "\\Script.mts", path + "\\" + str(name) + ".vbs")
    
