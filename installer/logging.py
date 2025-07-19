import logging
import os


class ColouredLoggingFormatter(logging.Formatter):
    # ANSI color codes
    BLUE_UNDERLINE = "\x1b[4;34m"
    GREEN = "\x1b[32;21m"
    YELLOW = "\x1b[33;21m"
    RED = "\x1b[31;21m"
    BOLD_RED = "\x1b[31;1m"
    RESET = "\x1b[0m"

    LEVEL_COLORS = {
        logging.DEBUG: BLUE_UNDERLINE,
        logging.INFO: GREEN,
        logging.WARNING: YELLOW,
        logging.ERROR: RED,
        logging.CRITICAL: BOLD_RED,
    }

    def format(self, record):
        levelname = record.levelname
        color = self.LEVEL_COLORS.get(record.levelno, self.RESET)
        record.levelname = f"{color}{levelname}{self.RESET}"
        return super().format(record)


def make_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    log_level_str = os.environ.get("DOTFILES_LOG_LEVEL", "INFO")
    log_level = logging.getLevelNamesMapping().get(log_level_str, logging.INFO)
    logger.setLevel(log_level)
    ch = logging.StreamHandler()
    ch.setLevel(log_level)
    formatter = ColouredLoggingFormatter("%(levelname)s: %(message)s")
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return logger
