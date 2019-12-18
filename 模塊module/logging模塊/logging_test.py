import logging

# -----------------------------------logging.basicConfig
# logging.basicConfig(
#     level=logging.DEBUG,
#     filename="logger.log",
#     filemode="w",
#     format="%(asctime)s %(filename)s[%(lineno)d]  %(message)s"
#
#
# )
#
# logging.debug('hello')
# logging.info('hello')
# logging.warning('warning message')
# logging.error('error message')
# logging.critical('critical message')

# -----------------------------------logger
# def logger():
#     logger=logging.getLogger()
#
#
#     fh=logging.FileHandler("test_log")
#     #ch=logging.StreamHandler()
#
#     fm=logging.Formatter("%(asctime)s  %(message)s")
#
#     fh.setFormatter(fm)
#     #ch.setFormatter(fm)
#
#     logger.addHandler(fh)
#     #logger.addHandler(ch)
#     logger.setLevel("DEBUG")
#
#     return logger
# #----------------------
# logger=logger()
#
# logger.debug("debug")
# logger.info("info")
# logger.warning("warning")
# logger.error("error")
# logger.critical("critical")
# --------------------------------------------------
import logging

logger = logging.getLogger()

logger1 = logging.getLogger('mylogger')
logger1.setLevel(logging.DEBUG)

# logger2 = logging.getLogger('mylogger')
# logger2.setLevel(logging.WARNING)


fh = logging.FileHandler("test_log-new")
ch = logging.StreamHandler()

# logger.addHandler(ch)
# logger.addHandler(fh)

logger1.addHandler(fh)
logger1.addHandler(ch)

# logger2.addHandler(fh)
# logger2.addHandler(ch)


# logger.debug('logger debug message')
# logger.info('logger info message')
# logger.warning('logger warning message')
# logger.error('logger error message')
# logger.critical('logger critical message')

# logger1.debug('logger1 debug message')
# logger1.info('logger1 info message')
# logger1.warning('logger1 warning message')
# logger1.error('logger1 error message')
# logger1.critical('logger1 critical message')

# logger2.debug('logger2 debug message')
# logger2.info('logger2 info message')
# logger2.warning('logger2 warning message')
# logger2.error('logger2 error message')
# logger2.critical('logger2 critical message')
