from os import path, environ, makedirs
import logging

class Logger(object):
    """This class logs to console / file or both.
    About the log structure
    -----------------------
    `write` is a usefull attribute to set up a quick all-time-log.
    This log mode writes to your terminal but also to a `.log` file.
    This means whenever your code breaks the logs are still available to you
    on your machine. The location of this file depends on where you installed
    the `codewars` package. For a virtualenv environment usually this will be
    `venv/lib/python3.*/site-packages/codewars*/codewars/logger/logs/appname.log`
    
    What does `write` actually write?
        - DEBUG
        - INFO
        - WARNING
        - ERROR
        - CRITICAL

    Note
    ----
    Write is the only mode that actually 

    The rest of the documentation page will provide more information.

    """

    def __createLogFolder(self):
        """Triggers when class gets initialized.
        Note
        ----
        This function should never be called outside the Log class itself.
        """
        directory=path.join(path.dirname(path.abspath(__file__)), 'logs')
        makedirs(str(directory), mode=0o777, exist_ok=True)
    
    def __init__(self, appname: str = "Application", mode: str = "DEBUG", write: bool = False):
        """When initializing you can choose a appname and the log level.

        Parameters
        ----------
        appname
            Default: 'Application'
            Type: String
            Description: The name the logger will show
        
        mode
            Default 'DEBUG'
            Type: String
            Choices: ['DEBUG', 'WARNING', 'INFO']
            Decription: Set a logging level.
                DEBUG: logs basically everything
                WARNING: logs only warnings and worse
                INFO: log info and worse

        write
            Default: False
            Type: bool
            Description: Write logs to log file.
        
        Note
        ----
        Log files are created with the appname. Depending on the appname the log
        will be created in the rootfolder of the codewars package. Only if
        `write` is turned on. if `write` is True it creates a 'logs' folder.
        """
        if write: self.__createLogFolder()  # Create log folder if not exists
        self.__appname = appname  # Set the app name
        # Figure out what the log level should be
        if mode.lower() == 'debug': self.__level = logging.DEBUG
        elif mode.lower() == 'warning': self.__level = logging.WARNING
        elif mode.lower() == 'info': self.__level = logging.INFO
        else: raise AttributeError("Logging level is not set.")
        if write: # If write to file is turned on
            # Create the logger
            logging.basicConfig(
                level=self.__level,
                format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                datefmt='%m-%d %H:%M',
                filename=path.join(path.join(path.dirname(path.abspath(__file__)), 'logs'), f'{self.__appname}.log'),
                filemode='w'
            )
        else:
            logging.basicConfig(
                level=self.__level,
                format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                datefmt='%m-%d %H:%M'
            )

        # Create the logger
        self.__logger = logging.getLogger(self.__appname)

        if write:  # also redirect to console
            console = logging.StreamHandler()
            console.setLevel(self.__level)
            formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
            console.setFormatter(formatter)
            self.__logger.addHandler(console)

    def __repr__(self):
        """Shows information when the class is called in a print statement"""
        return f"Codewars Logger {self.__appname}"

    def debug(self, msg):
        """Logs a message on DEBUG level."""
        return self.__logger.debug(str(msg))
    
    def info(self, msg):
        """Logs a message on INFO level."""
        return self.__logger.info(str(msg))
    
    def warning(self, msg):
        """Logs a message on WARNING level."""
        return self.__logger.warning(str(msg))
    
    def error(self, msg):
        """Logs a message on ERROR level."""
        return self.__logger.error(str(msg))
    
    def critical(self, msg):
        """Logs a message on CRITICAL level."""
        return self.__logger.critical(str(msg))

    def _testLoggerClass(self):
        """Invoke all class functions"""
        self.debug('debug message')
        self.info('info message')
        self.warning('warn message')
        self.error('error message')
        self.critical('critical message')
