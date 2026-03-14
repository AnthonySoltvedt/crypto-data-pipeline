import urllib.request
import json
print("importing config...")
from config import COINS_URL
print("importing transform...")
from transform import transform
print("importing database...")
from database import store, query

try:
    with urllib.request.urlopen(COINS_URL) as response:
        data = json.loads(response.read())
except Exception as e:
    print(f"Failed to fetch data: {e}")
    exit()

coins = transform(data)
store(coins)
query()
