import os

input_name=input("Name : ")

print("Registered Name: ",input_name)


try:
    os.mkdir(input_name)


except OSError:
    print("Creating of the directory %s failed or file name already existed "% input_name)

else:
    print("Successfully created the directory %s " % input_name)


