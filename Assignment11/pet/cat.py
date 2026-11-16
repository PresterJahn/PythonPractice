from pet import Pet


class Cat(Pet):
    def speak(self):
        return "Meow!"

    def __str__(self):
        return f"{super().__str__()} the Cat says {self.speak()}"
