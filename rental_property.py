class Rental_Property():
    def __init__(self):
        self.income = 0
        self.expenses = {}
        self.total_expenses = 0
        self.cash_flow = 0
        self.cash_ROI = None

    def rent(self):
        rent_charge = int(input("What do you charge per month to rent a unit?  "))
        rooms_rented = int(input("How many rooms does the unit have?  "))
        self.income = rent_charge * rooms_rented
        print(f"\nYour monthly income from rent is ${self.income}")

    def expense_calc(self):
        while True:
        
            possible_expense = input("Do you have any expenses on this property? (yes: 1 no: 2)  ")

            if possible_expense.lower() == '1':
                expense_name = input("What is the name of the expense?  ")
                self.expenses[expense_name] = int(input("How much does this cost you per month?  "))
                self.total_expenses = sum(self.expenses.values())
                self.cash_flow = self.income - self.total_expenses
            elif possible_expense.lower() == '2':
                break
            else:
                print('This is not a valid option')
        print(f"Your expense list is: {self.expenses}")
        print(f"\nYour total expenses per month are ${self.total_expenses}")
        print(f"\nYour monthly cash-flow is ${self.cash_flow}")

    def cashROI(self):
        total_investment = int(input("What was your total investment on this property?  "))
        self.cash_flow = self.income - self.total_expenses
        self.cash_ROI = ((self.cash_flow * 12) / total_investment) *100
        print(f"\nYour cash on cash return on investment is %{self.cash_ROI} a year")

my_duplex = Rental_Property()

def run():
    while True:
        action = input("""
        What would you like to do?
        -Calculate your monthly income: (1)
        -Add to your expense list: (2)
        -Calculate your yearly ROI: (3)
        -Exit the app: (4)
        """)
        if action.lower() == '1':
            my_duplex.rent()
        elif action.lower() == '2':
            my_duplex.expense_calc()
        elif action.lower() == '3':
            my_duplex.rent()
            my_duplex.expense_calc()
            my_duplex.cashROI()
        elif action.lower() == '4':
            break
        else:
            print("This is not a valid response")
run()