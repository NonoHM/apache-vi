from apachelogs import LogParser
import re

log_path = '../data/access.laii-8.log'

# Découper chaque partie du log selon la norme (voir docs)
parser = LogParser("%h %l %u %t \"%r\" %>s %b \"%{Referer}i\" \"%{User-Agent}i\"")

# Filtrer/Compter le nombre de navigateur par type
def count_browser(browser_type='Firefox', *browser_list):
    filtered = len(list(filter(lambda x: x == browser_type, *browser_list)))
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
    print(browser_list)
    for i in search_list:
        a = count_browser(i, browser_list)
        browser_dict.update({i: a})
    return browser_dict

# Pour tester
def main():
    browser_number()


if __name__ == "__main__":
    main()