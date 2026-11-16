class Pet:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return ""

    def __str__(self):
        return self.name
