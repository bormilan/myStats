import logging

PRODUCTION = False
REMOTE = True

LOG_PATH = (
    ""
    if PRODUCTION
    else ("api_log.log" if REMOTE else "")
)

CONNECTION_STRING = "mongodb+srv://admin:piSziRA2rlOn8i7T@cluster0.gyzgk2x.mongodb.net/"

_logger = logging.Logger("ms-logger", level=logging.DEBUG)
_fh = logging.FileHandler(LOG_PATH)
_fh.setFormatter(
    logging.Formatter(
        fmt="%(asctime)s | %(name)s | %(levelname)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
)
_fh.setLevel(logging.INFO)
_logger.addHandler(_fh)


class Logger:
    def debug(msg: str):
        _logger.debug(msg)

    def info(msg: str):
        _logger.info(msg)

    def warning(msg: str):
        _logger.warning(msg)

    def error(msg: str):
        _logger.error(msg)