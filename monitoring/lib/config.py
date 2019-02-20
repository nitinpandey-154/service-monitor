class Config(object):
    # Logging Levels - DEBUG --> 10, INFO --> 20, WARN --> 30, ERROR --> 40
    ROOT_LOGGING_LEVEL = 10
    FILE_LOGGING_LEVEL = 10
    CONSOLE_LOGGING_LEVEL = 10

    # Formatters
    CONSOLE_FORMATTER = '%(asctime)s - %(levelname)s - %(message)s - %(funcName)s - %(module)s'
    FILE_FORMATTER = '%(asctime)s - %(levelname)s - %(message)s - %(funcName)s - %(module)s'
