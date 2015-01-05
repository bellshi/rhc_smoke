#!/usr/bin/env python

# Project : rhc_smoke
# Loc : /bin
# Author : cshi
# Date : 5.Jan.2015

import logging
import logging.config
import sys
sys.path.append('../lib')
from option import *
from setup import *


def main():

    logging.config.fileConfig('../config/log.conf')
    log = logging.getLogger('rhc_smoke')
    # init log & config
    cfg = config().setup()
    # setup
    init(cfg).setup()
    # run case
    log.info('rhc smoke test starting...')






#DEBUG
main()
