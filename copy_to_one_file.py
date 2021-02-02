from imutils import paths
import os
from shutil import copyfile



root_folder="gamba_tesst"
dst_folder = "test_copyfile"


# loop over the image paths

for path, subdirs, files in os.walk(root_folder):
    for name in files:
        src=os.path.join(path, name)
        #print (os.path.join(path, name))
        #print(src)
        
        #src= root_folder +"/"+name+ "/"+fileName
        dst= dst_folder +"/"+name
        print("source = "+ src)
        print("copy to")
        print("destination = "+dst)
        print("")
        copyfile(src,dst)

    
