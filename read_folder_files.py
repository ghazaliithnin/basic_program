from imutils import paths
import os

imagePaths = list(paths.list_images("guardian_test"))

# loop over the image paths
for (i, imagePath) in enumerate(imagePaths):
    boxes = []
    # extract the person name from the image path
    print("[INFO] processing image {}/{}".format(i + 1,
                                                  len(imagePaths)))
    name = imagePath.split(os.path.sep)[-2] # Folder Name
    fileName = imagePath.split(os.path.sep)[-1]
    print("Folder Name = " + name)
    print("File Name = " + fileName)
    
