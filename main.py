from config import MAX_LINES, MAX_BET, MIN_BET, ROWS, COLS, SYMBOL_COUNT, SYMBOL_VALUE
from user_interaction import deposit, get_number_of_lines, get_bet, print_slot_machine
from utils import get_machine_spin, check_winnings

def spin(balance):
    lines = get_number_of_lines(MAX_LINES)
    while True:
        bet = get_bet(MIN_BET, MAX_BET)
        total_bet = bet * lines
        
        if total_bet > balance:
            print('Your balance is insufficient.')
        else:
            break 
    
    print(f'You are betting ${bet} on {lines} line(s). Total bet is: ${total_bet}.')
    
    slots = get_machine_spin(ROWS, COLS, SYMBOL_COUNT)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, SYMBOL_VALUE)
    print(f'You Won ${winnings} on lines:', *winning_lines)    
    
    return winnings - total_bet 
   
def main():
    balance = deposit()
    while True:
        print(f'Current balance: ${balance}')
        play = input('Press Enter to play (Q to quit).')
        if play.upper() == 'Q':
            break
        balance += spin(balance)
        
    print(f'Your closing balance is ${balance}')
   
if __name__ == "__main__":
    main()
