import common


def loadconf(conf):
    if (common.exists("broxy.conf")):
        path = open('broxy.conf','rb')
        lignes = path.readlines()
        for lig in lignes: 
            sp = lig.split('#')[0]
            sp = sp.split('=')
            if len(sp)==2: conf[sp[0].strip()]=sp[1].strip()
        path.close()
    else:
        conf["pidfile"] = "broxy.pid"
        conf["port"] = "1337"
        conf["maxconnection"] = 20
        conf["logfile"] = "broxy.log"
