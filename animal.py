# Базовый класс "Animal" для всех животных
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

# Класс "HomeAnimal" представляет домашних животных и наследует от "Animal"
class HomeAnimal(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        pass

# Подклассы домашних животных (собака, кошка, хомяк)
class Dog(HomeAnimal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        return f"{self.name} говорит: Гав-гав!"


class Cat(HomeAnimal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        return f"{self.name} говорит: Мяу-мяу!"


class Hamster(HomeAnimal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        return f"{self.name} говорит: Пи-пи!"

# Класс "PackAnimal" представляет вьючных животных и наследует от "Animal"
class PackAnimal(Animal):
    def __init__(self, name):
        super().__init__(name)

# Подклассы вьючных животных (лошадь, верблюд, осел)
class Horse(PackAnimal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        return f"{self.name} говорит: Иго-го!"


class Camel(PackAnimal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        return f"{self.name} говорит: Ррр-ррр!"


class Donkey(PackAnimal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        return f"{self.name} говорит: Иа-иа!"
