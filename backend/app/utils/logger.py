import logging

class CustomFormatter(logging.Formatter):
    """Custom logging formatter to add colors based on log level."""
    COLORS = {
        "CRITICAL": "\033[41m",  # Red background
        "ERROR": "\033[31m",    # Red
        "WARNING": "\033[33m",  # Yellow
        "DEBUG": "\033[34m",    # Blue
        "INFO": "\033[32m",     # Cyan
        "END": "\033[0m"        # Reset to default color
    }
    RESET = '\033[0m'

    def format(self, record):
        log_color = self.COLORS.get(record.levelname, self.RESET)
        record.levelname = f"{log_color}{record.levelname}{self.RESET}"
        # record.msg = f"{log_color}{record.msg}{self.RESET}"
        return super().format(record)

# Set up logger
logger = logging.getLogger(__name__)

# Prevent double logging
logger.propagate = False

# Clear existing handlers
if logger.hasHandlers():
    logger.handlers.clear()

# Add custom handler
handler = logging.StreamHandler()
handler.setFormatter(CustomFormatter('%(levelname)s:     %(message)s'))
logger.addHandler(handler)
