from datetime import datetime

class Logger:
    def log(self, level, msg):
        print(
            f"[{datetime.now()}] "
            f"{level}: {msg}"
        )

logger = Logger()
logger.log("INFO", "Server Started")
