import matplotlib.pyplot as plt
import sys
sys.path.append('/home/etudiant/Desktop/apache-vi/apache-vi')
import av_parser as pa
date_dict = pa.connection_number()
dict_month = pa.connection_month(date_dict, True)
dict_week = pa.connection_week(date_dict)
#print in a graph the month connextion

fig, axes = plt.subplots()
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
    width = 1.0
    plt.title("month_connexion")
    axes.bar(x, y, width, align = 'center', color='b' )
    plt.savefig('test7.png')
    plt.show()
if __name__ == "__main__":
    main()

#test :  print(pa.connection_month(date_dict, True))
"""
x=[]
y=[]
for key in dict_week.keys():
    x.append(key)
print(x)
    
for value in dict_week.values():
    y.append(value)
print(y)

# for test
def main():

    plt.bar(x,y)
    plt.show()

if __name__ == "__main__":
    main()
"""
