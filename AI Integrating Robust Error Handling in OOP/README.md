# AI: Integrating Robust Error Handling in OOP

## Objective

This task enhances the Product Inventory Manager by integrating robust error handling and data validation using Python's `@property` decorators and a custom exception.

## Files Included

- **initial_code.py** – The original Product Inventory Manager provided in the assignment.
- **refactored_code.py** – The improved version with data validation, encapsulation, and exception handling.

## AI Tool Used

ChatGPT

## Improvements Made

- Created a custom exception named `InvalidProductDataError`.
- Implemented `@property` getters and setters for `price` and `quantity`.
- Prevented negative values from being assigned.
- Stored validated values in private attributes (`_price` and `_quantity`).
- Improved encapsulation and data integrity.
- Added an invalid input test case.

## Test Performed

The following test was used to verify the validation:

```python
print("\n--- Testing Invalid Input ---")
try:
    manager.inventory[0].quantity = -5
except Exception as e:
    print(f"Test result: {e}")
```

### Result

The program raised `InvalidProductDataError` with the message:

```
Quantity cannot be negative.
```

The exception was caught by the `try...except` block, preventing the program from crashing and ensuring that the product's quantity remained unchanged.
