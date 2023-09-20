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

# PL----------------------------------------------------------------------

class Zwierze:
    def __init__(self, typ, imie, dzwiek):
        self.typ = typ
        self.imie = imie
        self.dzwiek = dzwiek

    def mow(self):
        print(f"{self.imie} wydaję dźwięk: {self.dzwiek}!")

    def baw_sie(self):
        print(f"{self.imie} bawi się!")

class Kot(Zwierze):
    def __init__(self, imie, dzwiek, dlugosc_siersci):
        if isinstance(dlugosc_siersci, str) and len(dlugosc_siersci) > 0:
            super().__init__("kot", imie, dzwiek)
            self.dlugosc_siersci = dlugosc_siersci
        else:
            raise ValueError("Nieprawidłowa długość futra.")

    def mrucz(self):
        print(f"{self.imie} mruczy.")

class Pies(Zwierze):
    def __init__(self, imie, dzwiek, rozmiar):
        super().__init__("pies", imie, dzwiek)
        self.rozmiar = rozmiar

    def mow(self):
        print(f"{self.imie} pies rasy {self.rozmiar} wydaje dzwiek: {self.dzwiek}!")

    def merdaj_ogonem(self):
        print(f"{self.imie} merda ogonem.")

class Pudel(Pies):
    def __init__(self, imie, rozmiar):
        super().__init__(imie, "Szczek", rozmiar)
        self.jest_hipoalergiczny = True

    def pielegnacja(self):
        print(f"{self.imie} pudel jest pielęgnowany.")

kot = Kot("Mruczek", "Miau", "długi")
kot.mrucz()
kot.mow()
kot.baw_sie()
print(kot.dlugosc_siersci)

pies = Pies("Burek", "Hau", "mały")
pies.mow()
pies.merdaj_ogonem()
pies.baw_sie()
print(pies.rozmiar)

pudel = Pudel("Pufek", "średni")
pudel.mow()
pudel.merdaj_ogonem()
pudel.baw_sie()
pudel.pielegnacja()
print(f"Czy {pudel.imie} jest hipoalergiczny? {pudel.jest_hipoalergiczny}")
