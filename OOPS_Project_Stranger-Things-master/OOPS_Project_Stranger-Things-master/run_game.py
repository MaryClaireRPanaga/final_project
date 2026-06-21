#!/usr/bin/env python3
"""
Stranger Things: Battle for Hawkins - Game Launcher
Choose between the available game versions.
"""

import sys
import os

def check_dependencies():
    """Check if pygame is installed"""
    try:
        import pygame
        print("✅ Pygame is installed!")
        return True
    except ImportError:
        print("❌ Pygame is not installed!")
        print("Please install it using: pip install pygame")
        return False

def main():
    print("=" * 50)
    print("🧪 Stranger Things: Battle for Hawkins")
    print("=" * 50)
    print()
    
    # Check dependencies
    if not check_dependencies():
        input("Press Enter to exit...")
        return
    
    print("Choose your game version:")
    print("1. Basic Version (Simple graphics)")
    print("2. Aesthetic Version (Beautiful design with custom background)")
    print("3. Exit")
    print()
    
    while True:
        try:
            choice = input("Enter your choice (1-3): ").strip()
            
            if choice == "1":
                print("Starting Basic Version...")
                import game_frontend
                game = game_frontend.Game()
                game.run()
                break
            elif choice == "2":
                print("Starting Aesthetic Version...")
                import game_simple_aesthetic
                game = game_simple_aesthetic.Game()
                game.run()
                break
            elif choice == "3":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"Error: {e}")
            print("Please make sure all files are in the same directory.")

if __name__ == "__main__":
    main() 