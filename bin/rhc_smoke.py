#!/usr/bin/env python

# Project : rhc_smoke
# Loc : /bin
# Author : cshi
# Date : 5.Jan.2015

import logging
import logging.config
import lib.config
import case


def main():
    # init log
    logging.config.fileConfig('config/log.conf')
    log = logging.getLogger('rhc_smoke')
    # init log & config
    cfg = lib.config.setup()
    # setup
    # lib.setup(cfg) to show the information include {account, password, env}
    # run case
    log.info('rhc smoke test starting...')

    for num in range(1, 18):
        c = eval('case.example%s.SmokeCase(%s)' % (num, cfg))
        c.test()

    log.info('rhc smoke test finish...')

# DEBUG
main()
