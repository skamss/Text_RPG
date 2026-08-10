class Character:
    def __init__(self, name, hp, max_hp, attack, defense):
        self.name = name
        self.hp = hp
        self.max_hp = max_hp
        self.attack = attack
        self.defense = defense

    @property
    def is_alive(self):
        return self.hp > 0

    def take_damage(self, amount):
        clear_damage = max(1, amount - self.defense)
        self.hp = max(0, self.hp - clear_damage)
        print(f'{self.name} takes {clear_damage} damage! [HP: {self.hp}/{self.max_hp}]')

    def __str__(self):
        return f'{self.name} [HP: {self.hp}/{self.max_hp}]'

class Player(Character):
    def __init__(self, name, hp, max_hp, attack, defense):
        super().__init__(name, hp, max_hp, attack, defense)
        self.level = 1
        self.experience = 0
        self.inventory = []