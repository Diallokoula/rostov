import csv
class Item:
    pay_rate = 0.8
    all = []
    def __init__(self, name: str, price: float, quantity = 0):
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, n):
        self.__name = n

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.pay_rate})"

    def calculate(self):
        return self.price * self.quantity

    def discount(self):
        self.price = self.price * self.pay_rate
    
    @classmethod
    def instantiation(cls):
        with open("data.csv") as file:
            for item in list(csv.DictReader(file)):
                Item(
                    name = item.get('name'),
                    price = float(item.get("price")),
                    quantity = int(item.get("quantity"))
                    )
                
    @staticmethod
    def isinteger(num):
        if isinstance(num, float):
            return num.is_integer()
        else:
            return True


phone1 = Item("jscPhone10", 500, 5)
phone1.name = "adra"
#phone2 = Phone("jscPhone20", 700, 5, 1)


print(phone1.name)

