import csv

def calculate_total_sales(filename):
    """
    Reads a CSV file and calculates the total sales.

    Assumes the CSV has 'product_name', 'price', 'quantity' columns.

    Args:
        filename (str): Path to the CSV file.

    Returns:
        float: Total sales amount.
    """
    total = 0.0
    try:
        with open(filename, mode='r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                try:
                    price = float(row['price'])
                    quantity = int(row['quantity'])
                    total += price * quantity
                except ValueError as ve:
                    print(f"Invalid data in row {row}: {ve}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return 0.0
    return total

if __name__ == "__main__":
    sales_data_file = 'sales_data.csv'
    total_sales = calculate_total_sales(sales_data_file)
    print(f"Total sales from {sales_data_file}: ${total_sales:.2f}")
