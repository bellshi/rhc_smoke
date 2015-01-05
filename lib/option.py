#!/usr/bin/env python

# Project :  rhc_smoke 
# Loc : /lib
# Author : cshi
# Date : 30.Dec.2014


class config:
    
    cfg = {}

    def __init__(self):
        
        self.__config_path = '../config/express.conf'
        self.__list_path='../config/smoke.list'

    def read_config(self):
        
        file = open(self.__config_path,'r')
        for line in file :
            line = line.strip('\n')
            if not line.startswith("#") and not line.count('\n')==len(line) :
              self.cfg[line.split('=')[0]] = line.split('=')[1]
       
    def get(self,key):
       
        if key in self.cfg : 
            return self.cfg.get(key)
        else :
            return "" 
    
    def getConfig(self):
        
        return self.cfg

    def setup(self):
        
        self.read_config()
        return self.getConfig()

#DEBUG
if __name__ == "__main__":
    
    c = config()
    #print cfg.get('default_rhlogin')
    #print cfg.get('libra_server')
    #print cfg.get('33')
    print c.setup()

