# Write a program in which a class named Account has private member variables named
# account_no ,account_bal ,security_code. Use a public function to initialize the variables and
# print all data.

class Account:
    def __init__(self, account_no, account_bal, security_code):
        self.__account_no = account_no
        self.__account_bal = account_bal
        self.__security_code = security_code

    def info(self):
        print(
            f"Account#: {self.__account_no}",
            f"Balance: {self.__account_bal}",
            f"Security Code: {self.__security_code}",
            sep='\n'
        )

Account(123, 5000, '1234').info()