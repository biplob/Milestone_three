class Bank:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def withdrow(self, taka):
        self.amount -= taka
        return self.amount
    def deposite(self, taka):
        self.amount += taka
        return self.amount

karim = Bank('Karim Uddin', 1000)
kaisar = Bank('Kasar Ali', 500)
print(karim.withdrow(500))
print(kaisar.deposite(5000))
print(kaisar.amount)