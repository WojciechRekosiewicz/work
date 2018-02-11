from reports import count_games, decide, get_latest, count_by_genre, get_line_number_by_title
import os

def main():
    export = 'export.txt'
    f = open(export, 'w', encoding='utf-8')
    f.close()
    while True:
        try:
            print("what do you wanna know?")
            print("1.press 1 for count games")
            print("2.Is there a game from a given year")
            print("3.Which was the latest game")
            print("4.How many games do we have by genre")
            print("5.What is the line number of the given game (by title)")
            print("0.To exit")
            choose = int(input())
            if choose == 1:
                file = input("enter the name of the file")
                print(count_games(file))
                amount = str(count_games(file))
                with open(export, 'a', encoding='utf-8') as f:
                    f.write("{}\n".format(str(amount)))
                continue
            if choose == 2:
                x = int(input("choose a year"))
                file = input("enter the name of the file")
                print(decide(file, x))
                amount = str(decide(file, x))
                with open(export, 'a', encoding='utf-8') as f:
                    f.write("{}\n".format(str(amount)))
                continue
            if choose == 3:
                file = input("enter the name of the file")
                print(get_latest(file))
                amount = str(get_latest(file))
                with open(export, 'a', encoding='utf-8') as f:
                    f.write("{}\n".format(str(amount)))
                continue
            if choose == 4:
                x = input("enter genre")
                file = input("enter the name of the file")
                print(count_by_genre(file, x))
                amount = str(count_by_genre(file, x))
                with open(export, 'a', encoding='utf-8') as f:
                    f.write("{}\n".format(str(amount)))
                continue
            if choose == 5:
                x = input("enter game name")
                file = input("enter the name of the file")
                print(get_line_number_by_title(file, x))
                amount = str(get_line_number_by_title(file, x))
                with open(export, 'a', encoding='utf-8') as f:
                    f.write("{}\n".format(str(amount)))
                continue
            elif choose == 0:
                exit("bb")
            else:
                print("wrong input try again")
                continue
        except ValueError:
            print("wrong input")
        except FileNotFoundError:
            print("Can't find this file")


if __name__ == "__main__":
    main()

