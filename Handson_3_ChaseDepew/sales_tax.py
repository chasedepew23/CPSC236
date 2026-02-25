# sales_tax.py

TAX_RATE = 0.06   # 6% sales tax


def calculate_tax(total):
    """Calculate sales tax based on total."""
    return round(total * TAX_RATE, 2)


def calculate_total_after_tax(total):
    """Calculate total amount after adding sales tax."""
    tax = calculate_tax(total)
    return round(total + tax, 2)