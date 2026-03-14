import sqlite3
from config import DB_NAME

def store(coins):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "CREATE TABLE IF NOT EXISTS prices ("
        "id INTEGER PRIMARY KEY AUTOINCREMENT,"
        "name TEXT,"
        "symbol TEXT,"
        "price REAL,"
        "market_cap INTEGER,"
        "change_24h REAL,"
        "fetched_at TEXT)"
    )

    for coin in coins:
        cursor.execute(
            "INSERT INTO prices (name, symbol, price, market_cap, change_24h, fetched_at) "
            "VALUES (?, ?, ?, ?, ?, ?)",
            (coin["name"], coin["symbol"], coin["price"], coin["market_cap"], coin["change_24h"], coin["fetched_at"])
        )

    conn.commit()
    conn.close()
    print("Data saved to database!")

def query():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    print("\n--- All Prices ---")
    cursor.execute("SELECT name, symbol, price, change_24h, fetched_at FROM prices")
    rows = cursor.fetchall()
    for row in rows:
        print(f"{row[0]} ({row[1]}) — ${row[2]} | 24h: {row[3]}% | Fetched: {row[4]}")

    print("\n--- Biggest Gainer ---")
    cursor.execute("SELECT name, change_24h FROM prices ORDER BY change_24h DESC LIMIT 1")
    gainer = cursor.fetchone()
    print(f"{gainer[0]} — {gainer[1]}%")

    print("\n--- Biggest Loser ---")
    cursor.execute("SELECT name, change_24h FROM prices ORDER BY change_24h ASC LIMIT 1")
    loser = cursor.fetchone()
    print(f"{loser[0]} — {loser[1]}%")

    conn.close()