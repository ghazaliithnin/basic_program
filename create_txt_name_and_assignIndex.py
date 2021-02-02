import os

# file1 = open("bottle_names.txt","w")

# for index,filename in enumerate(os.listdir('guardian_sorted')): # os.listdir('folder name')
#     print(filename)
#     file1.writelines(filename+"\n")

# file1.close()

###############################################################
###############

file1 = open("bottle_names.txt","r")

labels=file1.read().split("\n")

for index,filename in enumerate(os.listdir('guardian_sorted')): # os.listdir('folder name')
    print(str(index) + " == " + labels[index])

# labels[index] is to assign index according to order of the names in bottle_names.txt
#############
#####
### Tak jadi
# for name in labels:
#     print(name)
###



##############################################################