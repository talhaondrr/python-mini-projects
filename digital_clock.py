from datetime import datetime
import time

while True:
    simdi = datetime.now()

    print(simdi.strftime("%H:%M:%S"))

    time.sleep(1)