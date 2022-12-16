import matplotlib.pyplot as plt
import sys
sys.path.append('/home/etudiant/Desktop/apache-vi/apache-vi')
import ap_parser as pa
date_dict = pa.connexion_number()

dict_month = pa.connexion_month(date_dict, True)
dict_week = pa.connexion_week(date_dict)
#print in a graph the month connextion

x=[]
y=[]
for key in dict_month.keys():
    x.append(key)
print(x)
    
for value in dict_month.values():
    y.append(value)
print(y)

# for test
def main():

    plt.bar(x,y)
    plt.show()

if __name__ == "__main__":
    main()

#test :  print(pa.connexion_month(date_dict, True))

r=[]
k=[]
for key in dict_week.keys():
    r.append(key)
print(r)
    
for value in dict_week.values():
    k.append(value)
print(k)

# for test
def main():

    plt.bar(r,k)
    plt.show(2)

if __name__ == "__main__":
    main()