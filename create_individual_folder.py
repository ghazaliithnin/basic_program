import os

foldername="test"

list_foldername=os.listdir(foldername)
for index_list,elements in enumerate(list_foldername):
    filename_split=os.path.splitext(elements)
    filename=filename_split[0]
    #gabung=os.path.join(dir_name, elements) # ori
    gabung=os.path.join(foldername, filename)
    os.mkdir(gabung)
