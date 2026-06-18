# Text Based Slot Machine - TechWithTom - Learning Python Again

MAX_LINES = 3


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
            print("Enter valid number.")
            
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
            print("Enter valid number.")
            
    return lines


def main():
    balance = deposit()
    lines = get_no_of_lines()
        
    
main()        
            
