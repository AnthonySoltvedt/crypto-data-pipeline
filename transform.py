from datetime import datetime

def transform(coins):
    transformed = []
    for coin in coins:
        transformed.append({
            "name": coin["name"],
            "symbol": coin["symbol"].upper(),
            "price": round(coin["current_price"], 2),
            "market_cap": coin["market_cap"],
            "change_24h": round(coin["price_change_percentage_24h"], 2),
            "fetched_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
    return transformed