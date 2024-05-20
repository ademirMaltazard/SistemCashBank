
class BankAcount:
    def __init__(self, titular:str, balance:float = 0):
        self.titular = titular
        self.__balance = balance

    def Deposit(self, amountDeposited:float):
        self.balance = self.balance + amountDeposited
    
    def withdraw(self, amountWithdrawn:float):
        self.balance = self.balance - amountWithdrawn

    def checkBalance(self):
        # retorna um texto com o titular da conta e o valor
        return( f'A conta do titular tem {self.titular} tem R$ {self.__balance}')

contaJoao = BankAcount("Joao Costa", 5000.50)

print(contaJoao.checkBalance())
print(contaJoao.__balance)
print(contaJoao.checkBalance())
