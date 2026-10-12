import requests

r= requests.get("https://api.wheretheiss.at/v1/satellites/25544")
print(r.json())