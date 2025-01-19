# main-0.py

import sys
from bank_account import BankAccount

def main():
    account = BankAccount(100)  # Starting with an example initial balance of $100

    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    # Extracting the command and parameters
    command_parts = sys.argv[1].split(':')
    command = command_parts[0]
    amount = float(command_parts[1]) if len(command_parts) > 1 else None

    # Handling commands
    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${amount:.2f}")
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${amount:.2f}")
        else:
            print("Insufficient funds.")
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()
