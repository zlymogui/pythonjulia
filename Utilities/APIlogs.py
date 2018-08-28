#!/usr/bin/python
# -*- coding: UTF-8 -*-

import logging
import logging.handlers
import time

def logs(APIName):
    logger = logging.getLogger(__name__)
    logging.basicConfig(level=logging.INFO)
    handler = logging.FileHandler("log" + str(APIName)+ str(time.strftime("%Y%m%d%H%M%S", time.localtime())) + ".txt")
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger

#logger=logs()
#logger.info("hsfshfksflsdfsdf")