def get_most_played(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        lines_list = f.read().splitlines()
    for index, line in enumerate(lines_list):
        lines_list[index] = line.split('\t')
    def getKey(item):
        return float(item[1])
    game_by_sold = sorted(lines_list, key=getKey, reverse=True)
    title = game_by_sold[0][0]
    return title

def sum_sold(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        lines_list = f.read().splitlines()
    for index, line in enumerate(lines_list):
        lines_list[index] = line.split('\t')
    lst2 = [item[1] for item in lines_list] # get all sales from list and creates list of it
    sold_number = [float(i) for i in lst2] #convert list of strings to float
    return sum(sold_number)

def get_selling_avg(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        lines_list = f.read().splitlines()
    for index, line in enumerate(lines_list):
        lines_list[index] = line.split('\t')
    lst2 = [item[1] for item in lines_list] # get all sales from list and creates list of it
    sold_number = [float(i) for i in lst2] #convert list of strings to float
    avg = sum(sold_number) / len(sold_number) #doing average
    return avg

def count_longest_title(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        lines_list = f.read().splitlines()
    for index, line in enumerate(lines_list):
        lines_list[index] = line.split('\t')
    lst2 = [item[0] for item in lines_list] #create list of titles
    longest = max(lst2, key=len) # search for longest title
    return len(longest)

def get_date_avg(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        lines_list = f.read().splitlines()
    for index, line in enumerate(lines_list):
        lines_list[index] = line.split('\t')
    lst2 = [item[2] for item in lines_list] # get all dates from list and creates list of it
    list_of_dates = [float(i) for i in lst2] #convert list of strings to list of float
    avg = sum(list_of_dates) / len(list_of_dates) #doing average
    return round(avg)

def get_game(file_name, title):
    with open(file_name, 'r', encoding='utf-8') as f:
        lines_list = f.read().splitlines()
    for index, line in enumerate(lines_list):
        lines_list[index] = line.split('\t')
    this_f_game = []
    for item in lines_list:
        if item[0] == title: #checks if title is in the list of lists
            this_f_game = item #appends
    if this_f_game == []: #error
        raise ValueError("I can't find this game")
    this_f_game[1] = float(this_f_game[1])
    this_f_game[2] = int(this_f_game[2])
    return this_f_game
