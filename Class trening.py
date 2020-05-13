class Animal:
    common_weight = 0
    hevy_animels = []
    hevy_animels_name = []

    def __init__(self, name, noise, weight):
        self.name = name
        self.weight = weight
        self.noise = noise
        Animal.common_weight += weight
        Animal.hevy_animels.append(self.weight)
        Animal.hevy_animels_name.append(self.name)


class animals(Animal):
    def Nickname(self):
        print(f'Звать: {self.name}')

    def makeNoise(self):
        print(f'Издает звуки: {self.noise}')

    def Weight(self):
        print(f'Вес: {self.weight} кг')

    def feed(self):
        self.action = 'Кормить'
        print(f'{self.action}')


class Goose(animals):
    def Pick_eggs(self):
        self.action = 'Собирать яйца'
        print(f'{self.action}')


class Cow(animals):
    def Milk(self):
        self.action = 'Доить'
        print(f'{self.action}')


class Sheep(animals):
    def Shearing(self):
        self.action = 'Стрич'
        print(f'{self.action}')


class Chicken(Goose, animals):
    pass


class Goat(Cow, animals):
    pass


class Duck(Goose, animals):
    pass



goose_1 = Goose('Белый', 'Гагочет', 7)
goose_2 = Goose('Серый', 'Гагочат', 8)
cow = Cow('Манька', 'Мычит', 400)
sheep_1 = Sheep('Барашек', 'Бекает', 90)
sheep_2 = Sheep('Кудрявый', 'Бекает', 100)
chicken_1 = Chicken('Ко-Ко', 'Кукарекают', 1)
chicken_2 = Chicken('Кукареку', 'Кукарекают', 3)
goat_1 = Goat('Рога', 'Мекает', 50)
goat_2 = Goat('Копыта', 'Мекает', 40)
duck = Duck('Кряква', 'Крякает', 9)

print('Гусь первый:')
goose_1.Nickname()
goose_1.makeNoise()
goose_1.Weight()
goose_1.feed()
goose_1.Pick_eggs()
print('Гусь второй:')
goose_2.Nickname()
goose_2.makeNoise()
goose_2.Weight()
goose_2.feed()
goose_2.Pick_eggs()
print('Корова:')
cow.Nickname()
cow.makeNoise()
cow.Weight()
cow.feed()
cow.Milk()
print('Овца первая')
sheep_1.Nickname()
sheep_1.makeNoise()
sheep_1.Weight()
sheep_1.feed()
sheep_1.Shearing()
print('Овца вторая')
sheep_2.Nickname()
sheep_2.makeNoise()
sheep_2.Weight()
sheep_2.feed()
sheep_2.Shearing()
print('Курица первая')
chicken_1.Nickname()
chicken_1.makeNoise()
chicken_1.Weight()
chicken_1.feed()
chicken_1.Pick_eggs()
print('Курица вторая')
chicken_2.Nickname()
chicken_2.makeNoise()
chicken_2.Weight()
chicken_2.feed()
chicken_2.Pick_eggs()
print('Козел первый')
goat_1.Nickname()
goat_1.makeNoise()
goat_1.Weight()
goat_1.feed()
goat_1.Milk()
print('Козел второй')
goat_2.Nickname()
goat_2.makeNoise()
goat_2.Weight()
goat_2.feed()
goat_2.Milk()
print('Утка')
duck.Nickname()
duck.makeNoise()
duck.Weight()
duck.feed()
duck.Pick_eggs()

print('Общий вес животных: %d' % Animal.common_weight)
dictionary_animals_merge = dict(zip(Animal.hevy_animels, Animal.hevy_animels_name))
max_weight = max(Animal.hevy_animels)
heavy_anim = dictionary_animals_merge[max_weight]
print(f'Самое тяжелое животное: {heavy_anim}, весит: {max_weight} кг')
