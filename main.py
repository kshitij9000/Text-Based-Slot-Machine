# Text Based Slot Machine - TechWithTom - Learning Python Again

import random

MAX_LINES = 3
MAX_BET = 1000
MIN_BET = 10

# Numbers of Rows and Columns in slot machine
ROWS = 3
COLS = 3

symbol_counts = {
    "A": 1, #jackpot
    "B": 2,
    "C": 3,
    "D": 8,
    "E": 20
}

symbol_values = {
    "A": 600, #jackpot
    "B": 100,
    "C": 15,
    "D": 3,
    "E": 2
}

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

def get_slot_machine_spin(rows, cols, symbols):
    """Generate a slot machine spin using weighted symbol frequencies."""
    # This list stores all the symbols available.
    all_symbols = []
    # Stores key and value into symbol and count
    for symbol, count in symbols.items():
        # symbol = "B", count = 3, ["B"]*3 = ["B", "B", "B"] 
        # extend adds this to all_symbols list
        all_symbols.extend([symbol]*count)
    
    # This list stores the values on all the columns available
    columns = []
    for _ in range(cols):
        column = []
        # Numeric copy of all symbols
        # If [:] is not used same curr_symbols points to same address
        # Meaning change to curr_symbols would change all_symbols and vice versa
        curr_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(curr_symbols)
            curr_symbols.remove(value)
            column.append(value)
            
        columns.append(column)
    
    return columns
 
def print_slot_machine(columns):
    """Prints the slot machine in neat structure."""
    for row in range(len(columns[0])):
        values = [column[row] for column in columns]
        print(" | ".join(values))

def check_wins(columns, lines, bet, values):
    """Check if user won a bet or not."""
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet        
            winning_lines.append(line + 1)
    return winnings, winning_lines
    
def main():
    balance = deposit()
    lines = get_no_of_lines()
    # Check if user bets more than the amount present in balance.
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet <= balance:
            break
        else:
            print(f"You do not have enough to bet ${total_bet}. Your balance: ${balance}.")
        
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to ${total_bet}.")
    
    slots = get_slot_machine_spin(ROWS, COLS, symbol_counts)
    print_slot_machine(slots)
    
    winnings, winning_lines = check_wins(slots, lines, bet, symbol_values)
    print(f"You won ${winnings}.")
    print(f"You won on the line:", *winning_lines)
    

main()