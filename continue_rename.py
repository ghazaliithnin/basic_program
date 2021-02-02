import os

count=10
for filename in enumerate(os.listdir('bottles2_to_annotate')): # os.listdir('folder name')
    count = count + 1
    dst ="bottles_data" + str(count) + ".jpg"
    #print(dst)
    #print(filename +str(count) )
    src =  'bottles2_to_annotate/' + str(filename[1])
    dst = 'gamba_bottles2/' + dst

    print(src)
    print("Change to")
    print(dst)
    print("")
    os.rename(src,dst)

