from Characters.main_charcters import Character 

class Enemy(Character):
    def __init__(self, name, health, power, special_move):
        super().__init__(name, health, power, special_move)
        self._last_damage = 0        # ✅ Initialized
        self._last_target = ""       # ✅ Initialized

    def attack(self, opponent):
        damage = self._power
        opponent.take_damage(damage)
        self._last_damage = damage
        self._last_target = opponent.get_name()
        return f"{self._name} attacks {opponent.get_name()} with dark power! Damage: {damage}"

    def get_damage_text(self):
        return f"{self._name} attacks {self._last_target}! Damage: {self._last_damage}"


# Subclass: Demogorgon
class Demogorgon(Enemy):
    def __init__(self, name, health, power, special_move, emoji="🔬"):
        super().__init__(name, health, power, special_move)
        self._emoji = emoji  # ✅ Keep only emoji

    def attack(self, opponent):
        damage = self._power + 5
        opponent.take_damage(damage)
        self._last_damage = damage
        self._last_target = opponent.get_name()
        return f"{self._emoji} {self._name} slashes {opponent.get_name()} with claws! Damage: {damage}"

    def get_damage_text(self):
        return f"{self._emoji} {self._name} {self._special_move} {self._last_target}! Damage: {self._last_damage}"


# Subclass: Mind Flayer
class MindFlayer(Enemy):
    def __init__(self, name, health, power, special_move, emoji="🔬"):
        super().__init__(name, health, power, special_move)
        self._emoji = emoji

    def attack(self, opponent):
        damage = self._power + 8
        opponent.take_damage(damage)
        self._last_damage = damage
        self._last_target = opponent.get_name()
        return f"{self._emoji} {self._name} attacks {opponent.get_name()} with shadow tentacles! Damage: {damage}"

    def get_damage_text(self):
        return f"{self._emoji} {self._name} {self._special_move} {self._last_target}! Damage: {self._last_damage}"


# Subclass: Vecna
class Vecna(Enemy):
    def __init__(self, name, health, power, special_move, emoji="🔬"):
        super().__init__(name, health, power, special_move)
        self._emoji = emoji

    def attack(self, opponent):
        damage = self._power + 6
        opponent.take_damage(damage)
        self._last_damage = damage
        self._last_target = opponent.get_name()
        return f"{self._emoji} {self._name} blasts {opponent.get_name()} with psychic power! Damage: {damage}"

    def get_damage_text(self):
        return f"{self._emoji} {self._name} {self._special_move} {self._last_target}! Damage: {self._last_damage}"
