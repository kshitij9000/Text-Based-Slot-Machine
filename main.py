# Text Based Slot Machine - TechWithTom - Learning Python Again

def deposit():
    """Collects deposit amount from user."""
    while True:
        # Reads a line from input and converts to string
        amount = input("Enter deposit amount: ")
        # isdigit returns False if non numeric characters exist including -ve no
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Deposit amount must be greater than zero.")
        else:
            print("Enter valid positive number.")
            
    return amount
        
            
            
            
            

