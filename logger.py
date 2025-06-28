import os
import logging


class Logger:
	"""A simple logger class for easy logging setup and usage."""

	def __init__(self,
				 logger_name: str = "Default",
				 log_level: str = "INFO",
				 log_file: str = "logs\\info.log",
				 console_output: bool = True):
		"""
		Initialize the simple logger.

		Args:
			logger_name: Logger name
			log_level: Log level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
			log_file: Path to log file
		"""
		self.logger_name = logger_name
		self.log_level = log_level.upper()
		self.log_file = log_file
		self.console_output = console_output
		self.logger = self.setup_logger()

	def setup_logger(self):
		"""Set up and configure the logger."""

		# Create logs directory if it doesn't exist
		log_dir = os.path.dirname(self.log_file)
		if log_dir and not os.path.exists(log_dir):
			os.makedirs(log_dir)

		# Create logger
		logger = logging.getLogger(self.logger_name)
		logger.setLevel(getattr(logging, self.log_level))

		# Avoid duplicate handlers
		if logger.handlers:
			return logger

		# Create formatter
		formatter = logging.Formatter(
			'%(asctime)s - %(name)s - %(levelname)s - %(message)s',
			datefmt='%Y-%m-%d %H:%M:%S'
		)

		# File handler
		file_handler = logging.FileHandler(self.log_file)
		file_handler.setFormatter(formatter)
		logger.addHandler(file_handler)

		# Console handler
		if self.console_output:
			console_handler = logging.StreamHandler()
			console_handler.setFormatter(formatter)
			logger.addHandler(console_handler)

		return logger

	def debug(self, message):
		"""Log debug message."""
		self.logger.debug(message)

	def info(self, message):
		"""Log info message."""
		self.logger.info(message)

	def warning(self, message):
		"""Log warning message."""
		self.logger.warning(message)

	def error(self, message):
		"""Log error message."""
		self.logger.error(message)

	def critical(self, message):
		"""Log critical message."""
		self.logger.critical(message)

	def get_logger(self):
		"""Return the underlying logger instance."""
		return self.logger

