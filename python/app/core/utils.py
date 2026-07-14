from datetime import datetime


class Logger:

    @staticmethod
    def info(msg):
        print(f"[{datetime.now():%H:%M:%S}] INFO  {msg}")

    @staticmethod
    def success(msg):
        print(f"[{datetime.now():%H:%M:%S}] OK    {msg}")

    @staticmethod
    def error(msg):
        print(f"[{datetime.now():%H:%M:%S}] ERRO  {msg}")

    @staticmethod
    def warning(msg):
        print(f"[{datetime.now():%H:%M:%S}] WARN  {msg}")