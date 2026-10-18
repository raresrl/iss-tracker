# iss-tracker

A small Python project that fetches the current position of the international space station from a public API, saves each reading in a SQLite database, and prints how many readings are stored.
The way it works:
models.py: Position class-one ISS reading
client.py: ISSClient class-calls the API
repository.py: PositionRepository class-saves and counts readings in SQLite
tracker.py: runs everything

HOW TO RUN:
pip install -r requirements.txt

python tracker.py


Run it several times: Total readings grows each time because the data is stored in the database iss.db.
Next step:
Add a FastAPI layer to fetch a new reading and list the saved historyand better error handling.
