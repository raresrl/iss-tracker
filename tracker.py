import sqlite3
import requests

URL = "https://api.wheretheiss.at/v1/satellites/25544"
DB_FILE = "iss.db"


def init_db():
    conn = sqlite3.connect(DB_FILE)
    conn.execute(
        """CREATE TABLE IF NOT EXISTS positions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp INTEGER,
            latitude REAL,
            longitude REAL,
            altitude REAL,
            velocity REAL
        )"""
    )
    conn.commit()
    return conn


def fetch_position():
    response = requests.get(URL, timeout=20)
    response.raise_for_status()
    d = response.json()
    return (d["timestamp"], d["latitude"], d["longitude"], d["altitude"], d["velocity"])


def save_position(conn, position):
    conn.execute(
        "INSERT INTO positions (timestamp, latitude, longitude, altitude, velocity) "
        "VALUES (?, ?, ?, ?, ?)",
        position,
    )
    conn.commit()


def count_positions(conn):
    return conn.execute("SELECT COUNT(*) FROM positions").fetchone()[0]


if __name__ == "__main__":
    conn = init_db()
    position = fetch_position()
    save_position(conn, position)
    print("Saved:", position)
    print("Total readings:", count_positions(conn))
    conn.close()
