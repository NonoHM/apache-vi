from apachelogs import LogParser
import re
# from itertools import combinations

log_path = '../data/access.laii-9.log'

# Découper chaque partie du log selon la norme (voir docs)
parser = LogParser("%h %l %u %t \"%r\" %>s %b \"%{Referer}i\" \"%{User-Agent}i\"")

# Filtrer/Compter le nombre de la liste par type (navigateur, date...)
def count_filter(filter_obj='Firefox', *list_to_iterate):
    filtered = len(list(filter(lambda x: x == filter_obj, *list_to_iterate)))
    #print(f"Il y a {filtered} {browser_type} utilisés")
    return filtered

# Filtrer le nombre de connexions par jour
def connexion_number():
    k = 1
    date_list = []
    date_filtered = {}
    with open(log_path) as fp:  
        for entry in parser.parse_lines(fp):
            date_list.append(str(entry.request_time.date()))
    # for i,j in combinations(date_list,2):
    #     if i == j:
    #         k+=1
    #         date_filtered.update({i: k })
    for i in sorted(set(date_list)):
        filtered = len(list(filter(lambda x: x == i, date_list)))
        date_filtered.update({i: filtered })
    return date_filtered


def main():
    print(f" Le nombre de connexions par jour est: \n {connexion_number()}")


if __name__ == "__main__":
    main()