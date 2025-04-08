import random
#переложить в интерфейс
class Player:
    def __init__(self):
        self.HP = 10
        self.defence = 0
        self.atk = 0

    def change_HP(self):
        self.HP -= 1

    def change_def(self, _pos):
        self.defence = _pos

    def change_atk(self, _pos):
        self.atk = _pos


class Goblin:
    def __init__(self):
        self.HP = 10
        self.defence = 0
        self.atk = 0

    def change_HP(self):
        self.HP -= 1

    def change_def(self):
        self.defence = random.randint(1,3)

    def change_atk(self):
        self.atk = random.randint(1,3)

player = Player()
goblin = Goblin()
while True:
    player_atk_pos = input("позиция атаки(1,2,3)")
    player_atk_pos = int(player_atk_pos)
    player_def_pos = input("позиция защиты(1,2,3)")
    player_def_pos = int(player_def_pos)
    player.change_atk(player_atk_pos)
    player.change_def(player_def_pos)
    goblin.change_def()
    goblin.change_atk()
    if goblin.defence != player.atk:
        goblin.change_HP()
    if player.defence != goblin.atk:
        player.change_HP()
    print(f"Player HP {player.HP}, Def:{player.defence},Atk:{player.atk}")
    print(f"Goblin HP {goblin.HP}, Def:{goblin.defence},Atk:{goblin.atk}")
    if player.HP<1 or goblin.HP<1:
        break
