import logging


class Logger:
    def __init__(self, module_name, filename="server.log"):
        self.module_name = module_name
        self.filename = filename
        self.logger = logging.getLogger(self.module_name)
        self.logger.setLevel(logging.INFO)
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.INFO)
        file_handler = logging.FileHandler(self.filename)
        file_handler.setLevel(logging.INFO)

        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        stream_handler.setFormatter(formatter)
        file_handler.setFormatter(formatter)

        self.logger.addHandler(stream_handler)
        self.logger.addHandler(file_handler)

    def get_logger(self)-> logging.Logger:
        return self.logger
