#!/usr/bin/python
import os
import sys
import start
import stop
import confloader
import common

def main():
    conf={}
    confloader.loadconf(conf)
    if (len(sys.argv) == 2 and sys.argv[1] == "start"):
        start.start(conf)
    elif (len(sys.argv) == 2 and sys.argv[1] == "restart"):
        if (stop.stop(conf) == True):
            common.log(conf, "Daemon stopped")
            print "Daemon stopped"
        start.start(conf)    
    elif (len(sys.argv) == 2 and sys.argv[1] == "stop"):
        if (stop.stop(conf) == True):
            common.log(conf, "Daemon stopped")
            print "Daemon stopped"
        else:
            print >> sys.stderr, "Daemon isn't started"
    else:
        print >> sys.stderr, "Va te faire foutre\n"

main()
