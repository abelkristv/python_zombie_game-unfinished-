import sys
import os

from random import randint
from time import sleep
class Unit:
    """Class untuk unit secara general"""

    def __init__(self, xLok, yLok):
        self.health = 0
        self.xLok = xLok
        self.yLok = yLok
        self.special_bar = 5
        self.max_special = 5

    def normal_attack(self, zombie):
        zombie.health -= 5
        zombie.symbol = " "
        zombie.xLok = 1000
        zombie.yLok = 1000
        print("[o_o] Hwaaa....")
        print("Zombie dead...")
        sleep(1)

    def print_coordinate(self):
        print(f"Player coordinate is [x,y]: {self.xLok}, {self.yLok}")

    def add_special_bar(self, num):
        self.special_bar += num

class SupportUnit(Unit):

    def __init__(self, xLok, yLok):
        super().__init__(xLok, yLok)
        self.health = 5
        self.symbol = 'S'
        self.name = 'Support Unit [~v~]'
        self.max_health = 5

    def add_health(self, num):
        self.health += num

    def special_1(self):
        if self.special_bar < 3:
            print("Not enough special bar!!")
            sleep(1)
            return
        print("Who would you like to heal: ")
        print("[1] Assault Trooper   [2] Heavy Mech   [3] Support Unit")
        choice = input("Enter choice : ")
        if choice == '1':
            assault_unit.add_health(3)
            health_min = assault_unit.health - assault_unit.max_health
            assault_unit.health = assault_unit.health - health_min
        elif choice == '2':
            heavy_mech.add_health(3)
            health_min = heavy_mech.health - heavy_mech.max_health
            heavy_mech.health = heavy_mech.health - health_min
        elif choice == '3':
            support_unit.add_health(3)
            health_min = support_unit.health - support_unit.max_health
            support_unit.health = support_unit.health - health_min
        
        self.special_bar -= 3 
       
    def special_2(self):
        if self.special_bar < 3:
            print("Not enough special bar")
            sleep(1)
            return
        print("Who would you like to encourage: ")
        print("[1] Assault Trooper   [2] Heavy Mech")
        choice = input("Enter choice : ")

        if choice == '1':
            assault_unit.add_special_bar(3)
            special_min = assault_unit.special_bar - assault_unit.max_special
            assault_unit.special_bar = assault_unit.special_bar - special_min
        elif choice == '2':
            heavy_mech.add_special_bar(3)
            special_min = heavy_mech.special_bar - heavy_mech.max_special
            heavy_mech.special_bar = heavy_mech.special_bar - special_min
        self.special_bar -= 3


class AssaultTrooper(Unit):

    def __init__(self, xLok, yLok):
        super().__init__(xLok, yLok)
        self.health = 3
        self.symbol = 'A'
        self.name = 'Assault Trooper [~_~]'
        self.max_health = 3

    def add_health(self, num):
        self.health += num

    def special_1(self):
        print("Assault Trooper used faceoff...")
        player = self
        for coorY in range(self.yLok, self.yLok+2):
            for coorX in range(self.xLok, self.xLok+2):
                if coorX == zombie1.xLok and coorY == zombie1.yLok:
                    player.normal_attack(zombie1)
                if coorX == zombie2.xLok and coorY == zombie2.yLok:
                    player.normal_attack(zombie2)
                if coorX == zombie3.xLok and coorY == zombie3.yLok:
                    player.normal_attack(zombie3)
                if coorX == zombie4.xLok and coorY == zombie4.yLok:
                    player.normal_attack(zombie4)
                if coorX == zombie5.xLok and coorY == zombie5.yLok:
                    player.normal_attack(zombie5)
                if coorX == zombie6.xLok and coorY == zombie6.yLok:
                    player.normal_attack(zombie6)

        for coorY in range(self.yLok, self.yLok-2, -1):
            for coorX in range(self.xLok, self.xLok-2, -1):
                if coorX == zombie1.xLok and coorY == zombie1.yLok:
                    player.normal_attack(zombie1)
                if coorX == zombie2.xLok and coorY == zombie2.yLok:
                    player.normal_attack(zombie2)
                if coorX == zombie3.xLok and coorY == zombie3.yLok:
                    player.normal_attack(zombie3)
                if coorX == zombie4.xLok and coorY == zombie4.yLok:
                    player.normal_attack(zombie4)
                if coorX == zombie5.xLok and coorY == zombie5.yLok:
                    player.normal_attack(zombie5)
                if coorX == zombie6.xLok and coorY == zombie6.yLok:
                    player.normal_attack(zombie6)

    def special_2(self):
        for i in range(1, 4):
            player = self
            print("Activating Adv targeting!!")
            print(f"Your current coordinate [x,y]: {player.xLok-1}, {player.yLok-1}")
            coorX = input("Input the zombie X coordinate: ")
            coorX = int(coorX)
            coorY = input("Input the zombie Y coordinate: ")
            coorY = int(coorY)
            if coorX == zombie1.xLok-1 and coorY == zombie1.yLok-1:
                player.normal_attack(zombie1)
            elif coorX == zombie2.xLok-1 and coorY == zombie2.yLok-1:
                player.normal_attack(zombie2)
            elif coorX == zombie3.xLok-1 and coorY == zombie3.yLok-1:
                player.normal_attack(zombie3)
            elif coorX == zombie4.xLok-1 and coorY == zombie4.yLok-1:
                player.normal_attack(zombie4)
            elif coorX == zombie5.xLok-1 and coorY == zombie5.yLok-1:
                player.normal_attack(zombie5)
            elif coorX == zombie6.xLok-1 and coorY == zombie6.yLok-1:
                player.normal_attack(zombie6)
            else:
                print("There is nothing in that coordinate...")
                sleep(1)


class HeavyMech(Unit):

    def __init__(self, xLok, yLok):
        super().__init__(xLok, yLok)
        self.health = 5
        self.symbol = 'H'
        self.name = 'Heavy Mech [~w~]'
        self.max_health = 5

    def add_health(self, num):
        self.health += num

    def special_1(self):
        print("HeavyMech used grenade!!")
        xLok = input("Enter the x coordinate: ")
        xLok = int(xLok)
        yLok = input("Enter the y coordinate: ")
        yLok = int(yLok)
        player = self
        for coorY in range(yLok, yLok+2):
            for coorX in range(xLok, xLok+2):
                if coorX == zombie1.xLok-1 and coorY == zombie1.yLok-1:
                    player.normal_attack(zombie1)
                if coorX == zombie2.xLok-1 and coorY == zombie2.yLok-1:
                    player.normal_attack(zombie2)
                if coorX == zombie3.xLok-1 and coorY == zombie3.yLok-1:
                    player.normal_attack(zombie3)
                if coorX == zombie4.xLok-1 and coorY == zombie4.yLok-1:
                    player.normal_attack(zombie4)
                if coorX == zombie5.xLok-1 and coorY == zombie5.yLok-1:
                    player.normal_attack(zombie5)
                if coorX == zombie6.xLok-1 and coorY == zombie6.yLok-1:
                    player.normal_attack(zombie6)

        for coorY in range(yLok-2, yLok+1):
            for coorX in range(xLok-2, xLok+1):
                if coorX == zombie1.xLok-1 and coorY == zombie1.yLok-1:
                    player.normal_attack(zombie1)
                if coorX == zombie2.xLok-1 and coorY == zombie2.yLok-1:
                    player.normal_attack(zombie2)
                if coorX == zombie3.xLok-1 and coorY == zombie3.yLok-1:
                    player.normal_attack(zombie3)
                if coorX == zombie4.xLok-1 and coorY == zombie4.yLok-1:
                    player.normal_attack(zombie4)
                if coorX == zombie5.xLok-1 and coorY == zombie5.yLok-1:
                    player.normal_attack(zombie5)
                if coorX == zombie6.xLok-1 and coorY == zombie6.yLok-1:
                    player.normal_attack(zombie6)

    def special_2(self):
        print("Machine Gun!!")
        print("Which direction would you like to shoot")
        print("['w'] Up  ['a'] Left  ['s'] down  ['d'] Right")
        player = self
        direction = input(":")
        if direction == 'w' or direction == 's':
            temp = self.yLok
            direct = 'vertical'
            if direction == w:
                moving = 'plus'
            else:
                moving = 'min'
        elif direction == 'a' or direction == 'd':
            temp = self.xLok
            direct = 'horizontal'
            if direction == 'd':
                moving = 'plus'
            else:
                moving = 'min'

        temporaryLok = temp
        for i in range(0, 12):
            if direction == 'vertical':
                coorY = temporaryLok-1
                coorX = self.xLok-1
                if moving == 'plus':
                    temporaryLok += 1
                else:
                    temporaryLok -= 1
                if coorX == zombie1.xLok-1 and coorY == zombie1.yLok-1:
                    player.normal_attack(zombie1)
                if coorX == zombie2.xLok-1 and coorY == zombie2.yLok-1:
                    player.normal_attack(zombie2)
                if coorX == zombie3.xLok-1 and coorY == zombie3.yLok-1:
                    player.normal_attack(zombie3)
                if coorX == zombie4.xLok-1 and coorY == zombie4.yLok-1:
                    player.normal_attack(zombie4)
                if coorX == zombie5.xLok-1 and coorY == zombie5.yLok-1:
                    player.normal_attack(zombie5)
                if coorX == zombie6.xLok-1 and coorY == zombie6.yLok-1:
                    player.normal_attack(zombie6)

            else:
                coorY = self.yLok-1
                coorX = temporaryLok-1
                if moving == 'plus':
                    temporaryLok += 1
                else:
                    temporaryLok -= 1
                if coorX == zombie1.xLok-1 and coorY == zombie1.yLok-1:
                    player.normal_attack(zombie1)
                if coorX == zombie2.xLok-1 and coorY == zombie2.yLok-1:
                    player.normal_attack(zombie2)
                if coorX == zombie3.xLok-1 and coorY == zombie3.yLok-1:
                    player.normal_attack(zombie3)
                if coorX == zombie4.xLok-1 and coorY == zombie4.yLok-1:
                    player.normal_attack(zombie4)
                if coorX == zombie5.xLok-1 and coorY == zombie5.yLok-1:
                    player.normal_attack(zombie5)
                if coorX == zombie6.xLok-1 and coorY == zombie6.yLok-1:
                    player.normal_attack(zombie6)


class Zombie:
    """Class untuk zombie"""
    def __init__(self, yLok, xLok):
        self.xLok = xLok
        self.yLok = yLok
        self.health = 5
        self.symbol = '\033[1;32;40mZ\033[0m'
        self.name = 'Zombiee [o_o]'

def clear_screen():
    if(os.name == 'posix'):
        os.system('clear')
    else:
        os.system('cls')

def gotoxy(x,y):
    print("%c[%d;%df" % (0x1B, y, x), end="")

def support_unit_stat(support_unit):
    gotoxy(26, 5)
    print(f"      {support_unit.name}")
    gotoxy(26, 6)
    print(f"\033[1;32;40mHealth : {support_unit.health}/{support_unit.max_health}     \033[1;33;40mSpecial : {support_unit.special_bar}/{support_unit.max_special}\033[0m")
    gotoxy(26, 7)
    print("[#] COMMAND: ")
    gotoxy(26, 8)
    print(" |  [1] >> [Move]")
    gotoxy(26, 9)
    print(" |  [2] >> [Attack]")
    gotoxy(26, 10)
    print(" |  [3] >> [Heal Teammate]")
    gotoxy(26, 11)
    print(" |  [4] >> [Encouragement]")
    gotoxy(26, 12)
    print(" |  [5] >> [CallForExtraction]")
    gotoxy(26, 13)
    print("[#]")

def assault_trooper_stat(assault_unit):
    gotoxy(26, 5)
    print(f"      {assault_unit.name}")
    gotoxy(26, 6)
    print(f"\033[1;32;40mHealth : {assault_unit.health}/{assault_unit.max_health}     \033[1;33;40mSpecial : {assault_unit.special_bar}/{assault_unit.max_special}\033[0m")
    gotoxy(26, 7)
    print("[#] COMMAND: ")
    gotoxy(26, 8)
    print(" |  [1] >> [Move]")
    gotoxy(26, 9)
    print(" |  [2] >> [Attack]")
    gotoxy(26, 10)
    print(" |  [3] >> [Faceoff]")
    gotoxy(26, 11)
    print(" |  [4] >> [Adv Targeting]")
    gotoxy(26, 12)
    print(" |  [5] >> [CallForExtraction]")
    gotoxy(26, 13)
    print("[#]")

def heavy_mech_stat(heavy_mech):
    gotoxy(26, 5)
    print(f"      {heavy_mech.name}")
    gotoxy(26, 6)
    print(f"\033[1;32;40mHealth : {heavy_mech.health}/{heavy_mech.max_health}   \033[0;33;40mSpecial : {heavy_mech.special_bar}/{heavy_mech.max_special}\033[0m")
    gotoxy(26, 7)
    print("[#] COMMAND: ")
    gotoxy(26, 8)
    print(" |  [1] >> [Move]")
    gotoxy(26, 9)
    print(" |  [2] >> [Attack]")
    gotoxy(26, 10)
    print(" |  [3] >> [Grenade]")
    gotoxy(26, 11)
    print(" |  [4] >> [Machine Gun]")
    gotoxy(26, 12)
    print(" |  [5] >> [CallForExtraction]")
    gotoxy(26, 13)
    print("[#]")


def main_menu():
    clear_screen()
    print("===========================")
    print("\033[1;32;40m")
    print("           ZCOM            ")
    print("\033[0m")
    print("===========================")
    print("\033[1;35;40m[1]\033[0m Play")
    print("\033[1;35;40m[2]\033[0m Highscore")
    print("\033[1;35;40m[0]\033[0m Exit")
    pilihan = input("Enter choice: ")
    pilihan = int(pilihan)
    return pilihan

def draw_board(playerX, playerY, sizeX, sizeY, turn):
    print("=========================================================")
    print("\033[1;32;40m", end = "")
    print("                       Game mode            ")
    print("\033[0m", end = "")
    print("=========================================================")
    for y in range(1, sizeY):
        for x in range(1, sizeX):
            if (y == 1) or (y == sizeY-1):
                print("# ", end = "")
            if ((y > 1 and x == 1) or (y > 1 and x == sizeX-1)) and y != sizeY-1:
                print("# ", end = "")
            elif (y > 1 and (x > 1 or x < sizeX-1)) and (y < sizeY-1 and (x < sizeX-1 or x > 1)):
                if x == support_unit.xLok and y == support_unit.yLok:
                    print(f"{support_unit.symbol} ", end = "")
                elif x == assault_unit.xLok and y == assault_unit.yLok:
                    print(f"{assault_unit.symbol} ", end = "")
                elif x == heavy_mech.xLok and y == heavy_mech.yLok:
                    print(f"{heavy_mech.symbol} ", end = "")
                elif x == zombie1.xLok and y == zombie1.yLok:
                    print(f"{zombie1.symbol} ", end = "")
                elif x == zombie2.xLok and y == zombie2.yLok:
                    print(f"{zombie2.symbol} ", end = "")
                elif x == zombie3.xLok and y == zombie3.yLok:
                    print(f"{zombie3.symbol} ", end = "")
                elif x == zombie4.xLok and y == zombie3.yLok:
                    print(f"{zombie4.symbol} ", end = "")
                elif x == zombie5.xLok and y == zombie5.yLok:
                    print(f"{zombie5.symbol} ", end = "")
                elif x == zombie6.xLok and y == zombie6.yLok:
                    print(f"{zombie6.symbol} ", end = "")

                else:
                    print("  ", end = "")
        print("")
        
    gotoxy(25,4)

    print("\u250f", end = "")
    for i in range(1,32):
        print("\u2501", end = "")
    print("\u2513")
    for i in range(1,10):
        gotoxy(25,4+i)
        print("\u2503                               \u2503")
    gotoxy(25,14)
    print("\u2517", end = "")
    for i in range(1,32):
        print("\u2501", end = "")
    print("\u251b")
    
    if turn == 1:
        support_unit_stat(support_unit)
    elif turn == 2:
        assault_trooper_stat(assault_unit)
    elif turn == 3:
        heavy_mech_stat(heavy_mech)
    
    gotoxy(1, 15)

def move_input(playerxLok, playeryLok, move, i, playerName):
            while True:
                if move == 0:
                    print("You've run out of move")
                    sleep(1)
                    break
                clear_screen()
                draw_board(6, 6, 12, 12, i)
                print(f"{playerName} mode: [Moving] [Move left: {move}]")
                print("Enter WASD to move! [Enter HOLD to get into command mode]")
                choice = input()
                if choice == 'w':
                    playeryLok -= 1
                    if playeryLok == 1:
                        playeryLok += 1
                        move += 1
                elif choice == 'a':
                    playerxLok -= 1
                    if playerxLok == 1:
                        playerxLok += 1
                        move += 1
                elif choice == 's':
                    playeryLok += 1
                    if playeryLok == 11:
                        playeryLok -= 1
                        move += 1
                elif choice == 'd':
                    playerxLok += 1
                    if playerxLok == 11:
                        playerxLok -= 1
                        move += 1
                elif choice.lower() == 'hold':
                    break
                else:
                    print("Key not recognized")
                    sleep(1)
                    move += 1
                move -= 1
                if i == 1:
                    support_unit.xLok = playerxLok
                    support_unit.yLok = playeryLok
                elif i == 2:
                    assault_unit.xLok = playerxLok
                    assault_unit.yLok = playeryLok
                elif i == 3:
                    heavy_mech.xLok = playerxLok
                    heavy_mech.yLok = playeryLok

                if move == 0:
                    print("You run out of move!!")
                    sleep(1)
                    break
            return [move, playerxLok, playeryLok]

def attack(xLok, yLok, player):
    while True:
        print("You can only attack 4 radius from you position!!")
        print(f"Your current coordinate [x,y]: {player.xLok-1}, {player.yLok-1}")
        coorX = input("Input the zombie X coordinate: ")
        coorX = int(coorX)
        coorY = input("Input the zombie Y coordinate: ")
        coorY = int(coorY)
        if coorX > xLok+4 or coorY > yLok+4 or coorX < xLok-4 or coorY < yLok-4:
            print("Invalid coordinate")
        elif coorX == zombie1.xLok-1 and coorY == zombie1.yLok-1:
            player.normal_attack(zombie1)
            break
        elif coorX == zombie2.xLok-1 and coorY == zombie2.yLok-1:
            player.normal_attack(zombie2)
            break
        elif coorX == zombie3.xLok-1 and coorY == zombie3.yLok-1:
            player.normal_attack(zombie3)
            break
        elif coorX == zombie4.xLok-1 and coorY == zombie4.yLok-1:
            player.normal_attack(zombie4)
            break
        elif coorX == zombie5.xLok-1 and coorY == zombie5.yLok-1:
            player.normal_attack(zombie5)
            break
        elif coorX == zombie6.xLok-1 and coorY == zombie6.yLok-1:
            player.normal_attack(zombie6)
            break
        else:
            print("There is nothing in that coordinate...")
            sleep(1)

def start_game():
    while True:
        move = 10
        for i in range(1, 10):
            if i == 1:
                playerxLok = support_unit.xLok
                playeryLok = support_unit.yLok
                playerName = support_unit.name
                player = support_unit
            elif i == 2:
                playerxLok = assault_unit.xLok
                playeryLok = assault_unit.yLok
                playerName = assault_unit.name
                player = assault_unit
            elif i == 3:
                playerxLok = heavy_mech.xLok
                playeryLok = heavy_mech.yLok
                playerName = heavy_mech.name
                player = heavy_mech
            elif i == 4:
                player = zombie1
            move = 10

            while True:
                if move > 0:
                    lists = move_input(playerxLok, playeryLok, move, i, playerName)
                    move = lists[0]
                    playerxLok = lists[1]
                    playeryLok = lists[2]
                clear_screen()
                draw_board(6, 6, 12, 12, i)
                print("[COMMAND MODE]")
                command = input(":")
                if command.lower() == 'move' or command == '1':
                    if move == 0:
                        print("You run out of move")
                        sleep(1)
                        continue
                    else:
                        continue
                elif command.lower() == 'attack' or command == '2':
                    attack(playerxLok, playeryLok, player)
                    break
                elif command == '3':
                    player.special_1()
                    break
                elif command == '4':
                    player.special_2()
                    break


                

class Player:
    """Class untuk player"""
    def __init__(self):
        self.turn = 1
        self.score = 0

    def increment_turn(self):
        self.turn += 1

    def increment_score(self):
        self.score+=10

    def game_over(self):
        self.score = 0



class Zcom:
    """Class untuk memanage asset dan game"""
    
    def __init__(self):
        self.score = 0
        self.turn = 1

    def run_game(self):
        """Looping utama untuk gamenya"""
        while True:
            choice = main_menu()
            if choice == 1:
                clear_screen()
                start_game()
                a = input()
            if choice == 0:
                break
        
if __name__ == '__main__':
    zcom = Zcom() 
    support_unit = SupportUnit(6, 6+1)
    assault_unit = AssaultTrooper(6-1, 6)
    heavy_mech = HeavyMech(6+1, 6)
    zombie1 = Zombie(6, 3)
    zombie2 = Zombie(4, 8)
    zombie3 = Zombie(3, 4)
    zombie4 = Zombie(8, 7)
    zombie5 = Zombie(4, 5)
    zombie6 = Zombie(8, 9)

    zcom.run_game()
            

