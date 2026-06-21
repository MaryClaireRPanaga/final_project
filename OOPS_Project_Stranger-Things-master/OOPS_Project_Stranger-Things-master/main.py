from Characters.heroes import Eleven, Dustin, Mike
from Characters.enemies import Demogorgon, MindFlayer, Vecna
from battle_manager import BattleManager

# Create Hero Instances
hero1 = Eleven("Eleven", health=100, power=30, special_move="Telekinesis", emoji="👩‍🔬")
hero2 = Dustin("Dustin", health=90, power=25, special_move="Sonic Boom Gadget", emoji="🧢")
hero3 = Mike("Mike", health=85, power=22, special_move="Sword Strike", emoji="⚔️")

# Create Enemy Instances
enemy1 = Demogorgon("Demogorgon", health=100, power=20, special_move="Claw Slash", emoji="👹")
enemy2 = MindFlayer("Mind Flayer", health=110, power=28, special_move="Shadow Tentacles", emoji="🕷️")
enemy3 = Vecna("Vecna", health=95, power=26, special_move="Psychic Blast", emoji="🧠")

# Group heroes and enemies
heroes = [hero1, hero2, hero3]
enemies = [enemy1, enemy2, enemy3]
battle_logs = []

# Run Battle
manager = BattleManager(heroes, enemies, battle_logs)
manager.run_battle()
