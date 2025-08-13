def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        return price - (discount_percent / 100) * price
    else:
        return price

# User input
original_price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate and display result
final_price = calculate_discount(original_price, discount_percent)

if discount_percent >= 20:
    print(f"Final price after {discount_percent}% discount: ${final_price:.2f}")
else:
    print(f"No discount applied. Price remains: ${final_price:.2f}")

