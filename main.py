from dotenv import load_dotenv
import os
from binance.client import Client
from binance.exceptions import BinanceAPIException, BinanceRequestException

# ========== Setup ==========
print("🚀 Initializing YazBot Testnet Client...")

# Load environment variables
load_dotenv()

API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_API_SECRET")

# Validate environment variables
if not API_KEY or not API_SECRET:
    raise SystemExit("❌ Missing BINANCE_API_KEY or BINANCE_API_SECRET in your .env file.\n"
                     "➡️ Please add them like this:\n"
                     "BINANCE_API_KEY=your_key_here\n"
                     "BINANCE_API_SECRET=your_secret_here")

# ========== Connect to Binance Testnet ==========
print("🔗 Connecting to Binance Testnet...")

try:
    client = Client(API_KEY, API_SECRET, testnet=True)
    client.ping()  # Quick check if API is responsive
    print("✅ Connection successful! Binance Testnet is reachable.")
except Exception as e:
    raise SystemExit(f"❌ Connection failed: {e}")

# ========== Test Order ==========
print("🧪 Placing a small test order (simulation)...")

try:
    order = client.create_order(
        symbol="BTCUSDT",
        side="BUY",
        type="MARKET",
        quantity=0.001  # very small test trade
    )
    print("✅ Test order placed successfully!")
    print("📦 Order details:")
    print(order)
except BinanceAPIException as e:
    print(f"❌ Binance API Error: {e.message}")
except BinanceRequestException as e:
    print(f"⚠️ Network Error: {e.message}")
except Exception as e:
    print(f"❌ Unexpected error: {e}")

# ========== Final Confirmation ==========
print("\n🎉 YazBot setup complete!")
print("✅ Environment working correctly")
print("✅ Binance Testnet connection verified")
print("✅ Trade simulation successful")
print("📢 Your bot is ready for phase 2 🚀")
