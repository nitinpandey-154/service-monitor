import logging
import datetime
import os


class Logger(object):
    def __init__(self, properties):
        self.properties = properties

    def get_stream_handler(self):
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(self.properties.CONSOLE_LOGGING_LEVEL)
        stream_handler.setFormatter(logging.Formatter(
            self.properties.CONSOLE_FORMATTER))
        return stream_handler

    def get_file_handler(self):
        file_name = datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
        file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../log', file_name)
        file_handler = logging.FileHandler(filename=file_path)
        file_handler.setLevel(self.properties.FILE_LOGGING_LEVEL)
        file_handler.setFormatter(logging.Formatter(
            self.properties.FILE_FORMATTER))
        return file_handler

    def get_logger(self, logger_name="service-monitor"):
        logger = logging.getLogger(logger_name)
        logger.setLevel(self.properties.ROOT_LOGGING_LEVEL)
        logger.addHandler(self.get_stream_handler())
        logger.addHandler(self.get_file_handler())
        return logger

