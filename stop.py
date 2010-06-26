import os
import sys
import common


def stop():
    if (common.exists("pid.broxy") == True):
        if (common.kill(int(open("pid.broxy", "r").read())) == True):
            common.delete("pid.broxy")
            return True            
        common.delete("pid.broxy")
    return False
