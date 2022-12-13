from datetime import datetime
from collections import Counter

date = {'2010-05-16': 3340, '2010-05-17': 4303, '2010-05-18': 4416, '2010-05-19': 4875, '2010-05-20': 4668, '2010-05-21': 3586, '2010-05-22': 2749, '2010-05-23': 184}

# Filtre les dates par mois, 
# 2 Arguments, 1er: dictionnaire des jours, 2e: True or False.
# False retourne le numéro du mois format ISO - nb total de connexions sur ce mois
# True retourne le nom du mois  - nb connexions du mois 
def connexion_month(date_dict, switch=False):
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
    print(connexion_month(date))

if __name__ == "__main__":
    main()