import csv
import os
from datetime import datetime

# Sample stock prices for demonstration
stock_prices = {
    "AAPL": 230.00,
    "MSFT": 510.00,
    "NVDA": 180.00,
    "AMZN": 225.00,
    "GOOGL": 195.00,
    "META": 700.00,
    "TSLA": 350.00
}


# Load stock symbols and company names from stock_data.csv
def load_stocks():
    stocks = {}

    try:
        with open("stock_data.csv", "r", newline="", encoding="utf-8-sig") as file:
            reader = csv.DictReader(file)

            for row in reader:
                symbol = row["Symbol"].strip().upper()
                company = row["Security"].strip()
                stocks[symbol] = company

    except FileNotFoundError:
        print("Error: stock_data.csv was not found.")
        return {}

    return stocks


# Get a valid positive number from the user
def get_positive_number(message):
    while True:
        try:
            value = float(input(message))

            if value > 0:
                return value

            print("Please enter a number greater than zero.")

        except ValueError:
            print("Invalid input. Please enter a number.")


# Save portfolio results to CSV
def save_to_csv(results, total_invested, total_value, total_profit):
    file_exists = os.path.exists("portfolio_summary.csv")

    with open("portfolio_summary.csv", "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        if not file_exists or os.path.getsize("portfolio_summary.csv") == 0:
            writer.writerow([
                "Date",
                "Symbol",
                "Company",
                "Buy Price",
                "Current Price",
                "Quantity",
                "Invested",
                "Current Value",
                "Profit/Loss",
                "Percentage Gain/Loss"
            ])

        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        for stock in results:
            writer.writerow([
                date,
                stock["symbol"],
                stock["company"],
                stock["buy_price"],
                stock["current_price"],
                stock["quantity"],
                stock["invested"],
                stock["current_value"],
                stock["profit_loss"],
                stock["percentage"]
            ])

        writer.writerow([
            date,
            "PORTFOLIO TOTAL",
            "",
            "",
            "",
            "",
            round(total_invested, 2),
            round(total_value, 2),
            round(total_profit, 2),
            ""
        ])

    print("\nPortfolio results successfully saved to portfolio_summary.csv!")


# Main program
def main():
    stocks = load_stocks()

    if not stocks:
        print("No stock data available. Check your stock_data.csv file.")
        return

    portfolio = []

    print("=" * 45)
    print("       STOCK PORTFOLIO TRACKER")
    print("=" * 45)

    while True:
        symbol = input("\nEnter stock ticker (e.g. AAPL): ").strip().upper()

        if symbol not in stocks:
            print("Stock symbol not found in stock_data.csv.")
            continue

        company = stocks[symbol]

        print(f"Company: {company}")

        buy_price = get_positive_number("Enter your buying price: ")
        quantity = get_positive_number("Enter number of shares: ")

        if symbol in stock_prices:
            current_price = stock_prices[symbol]
            print(f"Sample current price: ${current_price:.2f}")
        else:
            print("No sample price available for this stock.")
            current_price = get_positive_number(
                "Enter a demonstration current price: "
            )

        invested = buy_price * quantity
        current_value = current_price * quantity
        profit_loss = current_value - invested
        percentage = (profit_loss / invested) * 100

        portfolio.append({
            "symbol": symbol,
            "company": company,
            "buy_price": buy_price,
            "current_price": current_price,
            "quantity": quantity,
            "invested": invested,
            "current_value": current_value,
            "profit_loss": profit_loss,
            "percentage": percentage
        })

        another = input("\nAdd another stock? (yes/no): ").strip().lower()

        if another != "yes":
            break

    # Calculate portfolio totals
    total_invested = sum(stock["invested"] for stock in portfolio)
    total_value = sum(stock["current_value"] for stock in portfolio)
    total_profit = total_value - total_invested

    # Display portfolio report
    print("\n" + "=" * 55)
    print("             PORTFOLIO PERFORMANCE")
    print("=" * 55)

    for stock in portfolio:
        print(f"\nStock: {stock['company']} ({stock['symbol']})")
        print(f"Amount Invested: ${stock['invested']:.2f}")
        print(f"Current Value: ${stock['current_value']:.2f}")
        print(f"Profit/Loss: ${stock['profit_loss']:.2f}")
        print(f"Percentage Gain/Loss: {stock['percentage']:.2f}%")

    print("\n" + "-" * 55)
    print(f"Total Invested: ${total_invested:.2f}")
    print(f"Total Current Value: ${total_value:.2f}")
    print(f"Total Profit/Loss: ${total_profit:.2f}")
    print("=" * 55)

    save_to_csv(portfolio, total_invested, total_value, total_profit)


if __name__ == "__main__":
    main()