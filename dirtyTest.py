#for test
from datetime import datetime
import time 
date1 = datetime.now()
time.sleep(3)
date2 = datetime.now()
d = date2-date1
d.total_seconds()
print(type(date2-date1))
