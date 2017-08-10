import requests
import urllib.request
from collections import defaultdict
import time
import csv
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import webbrowser
from lxml import html
'''
Hello there! This is my goal to go through all the nba players and see which ones aren't garbage.
So first I have to go through the player data to create a bank of all the players and so I can access the webpages of Basketball Reference. 
Af

dasfdasf
'''

def get_all_players(player_dict):
    for player in player_dict.keys():
        try:
            r = requests.get('https://www.basketball-reference.com/players/', headers = {'User-agent': 'your bot 0.1'})
            data = r.text
        except:
            print('Something died')
            break
        print(data)
        
    # content = urllib.urlopen('https://www.basketball-reference.com/players/').read()
    # print(soup.prettify)
    # 
        
def get_all_players2():
    pass





# write in the raw data from the csv file to have players
def add_player_data_to_columns():
    columns = defaultdict(list) # each value in each column is appended to a list
    with open('players.csv') as f:
        reader = csv.DictReader(f) # read rows into a dictionary format
        for row in reader: # read a row as {column1: value1, column2: value2,...}
            for (k,v) in row.items(): # go over each column name and value 
                columns[k].append(v) # append the value into the appropriate list
                                        # based on column name k
    return columns
    
    
# pass in the raw csv data formatted into columns with player_data, and return a list with 
# only the active players in the format (Name//     
def filter_active_players(player_data): 
    index_list = []
    output = []
    for i in range(len(player_data['To'])):
        if player_data['To'][i] == '2017':
            index_list.append(i)
    for index in index_list:
        output.append(player_data['Player'][int(index)])
    return output

# filters the code of the player so that we may use them to scrape their data from bball ref, i.e
# their shortened name
def filter_active_players_to_dict(active_players):
    output = {}
    for player in active_players:
        counter = 0
        for i in range(len(player)):
            if counter == 1:
                index = i
                output[player[:i-1]]=player[i:]
                break
            if player[i] == "\\":
                counter += 1
    return output
            
# opens the bball reference page for which 

    
        
player_dict = {}      
player_data = add_player_data_to_columns()
active_players = filter_active_players(player_data)
player_dict = filter_active_players_to_dict(active_players)


class Player:
    def __init__(self, name):
        self.name = name
        self.salaries = []
        try:
            self.code = player_dict[name]
        except KeyError:
            print('This is not an active NBA player')
            
    def open_player_page(self):
        url = 'https://www.basketball-reference.com/players'
        webbrowser.open(url+'/'+self.code[0]+'/'+self.code+'.html')
        
    def scrape_player_data(self):
        
        url = 'https://www.basketball-reference.com/players'
        r = requests.get(url+'/'+self.code[0]+'/'+self.code+'.html'+'#all_salaries::none', headers = {'User-agent': 'your bot 0.1'})
        page = html.fromstring(r.content)
        data = r.text
        # print(data)
        poop = page.xpath('//*[@id="all_salaries"]/tbody/tr[1]/td[3]/@csk')
        print(poop)
        print(self.salaries)
        # //*[@id="all_salaries"]/tbody/tr[1]/td[3] 
            # //*[@id="all_salaries"]/tbody/tr[4]/td[3]
            
TR = Player('Thomas Robinson')
TR.scrape_player_data()

       ##   //*[@id="all_salaries"]/tbody/tr[1]/td[3]
        


        
            