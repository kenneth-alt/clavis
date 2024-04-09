def deposit():
    while True:
        amount = input('Enter deposit amount: $ ')
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print('Deposit amount must be greater than 0.')
        else:
            print('Please enter amount in number.')
    return amount

def get_number_of_lines(MAX_LINES):
    while True:
        lines = input(f'Enter number of lines to bet on (1-{MAX_LINES}): ')
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print('Enter a valid number of lines.')
        else:
            print('Please enter a number.')
    return lines

def get_bet(MIN_BET, MAX_BET):
    while True:
        bet_amount = input('Please enter your bet amount on each line: ') 
        if bet_amount.isdigit():
            bet_amount = int(bet_amount)
            if MIN_BET <= bet_amount <= MAX_BET:
                break
            else:
                print(f'Bet amount must be between ${MIN_BET} and ${MAX_BET}.')
        else:
            print('Please enter you bet in number.')
    return bet_amount

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
            
        print()
