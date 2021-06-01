import random
from actors import Player, Enemy, Ogre, Imp


class Game:
    def __init__(self, player, enemies):
        self.player = player
        self.enemies = enemies

    def main(self):
        self.print_intro()
        self.play()

    def print_intro(self):
        print("""
            Monster Slash!!!


            Ready Player One?
            [Press Enter to Continue]
        """)
        input()

    def print_linebreak(self):
        print()
        print('*'*30)
        print()

    def play(self):
        while True:
            next_enemy = random.choice(self.enemies)
            cmd = input('You see a {}. [r]un, [a]ttack, [p]ass?'.format(next_enemy.kind))
            if cmd == 'r':
                print('{} runs away!'.format(self.player.name))
                print('{} heals thyself!'.format(self.player.name))
                self.player.heal()
            elif cmd == 'a':
                self.player.attacks(next_enemy)
                if not next_enemy.is_alive():
                    self.enemies.remove(next_enemy)
                    next_enemy = None
                if next_enemy:
                    next_enemy.attacks(self.player)
            elif cmd == 'p':
                print('You are still thinking about your next move...')
                if random.randint(1, 11) < 5:
                    next_enemy.attacks(self.player)
            else:
                print('Please choose a valid option')

            if not self.player.is_alive():
                print('Oh no! You lose!')
                break
            self.print_linebreak()
            self.player.stats()
            for e in self.enemies:
                e.stats()
            self.print_linebreak()

            if not self.enemies:
                print('You have won! Congratulations!')
                break


if __name__ == '__main__':
    enemies = [
        Ogre('Bob', 1, 3),
        Imp('Alice', 1)
    ]
    player = Player('Hercules', 1)
    Game(player, enemies).main()






#
