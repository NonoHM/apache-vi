from datetime import datetime
from collections import Counter


date = {'2010-05-16': 3340, '2010-05-17': 4303, '2010-05-18': 4416, '2010-05-19': 4875, '2010-05-20': 4668, '2010-05-21': 3586, '2010-05-22': 2749, '2010-05-23': 184}

def connexion_week(date_dict):
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

def main():
    print(connexion_week(date))

if __name__ == "__main__":
    main()