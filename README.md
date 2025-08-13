# Discount Calculator in Python

This is a simple Python program that calculates the final price of an item after applying a discount.  
The program only applies the discount if it is **20% or higher**, otherwise, it returns the original price.

---

## Assignment Instructions

1. **Function**: Create a function named `calculate_discount(price, discount_percent)` that:
   - Takes the original price and discount percentage as parameters.
   - If the discount is 20% or higher, calculates and returns the final price after discount.
   - Otherwise, returns the original price.

2. **User Input**:
   - Prompt the user to enter:
     - The original price of an item.
     - The discount percentage.
   - Display the final price after applying the discount, or the original price if no discount is applied.

---

##  Code Example
```python
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



## Example Run
Enter the original price of the item: 100
Enter the discount percentage: 25
Final price after 25% discount: $75.00

##  Requirements
Python 3.x installed on your system.

## Author
Jennifer
linkedin: https://www.linkedin.com/in/jennifer-omoregie-83388232a?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app









    print(f"No discount applied. Price remains: ${final_price:.2f}")
