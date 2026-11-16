from pet import Pet


class Dog(Pet):
    def speak(self):
        return "Woof!"

    def __str__(self):
        return f"{super().__str__()} the Dog says {self.speak()}"
