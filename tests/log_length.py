from apachelogs import LogParser
import re

# Découper chaque partie du log selon la norme (voir docs)
parser = LogParser("%h %l %u %t \"%r\" %>s %b \"%{Referer}i\" \"%{User-Agent}i\"")

# Compter le nombre de lignes du log
def log_length():
    with open('../data/access.laii-8.log') as fp:
        lines = len(fp.readlines())
        return lines

# Pour tester
def main():
    log_length()


if __name__ == "__main__":
    main()