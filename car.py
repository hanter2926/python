class Car:
    def _init_(self, brand, price):
        self.brand = brand
        self.price = price

car1 = Car("Toyota", 800000)
print("Brand:", car1.brand)
print("Price:", car1.price)
print("self:", car1.self)