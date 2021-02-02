from time import strftime



while True:
    csec = int(strftime("%S"))
    #print("csec = " + str(csec))
    
    if csec == 10 or csec == 20 or csec == 30 or csec == 40 or csec ==50 or csec == 60:
        print("10 seconds has passed")
