import random
class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 20
        self.super_power_used = False

    def attack(self, other):
        other.health -= self.attack_power
        print(f"{self.name} атакует {other.name} и наносит {self.attack_power} урона.")

    def super_attack(self, other):
        if not self.super_power_used:
            damage = random.randint(10, 20)
            damage_amount = other.health * (damage / 100)
            other.health -= damage_amount
            self.super_power_used = True
            print(f"{self.name} использует суперсилу и наносит {int(damage_amount)} урона ({damage}% от здоровья).")
        else:
            print(f"{self.name} уже использовал свою суперсилу!")

    def is_alive(self):
        return self.health > 0
class Game:
    def __init__(self):
        player_name = input("Введите имя вашего героя: ")
        self.player = Hero(player_name)
        self.computer = Hero("Компьютерный герой")
    def start(self):
        current_turn = "player"
        while self.player.is_alive() and self.computer.is_alive():
            if current_turn == "player":
                use_super = input("Хотите использовать суперсилу? (да/нет): ")
                if use_super.lower() == "да":
                    self.player.super_attack(self.computer)
                else:
                    self.player.attack(self.computer)
                current_turn = "computer"
            else:
                if not self.computer.super_power_used and random.choice([True, False]):
                    self.computer.super_attack(self.player)
                else:
                    self.computer.attack(self.player)
                current_turn = "player"
            print(f"Здоровье {self.player.name}: {self.player.health}")
            print(f"Здоровье {self.computer.name}: {self.computer.health}")
            print()

            if random.choice([True, False]):
                print("Пропуск хода!")
                current_turn = "player" if current_turn == "computer" else "computer"

        winner = self.player if self.player.is_alive() else self.computer
        print(f"Игра окончена! Победитель: {winner.name}")

# Запуск игры
if __name__ == "__main__":
    game = Game()
    game.start()
