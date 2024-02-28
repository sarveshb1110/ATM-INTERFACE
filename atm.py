import time 

print("WELCOME TO BANK OF DYPCOE\n")
time.sleep(1)
pin=0000
  

def atmservices(lock):
        
    initial_balance=int(5000)
    balance=initial_balance
    history=[]
    verify=lock

    if(verify==pin):
        print("Authentication successfull\n")
        time.sleep(0.5)
        print("ATM SERVICES")
        print("1.Withdraw Amount")
        print("2.Deposit Amount")
        print("3.View Balance")
        print("4.Transaction History")  
        print("5.Exit")
                
        while True:
            choice=int(input("Please enter your choice for services :"))


            if choice == 1:
                        amount = float(input("Enter the withdrawal amount: "))
                        if amount>balance:
                            print("Unsuffecient Balance")
                            break
                        balance=balance-amount
                        print(f"Your account has been credited by ${amount} , Your account balance is ${balance}")
                        detail=f"Withdrawed ${amount}"
                        history.append(detail)
                          
            elif choice == 2:
                            amount = float(input("Enter the deposit amount: "))
                            balance=balance+amount
                            print(f"Your account has been debited by ${amount} , Your account balance is ${balance}")
                            print(f"Your account balance is {balance}")
                            detail=f"Deposited ${amount}"
                            history.append(detail)

            elif choice == 3:
                        print(f"Your account balance is ${balance}")

            elif choice == 4:
                        print("Your Transaction History is ",history)

            elif choice == 5:
                        print("Thank you for using the ATM. Goodbye!")
                        break
                
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")


    else:
        print("Invalid , Please enter 4 digit numeric password again")
        

lock=int(input("Please enter your 4 digit password :"))#[:max_digits]


atmservices(lock)
    





