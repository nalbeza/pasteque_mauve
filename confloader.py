#!/usr/bin/python
import common, array

def loadconf(conf):
    if (common.exists("broxy.conf")):
        path = open('broxy.conf','r')
        lignes = path.readlines()
        for lig in lignes:
            sp = lig.split('#')[0]
            sp = sp.split('=')
            if len(sp[1]) > 1: conf[sp[0]] = sp[1].strip()
        path.close()

conf = {"pidfile":"broxy.pid", "port":"4242", "maxconnection":20, "logfile":"broxy.log"}
loadconf(conf)
