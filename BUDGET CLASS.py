class Budget:

    welcomeMessage = ("Welcome to your Budget App")
    welcomeMessage = welcomeMessage.center(50, '*')
    print(welcomeMessage + "\n")

    def __init__(self, category):
        self.name = category
        self.balance = 0


    def deposit(self, depositing_amount):
        self.balance += depositing_amount

        feedback = 'Transaction Successful\n'
        feedback += "***************************************\n"
        feedback += f'Your deposit of ${depositing_amount} into {self.name} budget was successful\n'
        feedback += f'Your new balance for {self.name} budget is ${self.balance}\n\n'

        return feedback


    def withdraw(self, withdrawal_amount):

        if self.balance >= withdrawal_amount:
            self.balance -= withdrawal_amount

            feedback = 'Transaction Successful\n'
            feedback += "***************************************\n"
            feedback += f'Your withdrawal of ${withdrawal_amount} from {self.name} budget was successful\n'
            feedback += f'Your new balance for {self.name} budget is ${self.balance}\n\n'

            return feedback

        else:

            return "Insufficient Funds\n\n"


    def category_balance(self):
        feedback = "***************************************\n"
        feedback += f'The current balance for {self.name} budget is ${self.balance} \n'
        feedback += "***************************************\n\n"
        return feedback


    def transfer(self, transfer_amount, recipient_category):

        if self.name == recipient_category.name:

            feedback = "Error!\n"
            feedback += "You cannot transfer within the same category\n"
            feedback += "You can only transfer from a different category to another\n\n"

            return feedback

        if self.balance >= transfer_amount:

            self.balance -= transfer_amount
            recipient_category.balance += transfer_amount

            feedback = 'Transaction Successful\n'
            feedback += "***************************************\n"
            feedback += f'The current balance for {self.name} budget is ${self.balance}\n'
            feedback += f'The current balance for {recipient_category.name} budget is ${recipient_category.balance}\n\n'

            return feedback

        else:
            return "Insufficient Funds"




food = Budget('food')
clothing = Budget('clothing')
entertainment = Budget('entertainment')

food.deposit(5000)
clothing.deposit(10000)
entertainment.deposit(15000)

food.withdraw(2000)
clothing.withdraw(7000)
entertainment.withdraw(10000)

print(food.category_balance())
print(clothing.category_balance())
print(entertainment.category_balance())

print(entertainment.transfer(2500, food))
print(food.transfer(2000, clothing))
print(clothing.transfer(4000, entertainment))

print(food.category_balance())
print(clothing.category_balance())
print(entertainment.category_balance())


