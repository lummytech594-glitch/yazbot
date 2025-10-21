# YazBot - Binance Testnet Bot

 ---

## 🧪 How to Test the Bot

1. **Clone the Repository**
   - Go to the GitHub page: [YazBot Repo](https://github.com/lummytech594-glitch/yazbot)
   - Click the green **Code** button → Copy the HTTPS link  
   - Open your terminal and run:
     ```bash
     git clone https://github.com/lummytech594-glitch/yazbot.git
     cd yazbot
     ```

2. **Create a Virtual Environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate   # (Windows)

   markdown
3. **Install Dependencies**
```bash
pip install -r requirements.txt

4. **Add Your Binance Testnet Keys**
   - Create a file named `.env` in the project folder.
   - Paste this inside:
     ```
     BINANCE_API_KEY=your_api_key_here
     BINANCE_API_SECRET=your_secret_key_here
     ```
   - Save the file.

5. **Run the Bot**
   ```bash
   python main.py

---

## 🧩 Notes you can also check
- The bot connects to **Binance Testnet**, not the live exchange.
- No real money is used — trades are purely simulated.
- Make sure your `.env` file contains valid **Testnet** API keys.
- You must have an active internet connection when running the bot.
- Works best inside a Python virtual environment (`venv`).

---

## 👨‍💻 Developer
**Lummy Tech**  
📧 Email: lummytech594@gmail.com  
🌐 GitHub: [lummytech594-glitch](https://github.com/lummytech594-glitch)










