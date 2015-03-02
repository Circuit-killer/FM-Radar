import serial
import sys
import time
from datetime import datetime

def get_epoch_seconds():
    now = datetime.utcnow()
    return (now - datetime(1970,1,1)).total_seconds()

fname = sys.argv[1]
f = open(fname,'a')
s = serial.Serial(sys.argv[2], 9600)

while True:
    if s.inWaiting() > 1:
        f = open(fname,'a')
        line = s.readline()
        f.write(str(get_epoch_seconds()))
        f.write(",")
        f.write(line)
        print "Logged: ", datetime.utcnow().strftime("%B %d, %Y - %H:%M:%S")
        f.close()
    else:
        # Sleep to save system resources
        time.sleep(10)

s.close()
