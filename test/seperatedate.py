from datetime import datetime
from datetime import date

mdatetime = datetime.ctime(datetime.now())

hour = mdatetime.split(" ")[-2]
mdate = datetime.date(datetime.now())
cdate = mdate

