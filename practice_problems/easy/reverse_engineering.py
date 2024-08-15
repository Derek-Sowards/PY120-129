class Transform:
    def __init__(self, letters):
        self.letters = letters
    
    def uppercase(self):
        return self.letters.upper()
    
    @classmethod
    def lowercase(cls, letters):
        return letters.lower()





my_data = Transform('abc')
print(my_data.uppercase())              # ABC
print(Transform.lowercase('XYZ'))       # xyz