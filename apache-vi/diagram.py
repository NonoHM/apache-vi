import matplotlib.pyplot as plt
import os
from shutil import move
import sys
sys.path.append('/home/etudiant/Desktop/apache-vi/apache-vi')
import av_parser as pa
date_dict = pa.connection_number()
dict_month = pa.connection_month(date_dict, True)
nav_dict = pa.browser_number()
dict_week = pa.connection_week(date_dict)


#To save all the graph
def create_graph(path, graph):
    if not os.path.exists(path):
        os.makedirs(path)
    plt.savefig(graph)
    move(graph, f"{path}/{graph}")          

#print in a graph the month connextion : 
def month_graph(dict_month):
    fig, axes = plt.subplots()
    x=[]
    y=[]
    for key in dict_month.keys():
        x.append(key)
        
    for value in dict_month.values():
        y.append(value)
 
    width = 1.0
    plt.title("Histogramme des connexions par mois")
    plt.bar(x, y, width, align = 'center', color='b' )
    create_graph('output/img','month_graph.png')



#print in a graph the month connextion :
def nav_graph(nav_dict):
    fig, axes = plt.subplots()
    x=[]
    y=[]
    for key in nav_dict.keys():
        x.append(key)
        
    for value in nav_dict.values():
        y.append(value)

    plt.title("navigateur")
    plt.pie(y,labels=x, autopct='%1.1f%%',shadow=True,startangle=90)
    plt.axis('equal')
    create_graph('output/img','navigateur_filter.png')


#print in a graph the week connextion
def week_graph(dict_week):
    fig, axes = plt.subplots()
    x=[]
    y=[]
    for key in dict_week.keys():
        x.append(key)
        
    for value in dict_week.values():
        y.append(value)

    width = 1.0
    plt.title("connection_week")
    plt.bar(y, x, width, align = 'center', color='b' )
    create_graph('output/img','connection_week.png')


def main():
    nav_graph(nav_dict)
    week_graph(dict_week)
    month_graph(dict_month)
    
if __name__ == "__main__":
    main()




