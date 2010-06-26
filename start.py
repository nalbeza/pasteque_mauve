import os
import common
import sys
#TODO get fichier de config

#pidfile a mettre dans la conf
def start():
    if (common.exists("pid.broxy") == False 
        or os.path.getsize("pid.broxy") == 0):
        pid = os.fork()
        if (pid == 0):
            os.setsid()
            while (1):
                a = "a"
        else:
            open("pid.broxy", "w").write(str(pid))
        print "Daemon started"
    else:
        print >> sys.stderr, "Daemon is already running"
