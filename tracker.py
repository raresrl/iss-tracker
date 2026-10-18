from client import ISSClient
from repository import PositionRepository

if __name__ == "__main__":
    client = ISSClient()
    repo = PositionRepository()

    position = client.fetch_position()
    repo.save(position)

    print("Saved:", position)
    print("Total readings:", repo.count())
    repo.close()