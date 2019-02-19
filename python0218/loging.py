import  logging
# logging.basicConfig(level=logging.DEBUG,format='%(levelname)s - %(name)s - %(message)s-  %(filename)s')
# logging.debug('this is debug')
# logging.info('this is info message')
# logging.warning('this is warning')


logger=logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)
handler=logging.FileHandler("log.text")
handler.setLevel(logging.INFO)
fromat=logging.basicConfig(level=logging.DEBUG,fromat='%(levelname)s - %(name)s - %(message)s-  %(filename)s')
handler.setFormatter(fromat)

logger.info("startlog")
logger.debug("do buag")
logger.warning("this is warning")
