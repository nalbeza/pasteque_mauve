import os
import signal
import time

def exists(path):
   try:
      file(path)
      return True
   except:
      return False

def kill(pid):
    try:
       os.kill(pid, signal.SIGKILL)
       return True
    except:
       return False

def delete(path):
   try:
      os.remove(path)
      return True
   except:
      return False

def log(conf, msg):
   open(conf['logfile'], "aw").write(time.strftime('%d/%m/%y %H:%M:%S : ',time.localtime()) + msg + "\n")
      
