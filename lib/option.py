#!/usr/bin/env python

# Project :  rhc_smoke 
# Loc : /lib
# Function : read configure
# Author : cshi
# Date : 30.Dec.2014

import os

config = {}

class Config:
    
    def __init__(self):
        
        self.__config_path = '../config/express.conf'
        self.__list_path='../config/smoke.list'

    def read_config(self):
        
        global config
        file = open(self.__config_path,'r')
        for line in file :
            line = line.strip('\n')
            if not line.startswith("#") and not line.count('\n')==len(line) :
               config[line.split('=')[0]] = line.split('=')[1]
       
    def get(self,key):
       
        global config
        if key in config : 
            return config.get(key)
        else :
            return "" 
    
    def getConfig(self):
        
        global config
        return config

    def setup(self):
        
        self.read_config()
        return getConfig()

if __name__ == "__main__":
    
    cfg = Config()
    cfg.read_config()
    print cfg.get('default_rhlogin')
    print cfg.get('libra_server')
    print cfg.get('33')


