# 3) Create classes that capture bank customers and bank accounts.
# 	A customer has a first and last name.
#     An account has a customer and a balance. Make objects for two accounts held by the same customer.


class Bank_customers:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        



class Bank_accounts(Bank_customers):
    def __init__(self,first_name, last_name,  balance):
        super().__init__(self, first_name, last_name, balance)
        self.balance = balance

customer1 = Bank_customers("Jyoti", "Choudhary")
account1 = Bank_accounts("Jyoti", "Choudhary" , 100000)
account2 = Bank_accounts("Gaby", "Valez", 160000)


