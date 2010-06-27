import os
import sys
import common


def stop(conf):
    if (common.exists(conf['pidfile']) == True):
        if (common.kill(int(open(conf['pidfile'], "r").read())) == True):
            common.delete(conf['pidfile'])
            return True            
        common.delete(conf['pidfile'])
    return False
