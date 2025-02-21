import logging

# Set up logging to track function calls
logging.basicConfig(filename="app.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def add(a, b):
    """Returns the sum of two numbers."""
    result = a + b
    logging.info(f"Adding {a} + {b} = {result}")
    return result

def subtract(a, b):
    """Returns the difference of two numbers."""
    result = a - b
    logging.info(f"Subtracting {a} - {b} = {result}")
    return result

def multiply(a, b):
    """Returns the product of two numbers."""
    result = a * b
    logging.info(f"Multiplying {a} * {b} = {result}")
    return result

def divide(a, b):
    """Returns the division of two numbers. Raises error if dividing by zero."""
    if b == 0:
        logging.error("Attempted to divide by zero")
        raise ValueError("Cannot divide by zero")
    result = a / b
    logging.info(f"Dividing {a} / {b} = {result}")
    return result
