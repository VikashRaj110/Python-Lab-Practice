from abc import ABC, abstractmethod
class Account(ABC):
    def __init__(self, accName, accNum, accBalance):
        self.accName = accName
        self.accNum = accNum
        self.accBalance = accBalance

    def deposit(self, amt):
        self.accBalance += amt
        print(f"Deposited: {amt}")

    def display(self):
        print("Account Name :", self.accName)
        print("Account Number :", self.accNum)
        print("Account Balance :", self.accBalance)

    @abstractmethod
    def withdraw(self, amt):
        pass

class Saving(Account):
    MIN_BALANCE = 500

    def __init__(self, accName, accNum, accBalance):
        super().__init__(accName, accNum, accBalance)

    def withdraw(self, amt):
        if self.accBalance - amt >= Saving.MIN_BALANCE:
            self.accBalance -= amt
            print(f"Withdrawn: {amt}")
        else:
            print("Withdrawal denied! Minimum balance must be maintained.")

class Current(Account):
    def __init__(self, accName, accNum, accBalance):
        super().__init__(accName, accNum, accBalance)

    def withdraw(self, amt):
        if amt <= self.accBalance:
            self.accBalance -= amt
            print(f"Withdrawn: {amt}")
        else:
            print("Insufficient balance!")

s1 = Saving("Vikash", 101, 10000)

s1.display()
s1.deposit(2000)
s1.withdraw(3000)
s1.display()