import sqlite3

from logger import logger


class SQLite:
    def __init__(self, db_file):
        self.db_file = db_file
        self.conn = self.create_connection()
        self.table = """CREATE TABLE IF NOT EXISTS texts
                        (id INTEGER PRIMARY KEY AUTOINCREMENT, content TEXT)"""

    def create_connection(self):
        conn = None
        try:
            conn = sqlite3.connect(self.db_file)
            return conn
        except Exception as e:
            print(e)

        return conn

    def check_content_exists(self, content):
        c = self.conn.cursor()
        c.execute("SELECT * FROM texts WHERE content = ?", (content,))
        return c.fetchone() is not None

    def insert_content(self, content):
        c = self.conn.cursor()

        # 创建表
        if self.conn is not None:
            c = self.conn.cursor()
            c.execute(self.table)
            self.conn.commit()

        if not self.check_content_exists(content):
            sql = "INSERT INTO texts (content) VALUES (?)"
            c.execute(sql, (content,))
            self.conn.commit()
            logger.info(f"Inserted content: {sql}")

    def close_connection(self):
        if self.conn:
            self.conn.close()

    # 可选：使用析构函数（但请注意，它可能不会被调用）
    def __del__(self):
        self.close_connection()


if __name__ == "__main__":
    db_file = "./data/sqlite.db"
    db = SQLite(db_file)
    db.insert_content("test")
    print(db.check_content_exists("test"))
    db.close_connection()
