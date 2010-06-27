
# ajouter import sys

# log_message : localhost - - [26/Jun/2010 22:26:03] "GET http://www.3crowd.com/r/3c1px.gif HTTP/1.1" - -
    def log_message(self, format, *args):
        fd = open(conf["logfile"], 'a')
        fd.write("%s - - [%s] %s\n" %
                         (self.address_string(),
                          self.log_date_time_string(),
                          format%args))
        fd.close()
