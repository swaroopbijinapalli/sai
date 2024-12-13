import yfinance as yf

# Define the StockPortfolio class
class StockPortfolio:
    def _init_(self):
        self.portfolio = {}  # Dictionary to store stock symbol and quantity
    
    def add_stock(self, symbol, quantity):
        """Add stock to the portfolio."""
        if symbol in self.portfolio:
            self.portfolio[symbol] += quantity
        else:
            self.portfolio[symbol] = quantity
        print(f"Added {quantity} shares of {symbol} to your portfolio.")
    
    def remove_stock(self, symbol, quantity):
        """Remove stock from the portfolio."""
        if symbol in self.portfolio and self.portfolio[symbol] >= quantity:
            self.portfolio[symbol] -= quantity
            if self.portfolio[symbol] == 0:
                del self.portfolio[symbol]
            print(f"Removed {quantity} shares of {symbol} from your portfolio.")
        else:
            print(f"Insufficient shares or stock symbol not found in the portfolio.")
    
    def get_stock_data(self, symbol):
        """Fetch the latest stock price data."""
        stock = yf.Ticker(symbol)
        data = stock.history(period="1d")  # Get the stock data for the last day
        return data['Close'].iloc[0]  # Using iloc[0] to access the first element by position
    
    def track_portfolio(self):
        """Track the performance of the entire portfolio."""
        total_value = 0
        print(f"\n{'Symbol':<10} {'Shares':<10} {'Price':<15} {'Total Value':<15}")
        print("-" * 50)
        
        # Loop over the portfolio to display each stock's information
        for symbol, quantity in self.portfolio.items():
            try:
                price = self.get_stock_data(symbol)
                total_value += price * quantity
                print(f"{symbol:<10} {quantity:<10} {price:<15.2f} {price * quantity:<15.2f}")
            except Exception as e:
                print(f"Error fetching data for {symbol}: {str(e)}")
        
        print(f"\nTotal Portfolio Value: {total_value:.2f}")
        
# Example usage in a Jupyter notebook cell

# Initialize the portfolio
portfolio = StockPortfolio()

# Add some stocks to the portfolio (for testing purposes)
portfolio.add_stock('AAPL', 10)  # Add 10 shares of Apple
portfolio.add_stock('TSLA', 5)   # Add 5 shares of Tesla

# Remove some stocks
portfolio.remove_stock('TSLA', 2)  # Remove 2 shares of Tesla

# Track portfolio performance
portfolio.track_portfolio()
