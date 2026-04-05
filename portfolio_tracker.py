
# Task 2: Stock Portfolio Tracker
# Developed for CodeAlpha Internship

def calculate_portfolio():
    # 1. Predefined stock prices (using a dictionary)
    stock_prices = {
        "AAPL": 185.20,
        "TSLA": 170.10,
        "GOOGL": 152.50,
        "MSFT": 420.30,
        "AMZN": 180.00
    }

    portfolio = {}
    
    print("--- 📈 Welcome to Stock Portfolio Tracker ---")
    print(f"Available stocks: {', '.join(stock_prices.keys())}")
    print("-" * 45)

    # 2. User Input
    while True:
        symbol = input("Enter stock symbol (or type 'done' to finish): ").upper()
        if symbol == 'DONE':
            break
        
        if symbol in stock_prices:
            try:
                shares = int(input(f"How many shares of {symbol} do you own? "))
                portfolio[symbol] = shares
                print(f"✅ Added {shares} shares of {symbol}.")
            except ValueError:
                print("❌ Invalid input! Please enter a number for shares.")
        else:
            print("❌ Stock not found in our list. Please try again.")

    # 3. Calculation & Display
    print("\n" + "="*30)
    print("      PORTFOLIO SUMMARY      ")
    print("="*30)
    
    total_value = 0
    summary_text = "Stock Portfolio Report:\n"

    for symbol, shares in portfolio.items():
        price = stock_prices[symbol]
        value = shares * price
        total_value += value
        line = f"{symbol}: {shares} shares @ ${price:.2f} = ${value:.2f}"
        print(line)
        summary_text += line + "\n"

    final_total = f"\nTotal Portfolio Value: ${total_value:.2f}"
    print("-" * 30)
    print(final_total)
    summary_text += final_total

    # 4. Save to a file (.txt)
    with open("portfolio_report.txt", "w") as file:
        file.write(summary_text)
    
    print("\n📄 Report saved to 'portfolio_report.txt'")

if __name__ == "__main__":
    calculate_portfolio()
    