class Client:
    def __init__(self, name, email, amount, phone):
        self.name = name
        self.email = email
        self.amount = amount
        self.phone = phone

biplob = Client('Monsur Biplob', 'monsur.biplob25@gmail.com', 5000, '01629782123')
print(biplob.name, biplob.email, biplob.amount, biplob.phone)
print(dir(biplob))