from Characters.main_charcters import Character  # ✅ Corrected import path

# Hero Base Class
class Hero(Character):
    def __init__(self, name, health, power, special_move):
        super().__init__(name, health, power, special_move)
        self._last_damage = 0          # ✅ Initialized safely
        self._last_target = ""         # ✅ Initialized safely

    def attack(self, opponent):
        damage = self._power
        opponent.take_damage(damage)
        self._last_damage = damage
        self._last_target = opponent.get_name()
        return f"{self._name} attacks {opponent.get_name()}! Damage: {damage}"

    def get_damage_text(self):
        return f"{self._name} attacked {self._last_target}! Damage: {self._last_damage}"


# Subclass: Eleven
class Eleven(Hero):
    def __init__(self, name, health, power, special_move, emoji="🧠"):
        super().__init__(name, health, power, special_move)
        self._emoji = emoji  # ✅ Keep only emoji here

    def attack(self, opponent):
        damage = self._power + 10
        opponent.take_damage(damage)
        self._last_damage = damage
        self._last_target = opponent.get_name()
        return f"{self._emoji} {self._name} uses {self._special_move} on {opponent.get_name()}! Damage: {damage}"

    def get_damage_text(self):
        return f"{self._emoji} {self._name} used {self._special_move} on {self._last_target}! Damage: {self._last_damage}"


# Subclass: Mike
class Mike(Hero):
    def __init__(self, name, health, power, special_move, emoji="⚔️"):
        super().__init__(name, health, power, special_move)
        self._emoji = emoji

    def attack(self, opponent):
        damage = self._power + 3
        opponent.take_damage(damage)
        self._last_damage = damage
        self._last_target = opponent.get_name()
        return f"{self._emoji} {self._name} strikes {opponent.get_name()} with {self._special_move}! Damage: {damage}"

    def get_damage_text(self):
        return f"{self._emoji} {self._name} struck {self._last_target} with {self._special_move}! Damage: {self._last_damage}"


# Subclass: Dustin
class Dustin(Hero):
    def __init__(self, name, health, power, special_move, emoji="🔬"):
        super().__init__(name, health, power, special_move)
        self._emoji = emoji

    def attack(self, opponent):
        damage = self._power + 2
        opponent.take_damage(damage)
        self._last_damage = damage
        self._last_target = opponent.get_name()
        return f"{self._emoji} {self._name} shocks {opponent.get_name()} with {self._special_move}! Damage: {damage}"

    def get_damage_text(self):
        return f"{self._emoji} {self._name} used {self._special_move} on {self._last_target}! Damage: {self._last_damage}"
