import logging

from Utils.VKHelper import helperInstance

logging.basicConfig(filename="jaba.log", level=logging.INFO)

log = logging.getLogger()


def error(error_str):
    helperInstance.write_msg(error_str)
    log.error(error_str)
