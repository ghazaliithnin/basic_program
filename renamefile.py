import os


for count, filename in enumerate(os.listdir('glovemaskhat_to_annotate')): # os.listdir('folder name')
    dst ="hatdata" + str(count) + ".jpg"
    #print(dst)
    #print(filename +str(count) )
    src =  'glovemaskhat_to_annotate/' + filename
    dst = 'glovemaskhat_to_annotate/' + dst

    print(src)
    os.rename(src,dst)

#os.rename()