from apachelogs import LogParser
import re
from datetime import datetime
from collections import Counter

#default_log_path = '/home/etudiant/Desktop/apache-vi/data/pydefis-ssl.access_ano.log'
default_log_path = '../data/access.laii-8.log'
parser = LogParser("%h %l %u %t \"%r\" %>s %b \"%{Referer}i\" \"%{User-Agent}i\"")

def log_length(log_path=default_log_path):
    return sum(1 for line in open(log_path))

def count_filter(filter_obj='Firefox', *list_to_iterate):
    return sum(1 for x in list_to_iterate if x == filter_obj)

def browser_number(log_path=default_log_path):
    browser_list = []
    search_list = ['Firefox', 'Chrome', 'Safari', 'Brave', 'Opera', 'Edge', 'Internet Explorer']
    with open(log_path) as fp:  
        for entry in parser.parse_lines(fp):
            browser = str(entry.headers_in["User-Agent"])
            browser_search = re.compile('|'.join(search_list),re.IGNORECASE).search(browser)
            if browser_search:
                browser_list.append(browser_search.group(0))
    return Counter(browser_list)

def connection_number(log_path=default_log_path):
    date_list = []
    with open(log_path) as fp:  
        for entry in parser.parse_lines(fp):
            date_list.append(str(entry.request_time.date()))
    return Counter(date_list)

def connection_week(date_dict):
    return {datetime.strptime(date, '%Y-%m-%d').strftime('%U'): count for date, count in date_dict.items()}

def connection_month(date_dict, switch=True):
    format = '%B' if switch else '%m'
    return {datetime.strptime(date, '%Y-%m-%d').strftime(format): count for date, count in date_dict.items()}

def main():
    print(f" Le nombre de connexions par type de navigateur est: \n {browser_number()}")
    print(f" Le nombre de connexions par jour est: \n {connection_number()}")
    print(f" Le nombre de connexions par semaine est: \n {connection_week(connection_number())}")
    print(f" Le nombre de connexions par mois est: \n {connection_month(connection_number())}")

if __name__ == "__main__":
    main()