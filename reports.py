# Report functions
def count_games(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        lines_list = f.read().splitlines()
    x = len(lines_list)
    return x
      
def decide(file_name, year): 
    with open(file_name, 'r', encoding='utf-8') as f:
        lines_list = f.read().splitlines()
    for index, line in enumerate(lines_list):
        lines_list[index] = line.split('\t')   
    year = str(year)
    for game in lines_list:
        if year in game:
            return True    
    return False     

def get_latest(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        lines_list = f.read().splitlines()
    for index, line in enumerate(lines_list):
        lines_list[index] = line.split('\t')   
    def getKey(item):
        return item[2]
    game_by_year = sorted(lines_list, key=getKey, reverse=True)
    title = game_by_year[0][0]
    return title

def count_by_genre(file_name, genre):
    with open(file_name, 'r', encoding='utf-8') as f:
        lines_list = f.read().splitlines()
    for index, line in enumerate(lines_list):
        lines_list[index] = line.split('\t')      
    cout = [item for sublist in lines_list for item in sublist].count(genre)
    return cout

def get_line_number_by_title(file_name, title):
    with open(file_name, 'r', encoding='utf-8') as f:
        lines_list = f.read().splitlines()
    for index, line in enumerate(lines_list):
        lines_list[index] = line.split('\t') 
    for x, y in enumerate(lines_list):
        try:
            if title in y[0]:
                return x+1
        except ValueError:
            break
