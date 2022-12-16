import matplotlib.pyplot as plt
import sys
sys.path.append('../apache-vi/')
import av_parser as pa
date_dict = pa.connection_number()

dict_month = pa.connection_month(date_dict, True)
dict_week = pa.connection_week(date_dict)
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

#test :  print(pa.connection_month(date_dict, True))

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
    plt.show()

if __name__ == "__main__":
    main()