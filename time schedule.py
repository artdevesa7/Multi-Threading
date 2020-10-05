#You will have to install their Python library:

pip install schedule

#This is modified from their sample program:

import schedule
import time

def job(t):
    print "I'm working...", t
    return

schedule.every().day.at("01:00").do(job,'It is 01:00')

while True:
    schedule.run_pending()
    time.sleep(60) # wait one minute

#You will need to put your own function in place of job and run it with nohup, e.g.:

#nohup python2.7 MyScheduledProgram.py &
#Don't forget to start it again if you reboot.
