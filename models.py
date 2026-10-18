from dataclasses import dataclass


@dataclass
class Position:
    timestamp: int
    latitude: float
    longitude: float
    altitude: float
    velocity: float