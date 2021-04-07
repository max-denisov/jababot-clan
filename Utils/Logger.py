import logging

from control.VKHelper import helperInstance

logging.basicConfig(filemode="w", filename="jaba.log", level=logging.INFO)

log = logging.getLogger()


def error(error_str):
    helperInstance.write_msg(error_str)
    log.error(error_str)
