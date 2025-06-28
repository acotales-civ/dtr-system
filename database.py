from sqlite_database import SQLiteDatabase
from logger import Logger



# Global logger variable for logging database operations
logger = Logger(logger_name="SQL", console_output=False)


class DatabaseManager(SQLiteDatabase):
    def __init__(self, db_file: str, db_user: str):

        if not db_file or not db_user:
            raise ValueError("Database file and user must be provided.")

        super().__init__(db_file)
        self.user = db_user

        self.connect()

    def connect(self):
        try:
            super().connect()
            logger.info(f"user {self.user} connected to {self.file}")

        except Exception as e:
            logger.error(f"{self.user} failed to connect {self.file} | {e}")

    def disconnect(self):
        if self.connection is not None:
            super().disconnect()
            logger.info(f"user {self.user} disconnected to {self.file}")