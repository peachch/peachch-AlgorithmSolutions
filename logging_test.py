import logging

def test_logging():
    # 设置日志打印的级别，如果不设置默认显示error及以上
    logging.basicConfig(level=logging.DEBUG)
    logging.debug("debug")
    logging.info("info")
    logging.error('Python Error')
    logging.critical('Python critical')

    HANDLER{}

test_logging()