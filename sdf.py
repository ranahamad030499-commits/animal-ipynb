class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def speak(self):
        return f"{self.name} بول رہا ہے: {self.sound}"

class Dog(Animal):
    def __init__(self):
        super().__init__("کتا", "بھوں بھوں")

class Cat(Animal):
    def __init__(self):
        super().__init__("بلی", "میاؤں")

class Horse(Animal):
    def __init__(self):
        super().__init__("گھوڑا", "ہنہناہٹ")

# User choose
print("جانور منتخب کریں:")
print("1. کتا")
print("2. بلی")
print("3. گھوڑا")

choice = input("اپنا انتخاب نمبر میں لکھیں: ")

if choice == "1":
    animal = Dog()
elif choice == "2":
    animal = Cat()
elif choice == "3":
    animal = Horse()
else:
    animal = None

if animal:
    print(animal.speak())
else:
    print("غلط انتخاب ❌")
