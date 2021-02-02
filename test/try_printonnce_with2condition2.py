from datetime import datetime
from datetime import date
import time

name = "Adib"
pname=""
ptime=""
while True:
    cstate_name=name
    pstate_name=cstate_name

    cstate_time = str(time.strftime("%S-%M-%H"))

    if cstate_name!=pname or  cstate_time!=ptime:
        print(name + "--" + str(time.strftime("%S-%M-%H")))
    pname = cstate_name
    ptime = cstate_time
###############################

##    if cstate!=pname:
##
##        print(name)
##
##    pname=cstate
##############
##    if cstate_time!=ptime:
##
##        print(name)
##
##    ptime=cstate_time
##########