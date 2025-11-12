#Python Banking Program

def show_balance(balance):
    print(f"Your Balance is {balance:.2f} TK")

def deposit():
    amount = float(input("Enter an Deposit Amount : "))
    if amount >= 0:
        return amount
    else:
        print("That's not a valid Amount")
        return 0

def withdrow(balance):
    amount = float(input("Enter Amount to be Withdrawn : "))
    if amount > balance:
        print("Insufficient Funds")
        return 0
    elif amount < 0:
        print("Amount must be greater than 0")
        return 0
    else:
        return amount


def main():
    balance = 0
    is_running = True
    
    while is_running:
        print("*****************")
        print("Bnnking Program")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdrow")
        print("4. Exit")
        print("*****************")
    
        choice = input("Enter your choice (1 - 4) : ")
    
        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdrow(balance)
        elif choice == '4':
            is_running = False
        else:
            print("That is not a Valid Choice")
    
    print("Thank You")

if __name__ == '__main__':
    main()