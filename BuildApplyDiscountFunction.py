def apply_discount(price, discount):
    # Check if price is a valid integer or float
    if not isinstance(price, (int, float)):
        return "The price should be a number"
        
    # Check if discount is a valid integer or float
    if not isinstance(discount, (int, float)):
        return "The discount should be a number"
        
    # Check if price is greater than 0
    if price <= 0:
        return "The price should be greater than 0"
        
    # Check if discount is within valid percentage bounds
    if discount < 0 or discount > 100:
        return "The discount should be between 0 and 100"
        
    # Calculate and return the final discounted price
    return price - (price * discount / 100)
