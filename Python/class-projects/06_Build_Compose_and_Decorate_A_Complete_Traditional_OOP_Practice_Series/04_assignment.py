# Class Variables and Class Methods
# Assignment:
# Create a class Bank with a class variable bank_name. Add a class method change_bank_name(cls, name) that allows changing the bank name. Show that it affects all instances.

class Bank:
    bank_name = "Global Bank"  # Class variable

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name  # Change class variable

# Create instances of Bank
bank1 = Bank()
bank2 = Bank()
# Show initial bank name       
print(bank1.bank_name)  
print(bank2.bank_name)  
# After changing the bank name
Bank.change_bank_name("State Bank")
print("After changing the bank name:")
print(bank1.bank_name)  
print(bank2.bank_name)  
