import matplotlib.pyplot as plt
import sys
sys.path.append('../apache-vi')
import av_parser as pa
date_dict = pa.connection_number()
dict_month = pa.connection_month(date_dict, True)

#print in a graph the month connextion
fig, axes = plt.subplots()
x=[]
y=[]
for key in browser_dict.keys():
    x.append(key)
print(x)
    
for value in browser_dict.values():
    y.append(value)
print(y)

# # for test
def main():
    width = 1.0
    plt.title("test")
    axes.bar(x, y, width, align = 'center', color='b' )
    plt.savefig('test7.png')
    plt.show()
if __name__ == "__main__":
    main()
