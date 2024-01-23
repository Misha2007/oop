from zoo import Zoo, Animal

if __name__ == '__main__':
    zoo = Zoo("Our zoo", 4)
    animal1 = Animal("Simon", "lion", 9)
    animal2 = Animal("Ott", "lion", 1)
    animal3 = Animal("Mati", "turtle", 51)
    animal4 = Animal("Kati", "turtle", 54)
    animal5 = Animal("Kati", "lion", 5)
    zoo.add_animal(animal1)
    zoo.add_animal(animal2)
    zoo.add_animal(animal3)
    zoo.add_animal(animal4)
    zoo.add_animal(animal5)
    print(zoo.get_all_animals())
    print(zoo.get_animals_by_age())
    print(zoo.get_animals_sorted_alphabetically())