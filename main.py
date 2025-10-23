# main.py (connection part — full ready snippet)
from dotenv import load_dotenv
import os
from binance.client import Client
from binance.exceptions import BinanceAPIException, BinanceRequestException

# ========== Setup ==========
print("🚀 Initializing YazBot...")

# Load environment variables
load_dotenv()

API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_API_SECRET")

# Validate environment variables
if not API_KEY or not API_SECRET:
    raise SystemExit(
        "❌ Missing BINANCE_API_KEY or BINANCE_API_SECRET in your .env file.\n"
        "➡️ Please add them like this:\n"
        "BINANCE_API_KEY=your_key_here\n"
        "BINANCE_API_SECRET=your_secret_here"
    )

# Decide environment from .env (default = testnet)
USE_TESTNET = os.getenv("USE_TESTNET", "true").lower() in ("1", "true", "yes")
USE_DEMO_FALLBACK = os.getenv("USE_DEMO_FALLBACK", "true").lower() in ("1", "true", "yes")
# NOTE: demo fallback is only used if DNS/testnet is unreachable.

# If you must use the demo API endpoint because testnet DNS is not resolvable,
# set Client.API_URL BEFORE creating the Client object.
if not USE_TESTNET and USE_DEMO_FALLBACK:
    # live fallback — usually not needed
    Client.API_URL = "https://api-demo.binance.com/api"

if USE_TESTNET:
    # Prefer the official testnet behaviour
    print("🔗 Connecting to Binance Testnet (testnet=True)...")
    client = Client(API_KEY, API_SECRET, testnet=True)
else:
    print("🔗 Connecting to Binance Live/API-demo (no testnet=True)...")
    client = Client(API_KEY, API_SECRET)

# Quick ping check to confirm connectivity
try:
    client.ping()
    print("✅ Connection successful! Binance endpoint is reachable.")
except Exception as e:
    print(f"❌ Connection failed: {e}")
    # If you want to try demo fallback automatically, you could fallback here.
    raise SystemExit("Please check your network / API endpoint or enable VPN if required.")
