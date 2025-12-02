income = 0
expense = 0
income_list = []
expense_list = []

while True:
    print("\nWelcome to your very own finance and expenses tracker")
    print("\n1. Add income")
    print("2. Add expense")
    print("3. View summary")
    print("4. Exit")

    choice = input("\nEnter your choice: ")

    
    if choice == "1":
        print('\nType "done" if you’re finished adding incomes.')
        while True:
            income_name = input("\nEnter the name of the income: ")
            if income_name.lower() == "done":
                break
            elif income_name.lower() in ["donr", "dine", "donee", "dobe", "dnoe"]:
                confirm = input("Did you mean 'done'? (yes/no): ").lower()
                if confirm == "yes":
                    break
            amount = float(input(f"Enter the amount of income for {income_name}: "))
            if amount < 0:
                print("\nInvalid, please enter an actual amount")
                continue
            income += amount
            income_list.append((income_name, amount))
            print(f"Added {income_name}: {amount}")

    
    elif choice == "2":
        print('\nType "done" if you’re finished adding expenses.') 
        while True:
            expense_name = input("\nEnter the name of the expense: ")
            if expense_name.lower() == "done":
                break
            elif expense_name.lower() in ["donr", "dine", "donee", "dobe", "dnoe", "doen"]:
                confirm = input("Did you mean 'done'? (yes/no): ").lower()
                if confirm == "yes":
                    break
            amount = float(input(f"Enter the amount of expense for {expense_name}: "))
            if amount < 0:
                print("Invalid, please enter an actual amount")
                continue
            expense += amount
            income -= amount 
            expense_list.append((expense_name, amount))
            print(f"Added {expense_name}: {amount}")


    elif choice == "3":
        print("\n===== Summary =====")
        print("Income List:")
        for name, amount in income_list:
            print(f"  {name}: {amount}")

        print("\nExpense List:")
        for name, amount in expense_list:
            print(f"  {name}: {amount}")

        print(f"\nTotal Income: {sum(amount for _, amount in income_list)}")
        print(f"Total Expense: {sum(amount for _, amount in expense_list)}")
        print(f"Remaining Balance: {income}")

   
    elif choice == "4":
        print("\nThank you for using your finance tracker. Goodbye!")
        break

    else:
        print("Invalid choice, please try again.")