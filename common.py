import os
import signal

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
