User: Does this block of code meet my team's best practice criteria?

GitHub Copilot: Used 3 references
    copilot-instructions.md
    analyzer_GPT4.1.py
Unknown variable type

GitHub Copilot: Your code is **mostly good** but has a few issues to address based on your team's conventions:

## ✅ What's Working Well
- Clear docstrings following PEP 257
- Type hints on functions
- Good separation of concerns (loading vs. analyzing)
- Descriptive function and variable names
- Handles the core logic cleanly

## ⚠️ Issues to Fix

1. **Indentation**: Lines 5-6 use tabs instead of spaces (PEP 8 requires 4 spaces)
2. **Missing edge case handling**: 
   - `calculate_total_sales()` and `find_top_product()` don't handle empty data or missing columns
   - No error handling for file not found or malformed CSV
3. **Line length**: Some docstring lines may exceed 79 characters
4. **Missing type hints**: Return type for `find_top_product()` should handle `None` case → `Optional[str]`

## Quick Fixes Needed

````python
import csv
from typing import Optional

class SalesAnalyzer:
    """
    A class to analyze sales data from a CSV file.
    
    Attributes:
        filename (str): The path to the sales data CSV file.
        data (list): List of sales records loaded from the CSV file.
    """
    def __init__(self, filename: str):
        """
        Initialize the SalesAnalyzer with the given filename.
        
        Args:
            filename (str): Path to the sales data CSV file.
        """
        self.filename = filename
        self.data = []

    def load_data(self) -> None:
        """
        Load sales data from the CSV file into the data attribute.
        
        Assumes the CSV has 'product_name', 'price', and 'quantity'
        columns. Raises FileNotFoundError if the file doesn't exist.
        """
        try:
            with open(self.filename, mode='r') as file:
                csv_reader = csv.DictReader(file)
                self.data = [row for row in csv_reader]
        except FileNotFoundError:
            raise FileNotFoundError(
                f"Sales data file not found: {self.filename}"
            )

    def calculate_total_sales(self) -> float:
        """
        Calculate the total sales from the loaded data.
        
        Returns:
            float: The total sales value (0.0 if no data loaded).
        """
        if not self.data:
            return 0.0
        total = 0.0
        for row in self.data:
            price = float(row['price'])
            quantity = int(row['quantity'])
            total += price * quantity
        return total

    def find_top_product(self) -> Optional[str]:
        """
        Find the product with the highest total sales.
        
        Returns:
            Optional[str]: The name of the top-selling product,
            or None if no data is loaded.
        """
        if not self.data:
            return None
        top_product = None
        top_sales = 0.0
        for row in self.data:
            sales = float(row['price']) * int(row['quantity'])
            if sales > top_sales:
                top_sales = sales
                top_product = row['product_name']
        return top_product
````

**Main changes**: Spaces instead of tabs, added edge case checks, improved error handling, and proper `Optional` type hint.