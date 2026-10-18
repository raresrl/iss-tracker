from models import Position
from repository import PositionRepository

if __name__ == "__main__":
    repo = PositionRepository("test.db")
    fake = Position(timestamp=1, latitude=15.0, longitude=22.30, altitude=4.0, velocity=5.0)

    print("Latitude:", fake.latitude)
    repo.save(fake)
    print("Total readings:", repo.count())
    repo.close()
