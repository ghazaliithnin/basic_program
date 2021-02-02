import os

count = 0

filelist = os.listdir("ayu2")
filelist = sorted(filelist)

#for filename in os.listdir("ayu2"):
for filename in filelist:
  #dst = "ayu_nospek" + str(count) +".jpg"
  #src = 'ayu2' + filename
  src = filename
  #src = sorted(src)
  #print(src)
  #dst = 'ayu2' + filename
  dst = "ayu_nospek" + str(count) +".jpg"
  #print(dst)
  
  os.rename(src,dst)
  count = count + 1
