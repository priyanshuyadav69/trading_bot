# Binance Futures Testnet Trading Bot

## Setup

1 Install dependencies

pip install -r requirements.txt

2 Add API keys

Create .env file

BINANCE_API_KEY=your_key
BINANCE_API_SECRET=your_secret

3 Run bot

Example MARKET order

python cli.py --symbol BTCUSDT --side BUY --order_type MARKET --quantity 0.001

Example LIMIT order

python cli.py --symbol BTCUSDT --side SELL --order_type LIMIT --quantity 0.001 --price 70000

## Features

- Market orders
- Limit orders
- BUY / SELL support
- CLI interface
- Logging to file
- Error handling
- Input validation

