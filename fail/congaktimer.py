from time import strftime

psec = int(strftime("%M"))
#print("psec = " + str(psec))

while True:
    csec = int(strftime("%M"))
    #print("csec = " + str(csec))

    dsec = csec - psec
    #print(dsec)
    
    if dsec ==2:
        print("2 min passed")
        psec=0
    #elif dsec ==9:
     #   print("something")
      #  psec = 0