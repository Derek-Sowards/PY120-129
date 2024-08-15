class Wallet:
    def __init__(self, amount):
        self.amount = amount
    
    @property
    def amount(self):
        return self._amount
    
    @amount.setter
    def amount(self, value):
        self._amount = value
    
    def __add__(self, other):
        if not isinstance(other, Wallet):
            return NotImplemented
        return Wallet(self.amount + other.amount)


wallet1 = Wallet(50)
wallet2 = Wallet(30)
merged_wallet = wallet1 + wallet2
print(merged_wallet.amount == 80)       # True