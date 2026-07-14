from datetime import datetime


class Logger:

    @staticmethod
    def _print(level, msg):

        print(f"[{datetime.now():%Y-%m-%d %H:%M:%S}] [{level}] {msg}")

    @staticmethod
    def info(msg):
        Logger._print("INFO", msg)

    @staticmethod
    def success(msg):
        Logger._print("OK", msg)

    @staticmethod
    def warning(msg):
        Logger._print("WARN", msg)

    @staticmethod
    def error(msg):
        Logger._print("ERROR", msg)