# Text Based Slot Machine - TechWithTom - Learning Python Again

MAX_LINES = 3
MAX_BET = 1000
MIN_BET = 10


def deposit():
    """Collects deposit amount."""
    while True:
        # Reads a line from input and converts to string
        amount = input("Enter deposit amount: $")
        # isdigit returns False if non numeric characters exist including -ve no
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Deposit amount must be greater than zero.")
        else:
            print("Please enter a number.")
            
    return amount

def get_no_of_lines():
    """Collects no of lines user wants to bet on."""
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + "): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter valid amount of lines.")
        else:
            print("Please enter a number.")
            
    return lines

def get_bet():
    """Collects bet amount."""
    while True:
        amt = input("How much to would you like to bet? $")
        if amt.isdigit():
            amt = int(amt)
            if MIN_BET <= amt <= MAX_BET:
                break
            else:
                print(f"Amount must be between &{MIN_BET} - &{MAX_BET}.")
        else:
            print("Please enter a number.")
            
    return amt
    

def main():
    balance = deposit()
    lines = get_no_of_lines()
        
    
main()        
            
