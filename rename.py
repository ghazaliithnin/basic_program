import os


for count, filename in enumerate(os.listdir('bottles_to_annotate')): # os.listdir('folder name')
    dst ="bottles_data" + str(count) + ".jpg"
    #print(dst)
    #print(filename +str(count) )
    src =  'bottles_to_annotate/' + filename
    dst = 'bottles_to_annotate/' + dst

    print(src)
    #os.rename(src,dst)

