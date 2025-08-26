"""
Data Fetcher Module for AI-Enhanced Momentum Portfolio

This module handles the collection and processing of stock market data
for our momentum portfolio analysis.
"""

import pandas as pd
import yfinance as yf
import numpy as np
from typing import List, Dict, Optional
import os
from datetime import datetime, timedelta


class DataFetcher:
    """
    A class to handle fetching and processing stock market data.
    """
    
    def __init__(self, data_dir: str = "data"):
        """
        Initialize the DataFetcher.
        
        Args:
            data_dir (str): Directory to store downloaded data
        """
        self.data_dir = data_dir
        self._ensure_data_directory()
    
    def _ensure_data_directory(self):
        """Ensure the data directory exists."""
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)
            print(f"✅ Created data directory: {self.data_dir}")
    
    def get_sp500_symbols(self) -> List[str]:
        """
        Get a list of S&P 500 stock symbols.
        
        Returns:
            List[str]: List of stock symbols
        """
        # For now, we'll use a sample of major stocks
        # In a full implementation, you might scrape this from Wikipedia or use an API
        sample_stocks = [
            'AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA', 'META', 'NVDA', 'BRK-B',
            'JPM', 'JNJ', 'V', 'PG', 'UNH', 'HD', 'MA', 'DIS', 'PYPL', 'BAC',
            'ADBE', 'CRM', 'NFLX', 'CMCSA', 'PFE', 'ABT', 'KO', 'PEP', 'TMO',
            'AVGO', 'COST', 'DHR', 'MRK', 'ACN', 'VZ', 'TXN', 'QCOM', 'HON',
            'LLY', 'LOW', 'UPS', 'IBM', 'RTX', 'SPGI', 'INTU', 'MS', 'GS'
        ]
        return sample_stocks
    
    def fetch_stock_data(self, symbol: str, start_date: str = "2020-01-01", 
                        end_date: Optional[str] = None) -> pd.DataFrame:
        """
        Fetch historical stock data for a given symbol.
        
        Args:
            symbol (str): Stock symbol
            start_date (str): Start date in YYYY-MM-DD format
            end_date (str, optional): End date in YYYY-MM-DD format
            
        Returns:
            pd.DataFrame: Historical stock data
        """
        if end_date is None:
            end_date = datetime.now().strftime("%Y-%m-%d")
        
        try:
            ticker = yf.Ticker(symbol)
            data = ticker.history(start=start_date, end=end_date)
            
            if data.empty:
                print(f"⚠️  No data found for {symbol}")
                return pd.DataFrame()
            
            # Add symbol column
            data['Symbol'] = symbol
            
            print(f"✅ Successfully fetched data for {symbol}")
            return data
            
        except Exception as e:
            print(f"❌ Error fetching data for {symbol}: {str(e)}")
            return pd.DataFrame()
    
    def fetch_multiple_stocks(self, symbols: List[str], start_date: str = "2020-01-01",
                            end_date: Optional[str] = None) -> Dict[str, pd.DataFrame]:
        """
        Fetch data for multiple stocks.
        
        Args:
            symbols (List[str]): List of stock symbols
            start_date (str): Start date in YYYY-MM-DD format
            end_date (str, optional): End date in YYYY-MM-DD format
            
        Returns:
            Dict[str, pd.DataFrame]: Dictionary of stock data
        """
        stock_data = {}
        
        print(f"🔄 Fetching data for {len(symbols)} stocks...")
        
        for symbol in symbols:
            data = self.fetch_stock_data(symbol, start_date, end_date)
            if not data.empty:
                stock_data[symbol] = data
        
        print(f"✅ Successfully fetched data for {len(stock_data)} stocks")
        return stock_data
    
    def save_data(self, data: pd.DataFrame, filename: str):
        """
        Save data to CSV file.
        
        Args:
            data (pd.DataFrame): Data to save
            filename (str): Name of the file
        """
        filepath = os.path.join(self.data_dir, filename)
        data.to_csv(filepath)
        print(f"💾 Data saved to {filepath}")
    
    def load_data(self, filename: str) -> pd.DataFrame:
        """
        Load data from CSV file.
        
        Args:
            filename (str): Name of the file to load
            
        Returns:
            pd.DataFrame: Loaded data
        """
        filepath = os.path.join(self.data_dir, filename)
        if os.path.exists(filepath):
            data = pd.read_csv(filepath, index_col=0, parse_dates=True)
            print(f"📂 Data loaded from {filepath}")
            return data
        else:
            print(f"❌ File not found: {filepath}")
            return pd.DataFrame()


def main():
    """
    Main function to demonstrate the DataFetcher usage.
    """
    print("🚀 Starting Data Fetcher Demo...")
    
    # Initialize the data fetcher
    fetcher = DataFetcher()
    
    # Get sample stocks
    symbols = fetcher.get_sp500_symbols()[:10]  # Start with 10 stocks for demo
    
    # Fetch data
    stock_data = fetcher.fetch_multiple_stocks(symbols, start_date="2022-01-01")
    
    # Save data for each stock
    for symbol, data in stock_data.items():
        fetcher.save_data(data, f"{symbol}_data.csv")
    
    print("🎉 Data fetching demo completed!")


if __name__ == "__main__":
    main()
