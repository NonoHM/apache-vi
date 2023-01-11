from apachelogs import LogParser
import re
from datetime import datetime
from collections import Counter

"""
.. module:: av_parser.py
   :platform: Unix, windows
   :synopsis: Parser of the input file to return elements to create diagrams

.. moduleauthor:: Houmeau Noah <noah.houmeau@etu.univ-poitiers.fr>
"""

#default_log_path = '/home/etudiant/Desktop/apache-vi/data/pydefis-ssl.access_ano.log'
default_log_path = '../data/access.laii-8.log'
# Découper chaque partie du log selon la norme (voir docs)
parser = LogParser("%h %l %u %t \"%r\" %>s %b \"%{Referer}i\" \"%{User-Agent}i\"")

# Compter le nombre de lignes du log
def log_length(log_path=default_log_path):
    '''
    Returns the number of lines existing in the text
    
    :param str log_path: Path of the log file
    :returns: Number of existing lines
    :rtype: str
    '''
    with open(log_path) as fp:
        lines = len(fp.readlines())
        return lines

# Filtrer/Compter le nombre de la liste par type (navigateur, date...)
def count_filter(filter_obj='Firefox', *list_to_iterate):
    filtered = len(list(filter(lambda x: x == filter_obj, *list_to_iterate)))
    #print(f"Il y a {filtered} {browser_type} utilisés")
    return filtered

# Trouver le nombre de navigateurs et les ranger dans un dictionnaire
def browser_number(log_path=default_log_path):
    '''
    browser_number(log_path=default_default_log_path) searches in the log file for the presence of browsers and count how much there's in it
    
    :param str log_path: Path of the log file
    :returns: Searches which and how many browsers were connected with the log files 
    :rtype: dict
    '''
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
def connection_number(log_path=default_log_path):
    '''
    connection_number(log_path=default_log_path) searches how many times and when a connection has been done

    :param str log_path: Path of the log file
    :returns: Searches when and how many times a connection has been done in the log file
    :rtype: dict
    '''
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

# Filtre les dates par semaine, 
# Retourne le numéro de la semaine format ISO - nb total de connexions sur cette semaine
def connection_week(date_dict):
    '''
    connection_week(date_dict) uses the dict sent by the connection_number() function and returns the connections per week
    the week returned is the week ISO number provided by isocalendar()

    :param dict date_dict: {day: nb_connections}
    :returns: Returns connections per week 
    :rtype: dict
    '''
    L1 = []
    L2 = []
    L3 = []
    for i in date_dict:
        date = datetime.strptime(i,"%Y-%m-%d")
        weekd = date.isocalendar().week
        L1.append(weekd)
    for pairs in date_dict.values():
        L2.append(pairs)
    for j in range(len(L1)):
        L3.append({L1[j]: L2[j]})
    counter = Counter()
    for d in L3: 
        counter.update(d)  
    result = dict(counter)
    return result

# Filtre les dates par mois, 
# 2 Arguments, 1er: dictionnaire des jours, 2e: True or False.
# True retourne le numéro du mois format ISO - nb total de connexions sur ce mois
# False retourne le nom du mois  - nb connexions du mois 
def connection_month(date_dict, switch=True):
    '''
    connection_week(date_dict, switch=True) uses the dict sent by the connection_number() function and returns the connections per month.
    If the switch is False, it returns the ISO number of it instead of the name of the month

    :param dict date_dict: {day: nb_connections}
    :param bool switch: Returns month by name or by ISO Format
    :returns: Returns connections per month
    :rtype: dict
    '''
    assert switch == True or switch == False
    L1 = []
    L2 = []
    L3 = []
    for i in date_dict:
        date = datetime.strptime(i,"%Y-%m-%d")
        if switch == True:
            L1.append(date.ctime().split(' ')[1])
        else:
            monthd = date.month
            L1.append(monthd)
    for pairs in date_dict.values():
        L2.append(pairs)
    for j in range(len(L1)):
        L3.append({L1[j]: L2[j]})
    counter = Counter()
    for d in L3: 
        counter.update(d)  
    result = dict(counter)
    return result
        

def main():
    '''
    Main test function
    '''
    print(f" Le nombre de connexions par type de navigateur est: \n {browser_number()}")
    print(f" Le nombre de connexions par jour est: \n {connection_number()}")
    print(f" Le nombre de connexions par semaine est: \n {connection_week(connection_number())}")
    print(f" Le nombre de connexions par mois est: \n {connection_month(connection_number())}")

if __name__ == "__main__":
    main()