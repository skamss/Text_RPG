# Character

class Character:
    def __init__(self, name_character,class_character,
                 hp_character, mp_character, attributes_character, armor_character,
                 damage_character,crit_chance_character, crit_damage_character,
                 experience_character, level_character,weapon_character):
        self.name_character = name_character
        self.class_character = class_character
        self.hp_character = hp_character
        self.mp_character = mp_character
        self.attributes_character = attributes_character
        self.armor_character = armor_character
        self.damage_character = damage_character
        self.crit_chance_character = crit_chance_character
        self.crit_damage_character = crit_damage_character
        self.experience_character = experience_character
        self.level_character = level_character
        self.weapon_character = weapon_character

    weapon_equipped = False

    def equip_weapon(self, weapon: Sword):
        if not self.weapon_equipped:
            self.weapon_character = weapon
            self.damage_character = self.damage_character + weapon.damage_sword
            self.crit_chance_character = self.crit_chance_character + weapon.crit_chance_sword
            self.crit_damage_character = self.crit_damage_character + weapon.crit_damage_sword
            self.weapon_equipped = True
        else:
            print('Weapon already equipped')

    def unequip_weapon(self, weapon: Sword):
        self.weapon_character = 'Empty'
        self.damage_character = self.damage_character - weapon.damage_sword
        self.crit_chance_character = self.crit_chance_character - weapon.crit_chance_sword
        self.crit_damage_character = self.crit_damage_character - weapon.crit_damage_sword

    def character_list(self):
        return (f'Name:{self.name_character} \nClass: {self.class_character}'
                f'\nHP: {self.hp_character} \nMP: {self.mp_character} \nAttributes: {self.attributes_character}'
                f'\nArmor: {self.armor_character} \nDamage: {self.damage_character}'
                f'\nCrit chance: {self.crit_chance_character} \nCrit damage: {self.crit_damage_character}'
                f'\nExperience: {self.experience_character} \nLevel: {self.level_character}'
                f'\nSword: {self.weapon_character}')

# Warrior

Warrior = Character('Warrior_name','Warrior', 50, 10,
                    {'Strength' : 10, 'Agility' : 5, 'Intelligence' : 3}, 10,
                    5, 5, 1.25,
                    0, 1,'Empty')


# Equipments

class Sword:
    def __init__(self,name_sword, damage_sword, crit_chance_sword, crit_damage_sword):
        self.name_sword = name_sword
        self.damage_sword = damage_sword
        self.crit_chance_sword = crit_chance_sword
        self.crit_damage_sword = crit_damage_sword

    def __str__(self):
        return self.name_sword

class Armor:
    def __init__(self,name_armor,value_armor, hp_armor):
        self.name_armor = name_armor
        self.value_armor = value_armor
        self.hp_armor = hp_armor

    def __str__(self):
        return self.name_armor

warrior_sword = Sword('Warrior_sword',10, 5, 0.25 )
warrior_armor = Armor('Warrior_armor',10, 5)

print(Warrior.character_list())
Warrior.equip_weapon(warrior_sword)
Warrior.equip_weapon(warrior_sword)
Warrior.equip_weapon(warrior_sword)
print()
print(Warrior.character_list())
print()
Warrior.unequip_weapon(warrior_sword)
print(Warrior.character_list())

