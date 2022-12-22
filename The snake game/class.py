class Dog:
    def __init__(self, name, year_of_birth, breed):
        self._name = name
        self._year_of_birth = year_of_birth
        self._breed = breed
    def __str__(self):
        return "%s is a %s born in %d" % (self._name, self._breed, self._year_of_birth)

