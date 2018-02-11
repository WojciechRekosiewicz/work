from reports import get_most_played, sum_sold, get_selling_avg, count_longest_title, get_date_avg, get_game

def main():
    while True:
        try:
            print("What do you wanna know?")
            print("1.The title of the most played game (i.e. sold the most copies)")
            print("2.Copies sold total")
            print("3.The average selling")
            print("4.How many characters long is the longest title")
            print("5.Average of the release dates")
            print("6.Properties of selected game")
            print("0.To exit")
            choose = int(input())
            if choose == 1:
                file = input("enter the name of the file")
                print(get_most_played(file))
                continue
            if choose == 2:
                file = input("enter the name of the file")
                print(sum_sold(file))
                continue
            if choose == 3:
                file = input("enter the name of the file")
                print(get_selling_avg(file))
                continue
            if choose == 4:
                file = input("enter the name of the file")
                print(count_longest_title(file))
                continue
            if choose == 5:
                file = input("enter the name of the file")
                print(get_date_avg(file))
                continue
            if choose == 6:
                x = input("enter name of the game")
                file = input("enter the name of the file")
                print(get_game(file, x))
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
