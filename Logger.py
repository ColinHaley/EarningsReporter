class Logger(object):
    def __init__(self, logger, level):
        """ Requires logger and a level """
        self.logger = logger
        self.level = level

    def write(self, message):
        # only log for real stuff, not None
        if message.rstrip() != "":
            self.logger.log(self.level, message.rstrip())