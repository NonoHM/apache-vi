from apachelogs import LogParser
import re


log_path = '../data/access.laii-9.log'

# Découper chaque partie du log selon la norme (voir docs)
parser = LogParser("%h %l %u %t \"%r\" %>s %b \"%{Referer}i\" \"%{User-Agent}i\"")

# Compter le nombre de lignes du log
def log_length():
    with open(log_path) as fp:
        lines = len(fp.readlines())
        return lines

# Filtrer/Compter le nombre de la liste par type (navigateur, date...)
def count_filter(filter_obj='Firefox', *list_to_iterate):
    filtered = len(list(filter(lambda x: x == filter_obj, *list_to_iterate)))
    #print(f"Il y a {filtered} {browser_type} utilisés")
    return filtered

# Trouver le nombre de navigateurs et les ranger dans un dictionnaire
def browser_number():
    browser_list = []
    browser_dict = {}
    search_list = ['Firefox', 'Chrome', 'Safari', 'Brave', 'Opera', 'Edge', 'Internet Explorer']
    with open(log_path) as fp:  
        for entry in parser.parse_lines(fp):
            browser = str(entry.headers_in["User-Agent"])
            browser_search = re.compile('|'.join(search_list),re.IGNORECASE).search(browser)
            if browser_search:
                browser_list.append(browser_search.group(0))
    for i in sorted(set(browser_list)):
        a = count_filter(i, browser_list)
        browser_dict.update({i: a})
    return browser_dict

# Filtrer le nombre de connexions par jour
def connexion_number():
    k = 1
    date_list = []
    date_filtered = {}
    with open(log_path) as fp:  
        for entry in parser.parse_lines(fp):
            date_list.append(str(entry.request_time.date()))
    for i in sorted(set(date_list)):
        filtered = count_filter(i,date_list)
        date_filtered.update({i: filtered })
    return date_filtered


def main():
    print(f" Le nombre de connexions par type de navigateur est: \n {browser_number()}")
    print(f" Le nombre de connexions par jour est: \n {connexion_number()}")


if __name__ == "__main__":
    main()