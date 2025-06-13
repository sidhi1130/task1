import csv
from datetime import datetime

# Hardcoded stock prices dictionary
STOCK_PRICES = {
    "AAPL": 180.00,
    "TSLA": 250.00,
    "GOOGL": 135.00,
    "MSFT": 375.00,
    "NVDA": 450.00,
    "AMZN": 140.00,
    "META": 320.00,
    "NFLX": 400.00,
    "AMD": 115.00,
    "INTC": 45.00
}

class StockPortfolio:
    def __init__(self):
        self.portfolio = {}
        self.total_value = 0.0
    
    def display_available_stocks(self):
        """Display all available stocks and their prices."""
        print("\n" + "="*50)
        print("AVAILABLE STOCKS")
        print("="*50)
        for stock, price in STOCK_PRICES.items():
            print(f"{stock:<8} ${price:>8.2f}")
        print("="*50)
    
    def add_stock(self, symbol, quantity):
        """Add a stock to the portfolio."""
        symbol = symbol.upper()
        if symbol in STOCK_PRICES:
            if symbol in self.portfolio:
                self.portfolio[symbol] += quantity
            else:
                self.portfolio[symbol] = quantity
            return True
        return False
    
    def calculate_total_value(self):
        """Calculate the total portfolio value."""
        self.total_value = 0.0
        for symbol, quantity in self.portfolio.items():
            self.total_value += quantity * STOCK_PRICES[symbol]
        return self.total_value
    
    def display_portfolio(self):
        """Display the current portfolio."""
        if not self.portfolio:
            print("\nYour portfolio is empty!")
            return
        
        print("\n" + "="*70)
        print("YOUR PORTFOLIO")
        print("="*70)
        print(f"{'Stock':<8} {'Quantity':<10} {'Price':<10} {'Total Value':<15}")
        print("-"*70)
        
        total_value = 0.0
        for symbol, quantity in self.portfolio.items():
            price = STOCK_PRICES[symbol]
            stock_value = quantity * price
            total_value += stock_value
            print(f"{symbol:<8} {quantity:<10} ${price:<9.2f} ${stock_value:<14.2f}")
        
        print("-"*70)
        print(f"{'TOTAL PORTFOLIO VALUE:':<43} ${total_value:<14.2f}")
        print("="*70)
        
        self.total_value = total_value
    
    def save_to_txt(self, filename="portfolio.txt"):
        """Save portfolio to a text file."""
        try:
            with open(filename, 'w') as file:
                file.write("STOCK PORTFOLIO REPORT\n")
                file.write("="*50 + "\n")
                file.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
                
                if not self.portfolio:
                    file.write("Portfolio is empty.\n")
                    return True
                
                file.write(f"{'Stock':<8} {'Quantity':<10} {'Price':<10} {'Total Value':<15}\n")
                file.write("-"*50 + "\n")
                
                total_value = 0.0
                for symbol, quantity in self.portfolio.items():
                    price = STOCK_PRICES[symbol]
                    stock_value = quantity * price
                    total_value += stock_value
                    file.write(f"{symbol:<8} {quantity:<10} ${price:<9.2f} ${stock_value:<14.2f}\n")
                
                file.write("-"*50 + "\n")
                file.write(f"TOTAL PORTFOLIO VALUE: ${total_value:.2f}\n")
            
            print(f"Portfolio saved to {filename}")
            return True
        except Exception as e:
            print(f"Error saving to file: {e}")
            return False
    
    def save_to_csv(self, filename="portfolio.csv"):
        """Save portfolio to a CSV file."""
        try:
            with open(filename, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Stock Symbol', 'Quantity', 'Price per Share', 'Total Value'])
                
                for symbol, quantity in self.portfolio.items():
                    price = STOCK_PRICES[symbol]
                    stock_value = quantity * price
                    writer.writerow([symbol, quantity, price, stock_value])
                
                # Add total row
                writer.writerow(['TOTAL', '', '', self.total_value])
            
            print(f"Portfolio saved to {filename}")
            return True
        except Exception as e:
            print(f"Error saving to CSV: {e}")
            return False

def main():
    """Main function to run the stock portfolio tracker."""
    portfolio = StockPortfolio()
    
    print("Welcome to Stock Portfolio Tracker!")
    print("Track your investments with ease!")
    
    while True:
        print("\n" + "="*40)
        print("MENU OPTIONS")
        print("="*40)
        print("1. View available stocks")
        print("2. Add stock to portfolio")
        print("3. View portfolio")
        print("4. Save portfolio to TXT file")
        print("5. Save portfolio to CSV file")
        print("6. Exit")
        print("="*40)
        
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == '1':
            portfolio.display_available_stocks()
        
        elif choice == '2':
            portfolio.display_available_stocks()
            
            while True:
                symbol = input("\nEnter stock symbol (or 'back' to return): ").strip()
                if symbol.lower() == 'back':
                    break
                
                if symbol.upper() not in STOCK_PRICES:
                    print(f"Stock '{symbol}' not found. Please choose from available stocks.")
                    continue
                
                try:
                    quantity = int(input(f"Enter quantity for {symbol.upper()}: "))
                    if quantity <= 0:
                        print("Quantity must be positive!")
                        continue
                    
                    if portfolio.add_stock(symbol, quantity):
                        print(f"Added {quantity} shares of {symbol.upper()} to your portfolio!")
                    break
                    
                except ValueError:
                    print("Please enter a valid number for quantity.")
        
        elif choice == '3':
            portfolio.display_portfolio()
        
        elif choice == '4':
            if portfolio.portfolio:
                portfolio.calculate_total_value()
                portfolio.save_to_txt()
            else:
                print("Your portfolio is empty. Add some stocks first!")
        
        elif choice == '5':
            if portfolio.portfolio:
                portfolio.calculate_total_value()
                portfolio.save_to_csv()
            else:
                print("Your portfolio is empty. Add some stocks first!")
        
        elif choice == '6':
            print("Thank you for using Stock Portfolio Tracker!")
            print("Happy investing!")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1-6.")

if __name__ == "__main__":
    main()