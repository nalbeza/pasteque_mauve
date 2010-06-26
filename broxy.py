#!/usr/bin/python
# print "salut"
import os
import sys
import start
import stop

def main():
    if (len(sys.argv) == 2 and sys.argv[1] == "start"):
        start.start()
    elif (len(sys.argv) == 2 and sys.argv[1] == "restart"):
        start.start()
        
    elif (len(sys.argv) == 2 and sys.argv[1] == "stop"):
        if (stop.stop() == True):
            print "Daemon killed"   
        else:
            print >> sys.stderr, "Daemon wasn't running"
    else:
        print >> sys.stderr, "Va te faire foutre\n"

main()
