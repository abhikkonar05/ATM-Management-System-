acc_holders={
    'Name':'Abhik',
    'Account Number':1234567890,
    'PIN':1234,
    'Balance':39875
}
User_pin=int(input("Enter your PIN: "))
if len(str(User_pin))!=4:
    print("Invalid PIN format. Please enter a 4-digit PIN.")
    exit()
attempt=3
while attempt>0:
    if User_pin==acc_holders['PIN']:
        print("Login successful.")
        print(f"Welcome {acc_holders['Name']}")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Change PIN")
        print("5. Exit")
        choice=int(input("Enter your choice: "))
        if choice==1:   
            print(f"Your current balance is: {acc_holders['Balance']}")
        elif choice==2:
            deposit_amount=int(input("Enter amount to deposit: "))
            if deposit_amount%500==0:
                acc_holders['Balance']+=deposit_amount
                print(f"Amount deposited successfully. New balance is: {acc_holders['Balance']}")
                break 
            else:
                print("Invalid deposit amount.")  
                deposit_amount=int(input("Enter amount to deposit: "))
        elif choice==3:
            withdraw_amount=int(input("Enter amount to withdraw: "))
            if withdraw_amount%500==0:
                if withdraw_amount<=acc_holders['Balance']:
                    acc_holders['Balance']-=withdraw_amount
                    print(f"Amount withdrawn successfully. New balance is: {acc_holders['Balance']}")
                else:
                    print("Insufficient balance.")
            else:
                print("Invalid withdrawal amount.")
        elif choice==4:
            new_pin=int(input("Enter new 4-digit PIN: "))
            if len(str(new_pin))==4:
                acc_holders['PIN']=new_pin
                print("PIN changed successfully.")
            else:
                print("Invalid PIN format.")
        elif choice==5:
            print("Thank you for using our ATM service.")
            exit()       

    else:
        attempt-=1
        if attempt>0:
            print(f"Invalid PIN. You have {attempt} attempts left.")
            User_pin=int(input("Enter your PIN: "))
        else:
            print("Too many failed attempts. Your account has been blocked.")
            exit()