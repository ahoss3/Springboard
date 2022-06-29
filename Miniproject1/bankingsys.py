import logging

logging.basicConfig(level=logging.INFO, filename='test.log')

def _init_logger():
    logger = logging.getLogger('banksys.io')
    logger.setLevel(logging.INFO)  

_init_logger()
_logger = logging.getLogger('banksys.io')

class Bank:
    "Bank object contains an ID so that other objects can link to it"
    def __init__(self, id):
        self.id = id

    def getBankId(self):
        return self.id

class BankAccount:
    "Bank account contains an acct num, the bank id it's linked to, a customer id, and an initial balance which must be positive"
    def __init__(self, number, bank_id, cust_id, balance=0):
        self.number = number
        self.bank_id = bank_id
        self.cust_id = cust_id

        try:
            if balance > 0:
                self.balance = balance
                _logger.info('Successfully created bank account')
            else:
                raise Exception("Only positive balances are allowed")
        except Exception as error:
            print('Balance Error: ' + str(error)+'\n')
            _logger.info('Failed to create bank account')
    
    def withdraw(self, amount):
        "If withdrawal amount is positive, subtract amount from balance, otherwise throw error"
        try:
            if amount > 0:
                self.balance -= amount
                _logger.info('Successfully withdrew')
            else:
                raise Exception("Amount must be a positive number")
        except Exception as error:
            print('Amount Error: ' + str(error)+'\n')
            _logger.info('Failed to withdraw')

    def deposit(self, amount):
        "If deposit amount is positive, add amount to balance, otherwise throw error"
        try:
            if amount > 0:
                self.balance += amount
                _logger.info('Successfully deposited')
            else:
                raise Exception("Amount must be a positive number")
        except Exception as error:
            print('Amount Error: ' + str(error)+'\n')
            _logger.info('Failed to deposit')

    def getAcctNum(self):
        return self.number

    def getBankId(self):
        return self.bank_id

    def getCustId(self):
        return self.cust_id

    def getBalance(self):
        return self.balance

    def __str__(self):
        return """Account number: {}
Bank ID: {} 
Customer ID: {}
Balance: {}""".format(self.number, self.bank_id, self.cust_id, self.balance)

class SavingsAccount(BankAccount):
    "Savings account adds an interest rate to init function, allowing for a compute interest function below"
    def __init__(self, number, bank_id, cust_id, balance, interest_rate):
        BankAccount.__init__(self, number, bank_id, cust_id, balance)
        self.interest_rate = interest_rate

    def compute_interest(self, n_periods=1):
        return self.balance * ((1 + self.interest_rate) ** n_periods-1)

class CheckingAccount(BankAccount):
    "Checking account adds a limit to init function so that the modified withdraw checks to see whether an overdraft fee should be levied"
    def __init__(self, number, bank_id, cust_id, balance, limit):
        BankAccount.__init__(self, number, bank_id, cust_id, balance)
        self.limit = limit

    def withdraw(self, amount, fee=0):
        try:
            if amount > 0:
                if fee <= self.limit:
                    BankAccount.withdraw(self, amount - fee)
                else:
                    BankAccount.withdraw(self, amount - self.limit)
                _logger.info('Successfully withdrew')
            else:
                raise Exception("Amount must be a positive number")
        except Exception as error:
            print('Amount Error: ' + str(error)+'\n')
            _logger.info('Failed to withdraw')

class CreditCard(BankAccount):
    "Credit card account adds an available credit to the init function to check whether or not a purchase is possible"
    def __init__(self, number, bank_id, cust_id, balance, available_credit=10000):
        BankAccount.__init__(self, number, bank_id, cust_id, balance) 
        self.available_credit = available_credit 

    def getAvailableCredit(self):
        return self.available_credit

    def makePurchase(self, amount):
        try:
            if (amount <= self.available_credit):
                self.available_credit -= amount
                self.balance += amount
                _logger.info('Successfully made purchase')
            else:
                raise Exception('Insufficient funds!')
        except Exception as error:
            print('Purchase Error: ' + str(error)+'\n')
            _logger.info('Failed to make purchase')

    def makePayment(self, payment): 
        try:
            if (payment <= self.current_balance):
                self.available_credit += payment
                self.balance -= payment
                _logger.info('Successfully made payment')
            else:
                raise Exception('Payment larger than outstanding balance!')
        except Exception as error:
            print('Payment Error: ' + str(error)+'\n')  
            _logger.info('Failed to make payment')

class Loan(BankAccount):
    "Loan object adds annual interest rate and number of years of the loan in order to calculate monthly payment"
    def __init__(self, number, bank_id, cust_id, balance, annualInterestRate, numberOfYears):
        BankAccount.__init__(self, number, bank_id, cust_id, balance)
        self.annualInterestRate = annualInterestRate
        self.numberOfYears = numberOfYears
        self.balance = balance

    def getannualInterestRate(self):
        return self.annualInterestRate

    def getnumberOfYears(self):
        return self.numberOfYears

    def getbalance(self):
        return self.balance

    def getcustomer(self):
        return self.cust_id

    def setannualInterestRate(self, annualInterestRate):
        self.annualInterestRate = annualInterestRate

    def setnumberOfYears(self, numberOfYears):
        self.numberOfYears = numberOfYears

    def getMonthlyPayment(self, balance, monthlyInterestRate, numberOfYears):
        monthlyPayment = balance * monthlyInterestRate / (1
        - 1 / (1 + monthlyInterestRate) ** (numberOfYears * 12))
        return monthlyPayment

class Customer:
    "Customer is linked to a bank"
    def __init__(self, id, bank_id, first_name, last_name, address):
        self.id = id
        self.bank_id = bank_id
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
    
    def __str__(self):
        return """Customer ID: {}
Customer first name: {} 
Customer last name: {}
Customer address: {}""".format(self.id, self.first_name, self.last_name, self.address, self.balance)

class Employee:
    "Employee is linked to a bank"
    def __init__(self, id, bank_id, first_name, last_name, salary):
        self.id = id
        self.bank_id = bank_id
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def __str__(self):
        return """Employee ID: {}
Employee first name: {} 
Employee last name: {}
Employee salary: {}""".format(self.id, self.first_name, self.last_name)