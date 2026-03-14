# Crypto Data Pipeline

A lightweight data pipeline that fetches live cryptocurrency prices, transforms the data, and stores it in a local SQLite database.

## What it does
- Fetches the top 5 cryptocurrencies by market cap from the CoinGecko API
- Cleans and transforms the raw data
- Stores each snapshot in a SQLite database
- Queries the data to show the biggest gainer and loser

## Project Structure
- `pipeline.py` — main entry point, orchestrates the pipeline
- `transform.py` — cleans and formats the raw API data
- `database.py` — handles storing and querying the database
- `config.py` — stores configuration like the API URL and database name

## How to run
This project uses only Python built-in libraries — no installs needed.
```bash
python pipeline.py
```

Run it multiple times to build up a history of price snapshots over time.

## Technologies
- Python 3
- SQLite3
- CoinGecko API (no API key required)