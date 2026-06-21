from Characters.heroes import Eleven, Dustin, Mike
from Characters.enemies import Demogorgon, MindFlayer, Vecna 

import random

class BattleManager:
    def __init__(self, heroes, enemies, battle_logs):
        self.heroes = heroes
        self.enemies = enemies
        self.battle_logs = battle_logs


    def run_battle(self):
        print("🎮 The Battle Begins: Hawkins vs The Upside Down\n")

        turn = 1
        while self.heroes and self.enemies:
            print(f"🔁 Turn {turn}\n")

            # Heroes Attack
            for hero in self.heroes[:]:  # [:] to avoid iteration errors on removal
                if self.enemies:
                    target = random.choice(self.enemies)
                    print(hero.attack(target))  # Print attack text
                    print(f"💥 {target.get_name()} takes {hero.get_power()} damage. (HP left: {target.get_health()})\n")

                    if not target.is_alive():
                        print(f"❌ {target.get_name()} has been defeated!\n")
                        self.enemies.remove(target)

            # Enemies Attack
            for enemy in self.enemies[:]:  # [:] for safe iteration
                if self.heroes:
                    target = random.choice(self.heroes)
                    print(enemy.attack(target))
                    print(f"💥 {target.get_name()} takes {enemy.get_power()} damage. (HP left: {target.get_health()})\n")

                    if not target.is_alive():
                        print(f"❌ {target.get_name()} has been knocked out!\n")
                        self.heroes.remove(target)

            print()
            turn += 1
    
        # Battle End
        if self.heroes:
            print("🏆 HEROES WIN! Hawkins is safe... for now.")
        else:
            print("💀 ENEMIES WIN! The Upside Down has taken over.")

    def is_battle_over(self):
        return all(hero.is_defeated() for hero in self.heroes) or all(enemy.is_defeated() for enemy in self.enemies)
    
    def get_winner_text(self):
        if all(hero.is_defeated() for hero in self.heroes):
            return "💀 Enemies win!"
        elif all(enemy.is_defeated() for enemy in self.enemies):
            return "🎉 Heroes win!"
        else:
            return ""