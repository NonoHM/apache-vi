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
output = '../output'

#To save all the graph
def create_graph(output, graph):
      '''
    create the graph in the output folder
    
    :param str graph: Path of the graph file
    :returns: graph 
    :rtype: str
    '''
    output = output + '/img'
    if not os.path.exists(output):
        os.makedirs(output)
    plt.savefig(graph)
    move(graph, f"{output}/{graph}")          

#print in a graph the breakdown of connections by browser :
def nav_graph(nav_dict, output):
    '''
    browser_number(log_path=default_default_log_path) create a pie chart to display the number of browsers used
    
    :param str log_path: Path of the graph file
    :returns: it displays a pie chart with all the browsers and their number of connections 
    :rtype: dict
    '''
    fig, axes = plt.subplots()
    x=[]
    y=[]
    for key in nav_dict.keys():
        x.append(key)
        
    for value in nav_dict.values():
        y.append(value)

    plt.title("Breakdown of connections by browser")
    plt.pie(y,labels=x, autopct='%1.1f%%',shadow=True,startangle=90)
    plt.axis('equal')
    create_graph(output,'browser_graph.png')

#print in a graph the month connextion : 
def month_graph(dict_month, output):
    '''
    connection_week(date_dict, switch=True) uses the dict sent by the connection_number() function and returns the connections per month in a graph.

    :param dict date_dict: date_dict = pa.connection_number() , dict_month = pa.connection_month(date_dict, True)
    :returns: returns a histogram of all the connections of the month.
    :rtype: dict
    '''
    fig, axes = plt.subplots()
    x=[]
    y=[]
    for key in dict_month.keys():
        x.append(key)
        
    for value in dict_month.values():
        y.append(value)
 
    width = 1.0
    plt.title("Histogram of connections by month")
    plt.bar(x, y, width, align = 'center', color='b' )
    create_graph(output,'month_graph.png')

#print in a graph the week connextion
def week_graph(dict_week, output):
    '''
    connection_week(date_dict) uses the dict sent by the connection_number() function and returns the connections per week in a graph

    :param dict date_dict: date_dict = pa.connection_number() , dict_week = pa.connection_week(date_dict, True)
    :returns: returns a histogram of all the connections of the week.
    :rtype: dict
    '''
    fig, axes = plt.subplots()
    x=[]
    y=[]
    for key in dict_week.keys():
        x.append(key)
        
    for value in dict_week.values():
        y.append(value)

    width = 1.0
    plt.title("Histogram of connections by week")
    plt.bar(x,y, width, align = 'center', color='b' )
    create_graph(output,'week_graph.png')

#Create every graph at same time
def make_all(dict_week, dict_month, nav_dict, output):
    nav_graph(nav_dict, output)
    week_graph(dict_week, output)
    month_graph(dict_month, output)

def main():
    make_all(dict_week, dict_month, nav_dict, output)
    
    
if __name__ == "__main__":
    main()




