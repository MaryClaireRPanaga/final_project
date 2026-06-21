import pygame
import sys
import os
import random
import math
from Characters.heroes import Eleven, Dustin, Mike
from Characters.enemies import Demogorgon, MindFlayer, Vecna

# Initialize Pygame
pygame.init()
pygame.mixer.init()

# Game Constants
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
FPS = 100

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (220, 20, 60)
GREEN = (34, 139, 34)
BLUE = (30, 144, 255)
YELLOW = (255, 215, 0)
ORANGE = (255, 140, 0)
DARK_BLUE = (25, 25, 112)
LIGHT_BLUE = (173, 216, 230)
DARK_GRAY = (40, 40, 40)
LIGHT_GRAY = (200, 200, 200)

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Stranger Things: Battle for Hawkins")
        self.clock = pygame.time.Clock()
        self.running = True
        self.game_state = "menu"
        
        # Game objects
        self.heroes = []
        self.enemies = []
        self.battle_log = []
        self.current_turn = 1
        self.game_over = False
        self.winner = None
        
        # UI elements
        self.buttons = {}
        self.button_hover = {}
        self.create_ui()
        
        # Load assets
        self.load_assets()
        
        # Animation
        self.menu_timer = 0
        
    def load_assets(self):
        """Load game assets"""
        self.assets_dir = "Assets"
        
        # Load character images
        self.character_images = {}
        character_files = {
            'eleven': 'eleven.png',
            'dustin': 'dustin.png', 
            'mike': 'mike.png',
            'demogorgon': 'demogorgon.png',
            'mindflayer': 'mindflayer.png',
            'vecna': 'vecna.png'
        }
        
        for name, filename in character_files.items():
            try:
                path = os.path.join(self.assets_dir, filename)
                if os.path.exists(path):
                    img = pygame.image.load(path)
                    self.character_images[name] = pygame.transform.scale(img, (100, 100))
                else:
                    self.character_images[name] = self.create_placeholder(name)
            except:
                self.character_images[name] = self.create_placeholder(name)
        
        # Create background
        self.background = self.create_background()
        
        # Load sounds
        self.sounds = {}
        try:
            punch_path = os.path.join(self.assets_dir, 'punch.wav')
            if os.path.exists(punch_path):
                self.sounds['punch'] = pygame.mixer.Sound(punch_path)
            else:
                self.sounds['punch'] = None
                
            music_path = os.path.join(self.assets_dir, 'background_music.mp3')
            if os.path.exists(music_path):
                pygame.mixer.music.load(music_path)
                pygame.mixer.music.set_volume(0.3)
        except:
            self.sounds['punch'] = None
            
        # Load fonts
        self.fonts = {
            'title': pygame.font.Font(None, 72),
            'large': pygame.font.Font(None, 48),
            'medium': pygame.font.Font(None, 32),
            'small': pygame.font.Font(None, 24)
        }
    
    def create_placeholder(self, name):
        """Create character placeholder"""
        surface = pygame.Surface((100, 100))
        surface.fill(DARK_BLUE)
        
        emojis = {
            'eleven': '👩‍🔬',
            'dustin': '🧢', 
            'mike': '⚔️',
            'demogorgon': '👹',
            'mindflayer': '🕷️',
            'vecna': '🧠'
        }
        
        font = pygame.font.Font(None, 40)
        text = font.render(emojis.get(name, '?'), True, WHITE)
        text_rect = text.get_rect(center=(50, 50))
        surface.blit(text, text_rect)
        
        return surface
    
    def create_background(self):
        """Create beautiful background"""
        surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        
        # Gradient background
        for y in range(SCREEN_HEIGHT):
            ratio = y / SCREEN_HEIGHT
            r = int(15 + ratio * 25)
            g = int(15 + ratio * 20)
            b = int(35 + ratio * 45)
            pygame.draw.line(surface, (r, g, b), (0, y), (SCREEN_WIDTH, y))
        
        # Add stars
        for _ in range(200):
            x = random.randint(0, SCREEN_WIDTH)
            y = random.randint(0, SCREEN_HEIGHT)
            brightness = random.randint(50, 200)
            color = (brightness, brightness, brightness)
            pygame.draw.circle(surface, color, (x, y), random.randint(1, 2))
        
        return surface
    
    def create_ui(self):
        """Create UI buttons"""
        button_width = 200
        button_height = 50
        center_x = SCREEN_WIDTH // 2
        
        self.buttons = {
            'start': pygame.Rect(center_x - button_width//2, 300, button_width, button_height),
            'next_turn': pygame.Rect(center_x - button_width//2, 700, button_width, button_height),
            'reset': pygame.Rect(center_x - button_width//2, 750, button_width, button_height),
            'sound': pygame.Rect(SCREEN_WIDTH - 70, 20, 50, 30)
        }
        
        for button_name in self.buttons:
            self.button_hover[button_name] = False
    
    def initialize_game(self):
        """Initialize the game"""
        # Create Hero Instances
        hero1 = Eleven("Eleven", health=100, power=30, special_move="Telekinesis", emoji="👩‍🔬")
        hero2 = Dustin("Dustin", health=90, power=25, special_move="Sonic Boom Gadget", emoji="🧢")
        hero3 = Mike("Mike", health=85, power=22, special_move="Sword Strike", emoji="⚔️")

        # Create Enemy Instances
        enemy1 = Demogorgon("Demogorgon", health=100, power=20, special_move="Claw Slash", emoji="👹")
        enemy2 = MindFlayer("Mind Flayer", health=110, power=28, special_move="Shadow Tentacles", emoji="🕷️")
        enemy3 = Vecna("Vecna", health=95, power=26, special_move="Psychic Blast", emoji="🧠")

        self.heroes = [hero1, hero2, hero3]
        self.enemies = [enemy1, enemy2, enemy3]
        self.current_turn = 1
        self.battle_log = []
        self.game_over = False
        self.winner = None
        self.game_state = "playing"
        
        # Start music
        try:
            pygame.mixer.music.play(-1)
        except:
            pass
    
    def handle_events(self):
        """Handle pygame events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                
                if self.game_state == "menu":
                    if self.buttons['start'].collidepoint(mouse_pos):
                        self.initialize_game()
                
                elif self.game_state == "playing":
                    if self.buttons['next_turn'].collidepoint(mouse_pos):
                        self.process_turn()
                    elif self.buttons['reset'].collidepoint(mouse_pos):
                        self.game_state = "menu"
                
                elif self.game_state == "game_over":
                    if self.buttons['reset'].collidepoint(mouse_pos):
                        self.game_state = "menu"
            
            elif event.type == pygame.MOUSEMOTION:
                mouse_pos = pygame.mouse.get_pos()
                for button_name, button_rect in self.buttons.items():
                    self.button_hover[button_name] = button_rect.collidepoint(mouse_pos)
    
    def process_turn(self):
        """Process one turn of battle"""
        if self.game_over:
            return
        
        # Heroes Attack
        for hero in self.heroes[:]:
            if self.enemies:
                target = random.choice(self.enemies)
                attack_text = hero.attack(target)
                self.battle_log.append(f"Turn {self.current_turn} - {hero.get_name()} attacks {target.get_name()}")
                self.battle_log.append(attack_text)
                self.battle_log.append(f"{target.get_name()} takes {hero.get_power()} damage. (HP: {target.get_health()})")
                
                # Play sound
                if self.sounds.get('punch'):
                    self.sounds['punch'].play()
                
                if not target.is_alive():
                    self.battle_log.append(f"{target.get_name()} has been defeated!")
                    self.enemies.remove(target)
        
        # Enemies Attack
        for enemy in self.enemies[:]:
            if self.heroes:
                target = random.choice(self.heroes)
                attack_text = enemy.attack(target)
                self.battle_log.append(f"Turn {self.current_turn} - {enemy.get_name()} attacks {target.get_name()}")
                self.battle_log.append(attack_text)
                self.battle_log.append(f"{target.get_name()} takes {enemy.get_power()} damage. (HP: {target.get_health()})")
                
                # Play sound
                if self.sounds.get('punch'):
                    self.sounds['punch'].play()
                
                if not target.is_alive():
                    self.battle_log.append(f"{target.get_name()} has been knocked out!")
                    self.heroes.remove(target)
        
        self.current_turn += 1
        
        # Check if battle is over
        if not self.heroes:
            self.game_over = True
            self.winner = "Enemies"
            self.battle_log.append("ENEMIES WIN! The Upside Down has taken over.")
            self.game_state = "game_over"
        elif not self.enemies:
            self.game_over = True
            self.winner = "Heroes"
            self.battle_log.append("HEROES WIN! Hawkins is safe... for now.")
            self.game_state = "game_over"
    
    def draw_button(self, button_name, text, color, hover_color):
        """Draw a button"""
        if button_name not in self.buttons:
            return
            
        button_rect = self.buttons[button_name]
        is_hovered = self.button_hover.get(button_name, False)
        
        bg_color = hover_color if is_hovered else color
        pygame.draw.rect(self.screen, bg_color, button_rect, border_radius=10)
        pygame.draw.rect(self.screen, WHITE, button_rect, 2, border_radius=10)
        
        text_surf = self.fonts['medium'].render(text, True, BLACK)
        text_rect = text_surf.get_rect(center=button_rect.center)
        self.screen.blit(text_surf, text_rect)
    
    def draw_menu(self):
        """Draw the main menu"""
        self.screen.blit(self.background, (0, 0))
        
        # Animated title
        self.menu_timer += 1
        title_y_offset = math.sin(self.menu_timer * 0.02) * 10
        
        # Title
        title = self.fonts['title'].render("Stranger Things", True, WHITE)
        title_rect = title.get_rect(center=(SCREEN_WIDTH//2, 150 + title_y_offset))
        self.screen.blit(title, title_rect)
        
        # Subtitle
        subtitle = self.fonts['large'].render("Battle for Hawkins", True, LIGHT_BLUE)
        subtitle_rect = subtitle.get_rect(center=(SCREEN_WIDTH//2, 220 + title_y_offset))
        self.screen.blit(subtitle, subtitle_rect)
        
        # Description
        desc = self.fonts['medium'].render("Join forces with Eleven, Mike & Dustin", True, LIGHT_GRAY)
        desc_rect = desc.get_rect(center=(SCREEN_WIDTH//2, 280 + title_y_offset))
        self.screen.blit(desc, desc_rect)
        
        # Start button
        self.draw_button('start', "🎮 Start Battle", GREEN, (0, 200, 0))
    
    def draw_battlefield(self):
        """Draw the battlefield"""
        self.screen.blit(self.background, (0, 0))
        
        # Draw heroes (left side)
        hero_y = 200
        for i, hero in enumerate(self.heroes):
            x = 150
            y = hero_y + i * 150
            
            # Character image
            img_name = hero.get_name().lower()
            if img_name in self.character_images:
                self.screen.blit(self.character_images[img_name], (x, y))
            
            # Character info
            name_text = self.fonts['medium'].render(hero.get_name(), True, GREEN)
            self.screen.blit(name_text, (x + 120, y))
            
            # Health bar
            health_ratio = hero.get_health() / 100
            bar_width = 150
            bar_height = 20
            pygame.draw.rect(self.screen, RED, (x + 120, y + 40, bar_width, bar_height))
            pygame.draw.rect(self.screen, GREEN, (x + 120, y + 40, bar_width * health_ratio, bar_height))
            
            # Health text
            health_text = self.fonts['small'].render(f"HP: {hero.get_health()}/100", True, WHITE)
            self.screen.blit(health_text, (x + 120, y + 65))
            
            # Power text
            power_text = self.fonts['small'].render(f"Power: {hero.get_power()}", True, WHITE)
            self.screen.blit(power_text, (x + 120, y + 85))
        
        # Draw enemies (right side)
        enemy_y = 200
        for i, enemy in enumerate(self.enemies):
            x = SCREEN_WIDTH - 250
            y = enemy_y + i * 150
            
            # Character image
            img_name = enemy.get_name().lower().replace(' ', '')
            if img_name in self.character_images:
                self.screen.blit(self.character_images[img_name], (x, y))
            
            # Character info
            name_text = self.fonts['medium'].render(enemy.get_name(), True, RED)
            self.screen.blit(name_text, (x + 120, y))
            
            # Health bar
            max_health = 110 if enemy.get_name() == "Mind Flayer" else 100
            health_ratio = enemy.get_health() / max_health
            bar_width = 150
            bar_height = 20
            pygame.draw.rect(self.screen, RED, (x + 120, y + 40, bar_width, bar_height))
            pygame.draw.rect(self.screen, GREEN, (x + 120, y + 40, bar_width * health_ratio, bar_height))
            
            # Health text
            health_text = self.fonts['small'].render(f"HP: {enemy.get_health()}/{max_health}", True, WHITE)
            self.screen.blit(health_text, (x + 120, y + 65))
            
            # Power text
            power_text = self.fonts['small'].render(f"Power: {enemy.get_power()}", True, WHITE)
            self.screen.blit(power_text, (x + 120, y + 85))
        
        # Draw turn counter
        turn_text = self.fonts['large'].render(f"Turn: {self.current_turn}", True, YELLOW)
        self.screen.blit(turn_text, (SCREEN_WIDTH//2 - 50, 50))
        
        # Draw buttons
        if not self.game_over:
            self.draw_button('next_turn', "⚔️ Next Turn", BLUE, (0, 100, 255))
        
        self.draw_button('reset', "🔄 Reset Game", ORANGE, (255, 100, 0))
    
    def draw_battle_log(self):
        """Draw the battle log"""
        log_surface = pygame.Surface((SCREEN_WIDTH - 100, 200))
        log_surface.fill(BLACK)
        log_surface.set_alpha(200)
        
        # Draw log entries
        y_offset = 10
        for i, entry in enumerate(self.battle_log[-10:]):
            if y_offset < 180:
                if "attacks" in entry:
                    color = YELLOW
                elif "takes" in entry:
                    color = ORANGE
                elif "defeated" in entry or "knocked out" in entry:
                    color = RED
                elif "WIN" in entry:
                    color = GREEN
                else:
                    color = WHITE
                
                text = self.fonts['small'].render(entry, True, color)
                log_surface.blit(text, (10, y_offset))
                y_offset += 20
        
        self.screen.blit(log_surface, (50, 550))
    
    def draw_game_over(self):
        """Draw game over screen"""
        self.screen.blit(self.background, (0, 0))
        
        if self.winner == "Heroes":
            title = self.fonts['title'].render("🏆 HEROES WIN!", True, GREEN)
            subtitle = self.fonts['large'].render("Hawkins is safe... for now.", True, LIGHT_BLUE)
        else:
            title = self.fonts['title'].render("💀 ENEMIES WIN!", True, RED)
            subtitle = self.fonts['large'].render("The Upside Down has taken over.", True, ORANGE)
        
        title_rect = title.get_rect(center=(SCREEN_WIDTH//2, 300))
        subtitle_rect = subtitle.get_rect(center=(SCREEN_WIDTH//2, 400))
        
        self.screen.blit(title, title_rect)
        self.screen.blit(subtitle, subtitle_rect)
        
        # Reset button
        self.draw_button('reset', "🎮 Play Again", ORANGE, (255, 100, 0))
    
    def draw(self):
        """Main draw function"""
        if self.game_state == "menu":
            self.draw_menu()
        elif self.game_state == "playing":
            self.draw_battlefield()
            self.draw_battle_log()
        elif self.game_state == "game_over":
            self.draw_game_over()
        
        pygame.display.flip()
    
    def run(self):
        """Main game loop"""
        while self.running:
            self.handle_events()
            self.draw()
            self.clock.tick(FPS)
        
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    try:
        game = Game()
        game.run()
    except Exception as e:
        print(f"Game crashed with error: {e}")
        import traceback
        traceback.print_exc()
        input("Press Enter to exit...") 