class MaxLimitReached:
     """When maxim limit reached """

class main:

    class HDFCBank:

        def __init__(self):
            self.__transaction_limit = 3
            self.__max_amount = 20000
            self.__transaction_count = 0

        def withdraw(self,amount):

             if self.__transaction_count>= self.__transaction_limit:
                  raise MaxLimitReached("HDFC transaction limit reached .")
             if self.__max_amount<=amount:
                  raise MaxLimitReached("HDFC per transaction limit Reached.")
             if amount<=0:
                  raise ValueError("Amount must e greater than Zero !")

             self.__transaction_count+=1
             print(f"Withdrawl Successful of {amount}")
             print(f"Transaction Used : {self.__transaction_count}/{self.__transaction_limit}")
             
    class AXISBank:

        def __init__(self):
            self.__transaction_limit = 3
            self.__max_amount = 30000
            self.__transaction_count = 0

        def withdraw(self,amount):

                    if self.__transaction_count>= self.__transaction_limit:
                        raise MaxLimitReached("AXIS transaction limit reached .")
                    if self.__max_amount<=amount:
                        raise MaxLimitReached("AXIS per transaction limit Reached.")
                    if amount<=0:
                        raise ValueError("Amount must e greater than Zero !")

                    self.__transaction_count+=1
                    print(f"Withdrawl Successful of {amount}")
                    print(f"Transaction Used : {self.__transaction_count}/{self.__transaction_limit}")
             



    def run(self):

        choice = input("Enter Bank name : HDFC or AXIS :").strip().lower()

        if choice == "hdfc":
              bank = self.HDFCBank()
        elif choice == "axis":
              bank = self.AXISBank()
        else:
              print("Invalid choice")
              return


        while True:

            try:
                 
                amount = float(input("Enter amount to withdraw : "))

                bank.withdraw(amount)

            except ValueError as error:
                 print(error)

            except MaxLimitReached as error:
                 print(error)
                 return

            next_transaction = input("Next transaction ? (yes/no)").strip().lower()

            if next_transaction != "yes":
                 print("ATM session End :) ")
                 return



main().run()


                 







        