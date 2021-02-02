from time import strftime

psec = int(strftime("%S"))
#print("psec = " + str(psec))

while True:
    csec = int(strftime("%S"))
    #print("csec = " + str(csec))
    
    if csec == 10 or csec == 20:
        psec= csec
        print("psec = " + str(psec))
        dsec = csec - psec
        print("dsec = " + str(dsec))
        
        if dsec ==10:
            print("10 seconds passed")
            #csec=0
            psec = csec
        #elif dsec ==9:
         #   print("something")
          #  psec = 0