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
            logger.info(f"User {self.user} connected to {self.file}")

        except Exception as e:
            logger.error(f"{self.user} failed to connect: {e}")

    def disconnect(self):
        if self.connection is not None:
            super().disconnect()
            logger.info(f"User {self.user} disconnected to {self.file}")

    def execute_query(self, query: str, params: dict, fetchall: bool = False):
        if self.connection is not None:
            try:
                return super().execute_query(query, params, fetchall)

            except Exception as e:
                logger.error(f"SQL Error: {e}")
        else:
            logger.info("Query Error: No connected database.")