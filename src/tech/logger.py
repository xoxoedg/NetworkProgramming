import logging
from typing import Any


class Logger:
    def __init__(self, module_name: str, filename: str = "server.log"):
        self.module_name: str = module_name
        self.filename: str = filename
        self.logger: logging.Logger = logging.getLogger(self.module_name)
        self.logger.setLevel(logging.INFO)

        stream_handler: logging.StreamHandler[Any] = logging.StreamHandler()
        stream_handler.setLevel(logging.INFO)

        file_handler: logging.FileHandler = logging.FileHandler(self.filename)
        file_handler.setLevel(logging.INFO)

        formatter: logging.Formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"
        )

        stream_handler.setFormatter(formatter)
        file_handler.setFormatter(formatter)

        self.logger.addHandler(stream_handler)
        self.logger.addHandler(file_handler)

    def get_logger(self) -> logging.Logger:
        return self.logger
