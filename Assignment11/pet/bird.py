from pet import Pet


class Bird(Pet):
    def speak(self):
        return "Tweet!"

    def __str__(self):
        return f"{super().__str__()} the Bird says {self.speak()}"
