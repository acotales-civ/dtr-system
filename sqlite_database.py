import sqlite3



class SQLiteDatabase:
    def __init__(self, database_file: str):
        self.file = database_file
        self.connection = None
    
    def connect(self):
        try:
            self.connection = sqlite3.connect(self.file)
            self.connection.row_factory = sqlite3.Row

            # Log information successful database connection
            print(f"[INFO] Database connection established.")

        except Exception as e:
            # Log information unsuccessful database connection
            print(f"[ERROR] ConnectError: {e}")
            raise

    def disconnect(self):
        if isinstance(self.connection, sqlite3.Connection):
            self.connection.close()
            self.connection = None
            # Log information of database closing or disconnection
            print("[INFO] Database disconnected and closed.")

    def execute_query(self, query: str, params: dict, fetchall: bool = False):
        if isinstance(self.connection, sqlite3.Connection):
            if not params or not isinstance(params, dict):
                params = {}
            try:
                with self.connection as connection:
                    cursor = connection.cursor()
                    cursor.execute(query, params)

                    # Log for successful database query operation
                    print("[INFO] Query operation: OK")

                    # Auto-detect based on query type
                    operation = query.strip().split()[0].upper()
                    if operation in ["INSERT", "DELETE", "UPDATE"]:
                        return cursor.rowcount > 0

                    return cursor.fetchall() if fetchall else cursor.fetchone()

            except Exception as e:
                # Log for unsuccessful database query operation
                print(f"[ERROR] QueryError: {e}")
                raise

        return None

    # Context manager methods
    def __enter__(self):
        """Enter the context manager - establish database connection"""
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Exit the context manager - clean up database connection"""
        self.disconnect()
        # Return None (or False) to propagate any exceptions that occured
        return None

