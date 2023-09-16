def Options(balance,name):
    print("WELCOME MR/MRS",name)
    print("\n\n\n")
    print("Enter Your Choice :\n")
    print('1. WITHDRAW ')
    print("2. DEPOSIT ")
    print("3. BALANCE INQUERY ")
    print("4. FUND TRANSFER ")
    print('5. Exit')
    choice = input("Enter Your Choice: ")
    if choice == '1':
        WITHDRAW(balance)
    elif choice == '2':
        Deposit(balance)
    elif choice == '3':
        BalanceInquery(balance)
    elif choice == '4':
        FundTrunsfer(balance)
    elif choice == '5':
        print("Thank You For Visiting Us.")

    else:
        print("invalid choice")


def WITHDRAW(balance):
    amount = int(input("Enter Amount to Witdraw :"))
    new_balance = balance-amount
    print("collect  Your money ")
    print("your remaining balance is :", new_balance)


def Deposit(balance):
    amount = int(input("Enter Amount to Deposit :"))
    new_balance = balance+amount
    print("Thanks  for deposting ")
    print("Your balance is ", new_balance)


def BalanceInquery(balance):

    print("Your balance is: \n", balance)
    choice = input("Do you want to another Transaction (Y/N): ").capitalize()
    if choice == 'Y':
        Options()
    else:
        print('THANKS FOR VISITING ')


def FundTrunsfer(balance):
    print("\n\n\n")
    print("Enter Your Choice :\n")
    print('1. Edhi Foundation ')
    print("2. Aga Khan Foundation ")
    print("3. Chhipa Welfare Association")
    print("4. SAYLANI WELFARE TRUST ")
    choice = input("Enter Your Choice: ")
    if choice == '1':
        donation_amount = int(input("Enter Your Amount for Donation :"))
        final_Amount = balance-donation_amount
        txt1 = "Your Donation of amount {} has been successfully send to Edhi Foundation."
        print(txt1.format(donation_amount))
        txt2 = "Your remaining balance is {}."
        print(txt2.format(final_Amount))
        print("THANK YOU!")
    elif choice == '2':
        donation_amount = int(input("Enter Your Amount for Donation :"))
        final_Amount = balance-donation_amount
        txt1 = "Your Donation of amount {} has been successfully send to Aga Khan Foundation."
        print(txt1.format(donation_amount))
        txt2 = "Your remaining balance is {}."
        print(txt2.format(final_Amount))
        print("THANK YOU!")
    elif choice == '3':
        donation_amount = int(input("Enter Your Amount for Donation :"))
        final_Amount = balance-donation_amount
        txt1 = "Your Donation of amount {} has been successfully send to Chhipa Welfare Association."
        print(txt1.format(donation_amount))
        txt2 = "Your remaining balance is {}."
        print(txt2.format(final_Amount))
        print("THANK YOU!")
    elif choice == '4':
        donation_amount = int(input("Enter Your Amount for Donation :"))
        final_Amount = balance-donation_amount
        txt1 = "Your Donation of amount {} has been successfully send to SAYLANI WELFARE TRUST."
        print(txt1.format(donation_amount))
        txt2 = "Your remaining balance is {}."
        print(txt2.format(final_Amount))
        print("THANK YOU!")
    else:
        print("invalid choice")


def ATM_number(input_number, input_pin):
    bank_accounts = {222103013: {'name':'AQIB MEHMMOD','pin': 2742, 'balance': 1000.0},
                     222103018: {'name':'MUHMMAD NOMAN','pin': 66626, 'balance': 2500.0},
                     222103025: {'name':'SAMIA GULAM QADIR','pin': 72642, 'balance': 500.0},
                     222103042: {'name':'FARWA IRFAN','pin': 32582, 'balance': 3000.0}
                     }
    if input_number in bank_accounts:
        if input_pin == bank_accounts[input_number]['pin']:
            print("Login successful!")
            Options(bank_accounts[input_number]['balance'], bank_accounts[input_number]['name'])
        else:
            print("Incorrect PIN. Please try again.")
            ATM_number(input_number, input_pin)
    else:
        print("Account not Found")


print("--------------------------")
print("--------------------------")
print('||\t\t\t||')
print('||\tWELCOME \t||')
print('||\t  TO \t\t||')
print('||\t UBL\t\t||')
print('||\t ATM\t\t||')
print('||\t\t\t||')
print('||\t\t\t||')
print('||\t\t\t||')

print("--------------------------")
print("--------------------------")
input_number = int(input("Enter your Acount  number :"))
input_pin = int(input("Enter your Acount PIN :"))
ATM_number(input_number, input_pin)
