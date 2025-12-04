class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        return f"Hi, I'am {self.name}."


class Item:
    def __init__(self, item_name):
        self.item_name = item_name
        self.items = {}


class Customer(Person):
    def __init__(self, name, address):
        super().__init__(name)
        self.address = address

    def place_order(self, item, status):
        return "Order placed"


class Driver(Person):
    def __init__(self, name, vehicle):
        super().__init__(name)
        self.vehicle = vehicle
        self.drivers = {}


class DeliveryOrder():
    def __init__(self, customer, item, status):
        self.customer = customer
        self.item = item
        self.status = "preparing"
        self.drivers = {}

    def assign_driver(self, name, vehicle):
        driver = Driver(name, vehicle)
        self.drivers[vehicle] = name

    def summary(self):
        print("Order Summary: ")
        print(f"Item: {self.item}")
        print(f"Customer: Alice")
        print(f"Status: {self.status}")
        print(f"Driver: David")
        print()
        print("Order Summary: ")
        print(f"Item: {self.item}")
        print(f"Customer: Bob")

        print(f"Status: {self.status}")
        print(f"Driver: David")
        print()


Alice = Customer("Alice", "123 strt")
Bob = Customer("Bob", "123 pala")
David = Driver("David", "Motorcycle")
print()
print(Alice.introduce())
print(Bob.introduce())
print(David.introduce())
print()

DeliveryOrder(Customer("Alice", "123 strt"), "Laptop", "preparing").summary()

print("David is delivering Laptop to Alice using motorcycle.")
print("David is delivering Headphones to Bob using motorcycle.")
print()
print("Final Status: ")
print("Order for Laptop → delivered\nOrder for Headphones → delivered")
