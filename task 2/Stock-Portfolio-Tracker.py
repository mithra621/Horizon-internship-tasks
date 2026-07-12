# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 135
}

total_value = 0

print("===== Stock Portfolio Tracker =====")
print("Available Stocks:")
for stock, price in stock_prices.items():
    print(f"{stock} : ${price}")

num_stocks = int(input("\nHow many different stocks do you own? "))

portfolio = {}

for i in range(num_stocks):
    stock_name = input("\nEnter stock symbol: ").upper()

    if stock_name not in stock_prices:
        print("Stock not available.")
        continue

    quantity = int(input("Enter quantity: "))

    investment = stock_prices[stock_name] * quantity
    portfolio[stock_name] = {
        "quantity": quantity,
        "investment": investment
    }

    total_value += investment

print("\n===== Portfolio Summary =====")

for stock, details in portfolio.items():
    print(
        f"{stock} | Quantity: {details['quantity']} | "
        f"Investment: ${details['investment']}"
    )

print(f"\nTotal Investment Value: ${total_value}")

# Save to file
with open("portfolio_summary.txt", "w") as file:
    file.write("===== Stock Portfolio Summary =====\n")

    for stock, details in portfolio.items():
        file.write(
            f"{stock} | Quantity: {details['quantity']} | "
            f"Investment: ${details['investment']}\n"
        )

    file.write(f"\nTotal Investment Value: ${total_value}")

print("\nPortfolio saved to portfolio_summary.txt")