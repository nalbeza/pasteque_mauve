import os
import common
import sys
import socket

def client(conn, addr, conf):
    print "client connected from " + str(addr)
    common.log(conf, "client connected from " + str(addr))
    while (1):
        data = conn.recv(4096) # more than the maximum length of an URL/http request
        if not data: break
        print str(addr) + " : request " + data
        conn.send("Salut LOL")
    conn.close()
    print "client on " + str(addr) + "disconnected"
    common.log(conf, "client on " + str(addr) + "disconnected")

def start(conf):
    if (common.exists(conf['pidfile']) == False 
        or os.path.getsize(conf['pidfile']) == 0):
        pid = os.fork()
        if (pid == 0):
            os.setsid()
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.bind(('', int(conf['port'])))
            s.listen(int(conf['maxconnection']))
            while (1):
                conn, addr = s.accept()
                if (os.fork() == 0):
                    client(conn, addr, conf)
        else:
            open(conf['pidfile'], "w").write(str(pid))
        print "Daemon started"
        common.log(conf, "Daemon started")
    else:
        print >> sys.stderr, "Daemon is already running"
