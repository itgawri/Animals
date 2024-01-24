class Pet:
    def __init__(self, pet_type, name, sound):
        self.pet_type = pet_type
        self.name = name
        self.sound = sound

    def speak(self):
        print(f"{self.name} goes {self.sound}!")

    def play(self):
        print(f"{self.name} is playing!")

class Cat(Pet):
    def __init__(self, name, sound, coat_length):
        if isinstance(coat_length, str) and len(coat_length) > 0:
            super().__init__("cat", name, sound)
            self.coat_length = coat_length
        else:
            raise ValueError("Invalid coat_length value.")

    def purr(self):
        print(f"{self.name} is purring.")

class Dog(Pet):
    def __init__(self, name, sound, size):
        super().__init__("dog", name, sound)
        self.size = size

    def speak(self):
        print(f"{self.name} the {self.size} dog goes {self.sound}!")

    def wag_tail(self):
        print(f"{self.name} is wagging its tail")

class Poodle(Dog):
    def __init__(self, name, size):
        super().__init__(name, "Bark", size)
        self.is_hypoallergenic = True

    def groom(self):
        print(f"{self.name} the Poodle is being groomed.")

cat = Cat("Mittens", "Meow", "long")
cat.purr()
cat.speak()
cat.play()
print(cat.coat_length)

dog = Dog("Cruiser", "Woof", "small")
dog.speak()
dog.wag_tail()
dog.play()
print(dog.size)

poodle = Poodle("Fluffy", "medium")
poodle.speak()
poodle.wag_tail()
poodle.play()
poodle.groom()
print(f"Is {poodle.name} hypoallergenic? {poodle.is_hypoallergenic}")
