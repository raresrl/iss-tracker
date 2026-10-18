import sqlite3

from models import Position


class PositionRepository:
    def __init__(self, db_file="iss.db"):
        # check_same_thread=False: FastAPI (step 3) runs requests on other threads
        self.conn = sqlite3.connect(db_file, check_same_thread=False)
        self._create_table()

    def _create_table(self):
        self.conn.execute(
            """CREATE TABLE IF NOT EXISTS positions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp INTEGER,
                latitude REAL,
                longitude REAL,
                altitude REAL,
                velocity REAL
            )"""
        )
        self.conn.commit()

    def save(self, position):
        self.conn.execute(
            "INSERT INTO positions (timestamp, latitude, longitude, altitude, velocity) "
            "VALUES (?, ?, ?, ?, ?)",
            (
                position.timestamp,
                position.latitude,
                position.longitude,
                position.altitude,
                position.velocity,
            ),
        )
        self.conn.commit()

    def count(self):
        return self.conn.execute("SELECT COUNT(*) FROM positions").fetchone()[0]

    def close(self):
        self.conn.close()