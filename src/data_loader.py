import yfinance as yf

TICKERS = ["SPY", "QQQ", "TLT", "GLD", "USO", "^VIX"]

print("Downloading market data...")

data = yf.download(
    TICKERS,
    start="2010-01-01",
    end="2026-01-01",
    auto_adjust=True
)

print("Download complete!")
print("Shape:", data.shape)

data.to_csv("data/market_data.csv")

print("Saved to data/market_data.csv")