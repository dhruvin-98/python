import random


class Main:

    class BankInfo:
        def __init__(self,fn,ln,gender,address):
            self.fn = fn
            self.ln = ln
            self.gender = gender
            self.address = address

    class BankAccount:
        def __init__(self,acno,amount,info):
            self.acno = acno
            self.amount = amount
            self.object_bank_info = info

    class Saving:
        min_amount=10000
        rate=6 #percent

    class Current:
        min_amount=5000
        rate=None

    def run(self):

        fn = input("First Name : ")
        ln = input("Last Name ")
        gender = input("Gender :")
        address = input("Address :")

        info = self.BankInfo(fn,ln,gender,address)

        choice = input("Choose Saving or Current: ").strip().lower()
        if choice == "saving":
            account_type = self.Saving
        elif choice == "current":
            account_type = self.Current
        else:
           print("Invalid choice")
           return
        



        for attempt in range(3):
                    try:
                        amount = float(input("Enter deposit amount: "))
                    except ValueError:
                        print("Please enter a valid number.")
                        continue

                    if amount >= account_type.min_amount:
                        break

                    remaining = 2 - attempt
                    if remaining:
                        print(
                            f"Minimum deposit is {account_type.min_amount}. "
                            f"Try again ({remaining} attempt(s) left)."
                        )
        else:
            print("Three attempts used. Exiting.")
            return

                    
        acno = random.randint(10**12,10**13-1)
        account = self.BankAccount(acno,amount,info)


        months = None
        if choice == "saving":
            try:
                months = int(input("Enter number of months: "))
            except ValueError:
                print("Please enter a whole number of months.")
                return
            interest = amount * (account_type.rate / 100) * (months / 12)
        else:
            interest = None


        print("\n--- Account Profile ---")
        print(f"First name: {account.object_bank_info.fn}")
        print(f"Last name: {account.object_bank_info.ln}")
        print(f"Gender: {account.object_bank_info.gender}")
        print(f"Address: {account.object_bank_info.address}")
        print(f"Account number: {account.acno}")
        print(f"Amount: {account.amount:.2f}")
        print(f"Account type: {choice.title()}")

        if choice == "saving":
            print(f"Months: {months}")
            print(f"Rate of interest: {account_type.rate}% per year")
            print(f"Interest: {interest:.2f}")


Main().run()

    