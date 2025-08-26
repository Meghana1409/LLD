

'''
Pros and Cons:
 You avoid tight coupling between the creator and the concrete products.
 Single Responsibility Principle. You can move the product creation code into one place in the program, making the code easier to support.
 Open/Closed Principle. You can introduce new types of products into the program without breaking existing client code.
 The code may become more complicated since you need to introduce a lot of new subclasses to implement the pattern. The best case scenario is when you’re introducing the pattern into an existing hierarchy of creator classes.
 '''


class FrenchLocalizer:
    def __init__(self):
        self.translations = {"car": "voiture", "bike": "bicyclette",
                             "cycle":"cyclette"}
    def localize(self, msg):
        return self.translations.get(msg, msg)

class SpanishLocalizer:
    def __init__(self):
        self.translations = {"car": "coche", "bike": "bicicleta",
                             "cycle":"ciclo"}
    def localize(self, msg):
        return self.translations.get(msg, msg)

class EnglishLocalizer:
    def localize(self, msg):
        return msg

if __name__ == "__main__":

    # main method to call others
    f = FrenchLocalizer()
    e = EnglishLocalizer()
    s = SpanishLocalizer()

    # list of strings
    message = ["car", "bike", "cycle"]

    for msg in message:
        print(f.localize(msg))
        print(e.localize(msg))
        print(s.localize(msg))

#solution

class FrenchLocalizer:
    def __init__(self):
        self.translations = {"car": "voiture", "bike": "bicyclette",
                             "cycle":"cyclette"}
    def localize(self, msg):
        return self.translations.get(msg, msg)

class SpanishLocalizer:
    def __init__(self):
        self.translations = {"car": "coche", "bike": "bicicleta",
                             "cycle":"ciclo"}
    def localize(self, msg):
        return self.translations.get(msg, msg)

class EnglishLocalizer:
    def localize(self, msg):
        return msg

def Factory(language ="English"):
    localizers = {
        "French": FrenchLocalizer,
        "English": EnglishLocalizer,
        "Spanish": SpanishLocalizer,
    }

    return localizers[language]()

if __name__ == "__main__":

    f = Factory("French")
    e = Factory("English")
    s = Factory("Spanish")

    message = ["car", "bike", "cycle"]

    for msg in message:
        print(f.localize(msg))
        print(e.localize(msg))
        print(s.localize(msg))
