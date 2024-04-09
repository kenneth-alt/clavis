import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
  "A": 2,
  "B": 4,
  "c": 6,
  "D": 8
}

symbol_value = {
  "A": 5,
  "B": 4,
  "c": 3,
  "D": 2
}


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

def get_number_of_lines():
  while True:
    lines = input('Enter number of lines to bet on: (1-' + str(MAX_LINES) + '): ')
    if lines.isdigit():
      lines = int(lines)
      if 1 <= lines <= MAX_LINES:
        break
      else:
        print('Enter a valid number of lines.')
    else:
      print('Please enter a number.')
  return lines
  
def get_bet():
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

def get_machine_spin(rows, cols, symbols):
  all_symbols = []
  for symbol, symbol_count in symbols.items():
    for _ in range(symbol_count):
      all_symbols.append(symbol)
      
  columns = []
  for _ in range(cols):
    column = []
    current_symbols = all_symbols[:]
    for _ in range(rows):
      value = random.choice(current_symbols)
      current_symbols.remove(value)
      column.append(value)
      
    columns.append(column)
    
  return columns

def print_slot_machine(columns):
  for row in range(len(columns[0])):
    for i, column in enumerate(columns):
      if i != len(columns) - 1:
        print(column[row], end=" | ")
      else:
        print(column[row], end="")
        
    print()

def check_winnings(columns, lines, bet, values):
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
 
 
def spin(balance)
  lines = get_number_of_lines()
  while True:
    bet = get_bet()
    total_bet = bet * lines
    
    if total_bet > balance:
      print('Your balance is insufficient.')
    else:
      break 
  
  print(f'You are betting ${bet} on {lines} line(s). Total bet is: ${total_bet}.')
  
  slots = get_machine_spin(ROWS, COLS, symbol_count)
  print_slot_machine(slots)
  winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
  print(f'You Won ${winnings} on lines', *winning_lines)    
  
  return winnings - total_bet 
 
  
def main():
  balance = deposit()
  while True:
    print(f'Current balance: ${balance}')
    play = input('Press Enter to play (Q to quit).')
    if play == 'Q':
      break
    balance += spin(balance)
    
  print(f'Your closing balance is ${balance}')
  
  
  
main()