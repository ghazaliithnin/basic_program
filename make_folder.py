import os

path =("face2")


try:
    os.mkdir(path)


except OSError:
    print("Creating of the directory %s failed"% path)

else:
    print("Successfully created the directory %s " % path)


