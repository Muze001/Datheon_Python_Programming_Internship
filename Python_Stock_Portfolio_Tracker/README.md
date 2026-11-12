 Stock Portfolio Performance Tracker

 Project Overview
The Stock Portfolio Performance Tracker is a Python-based application developed as part of the Datheon Python Programming Internship.

The application allows users to enter stock ticker symbols, purchase prices, and share quantities. It calculates the investment value, current portfolio value, and profit or loss for each stock.

It also calculates the overall portfolio performance and saves the results to a CSV file for future reference.

Note: This version uses demonstration stock prices rather than live market data.

 Features
- Accepts stock ticker symbols.
- Identifies companies using a stock dataset.
- Accepts stock purchase prices and share quantities.
- Calculates total invested capital.
- Calculates current portfolio value.
- Calculates profit or loss for individual stocks.
- Calculates percentage gain or loss.
- Calculates overall portfolio performance.
- Saves portfolio records to a CSV file.
- Handles invalid numerical inputs.

 Technologies Used
- Python 3
- CSV module
- OS module
- Datetime module

 Project Structure


Stock_Portfolio_Tracker/
│
├── portfolio.py
├── stock_data.csv
├── portfolio_summary.csv
└── README.md


 Requirements
- Python 3 installed on your computer.
- Visual Studio Code or another Python code editor.

 How to Run

1. Download or clone the project repository.
2. Open the project folder in Visual Studio Code.
3. Open the terminal.
4. Run the following command:

bash
python portfolio.py


5. Enter the stock ticker symbol.
6. Enter your purchase price and number of shares.
7. Choose whether to add another stock.
8. View your portfolio performance report.

 Output
The program displays:
- Amount invested.
- Current stock value.
- Profit or loss.
- Percentage gain or loss.
- Total portfolio investment.
- Total portfolio value.

The results are automatically saved in `portfolio_summary.csv`.

 Author 
Developed as part of the Datheon Python Programming Internship.