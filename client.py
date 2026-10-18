import requests

from models import Position


class ISSClient:
    URL = "https://api.wheretheiss.at/v1/satellites/25544"

    def fetch_position(self):
        response = requests.get(self.URL, timeout=20)
        response.raise_for_status()
        d = response.json()
        return Position(
            timestamp=d["timestamp"],
            latitude=d["latitude"],
            longitude=d["longitude"],
            altitude=d["altitude"],
            velocity=d["velocity"],
        )