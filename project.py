# import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import folium
from tabulate import tabulate


# different color fonts and reset
red_font = '\033[91m'
green_font = '\033[92m'
blue_font = '\033[94m'
reset_font = '\033[0m'

# make dataframe
df = pd.read_csv('worldcities.csv')
df = df.loc[:,['country','city_ascii','lat','lng']]
df = df.rename(columns={'city_ascii':'city'})

# some cleaning for name of countries that are hard to type
df = df.replace('Côte d\'Ivoire', 'Ivory Coast')
df = df.replace('Korea, South', 'South Korea')
df = df.replace('Korea, North', 'North Korea')
df['country'] = df['country'].agg(lambda x: x.str.replace('-', ' '))

# some cleaning for name of cities that are hard to type
df['city'] = df['city'].agg(lambda x: x.str.replace('-', ' '))
df['city'] = df['city'].agg(lambda x: x.str.replace('\'', ''))


# make the functions here
def main():
    instruction = """
What would you like to do? (Type number + Enter)
 1. make itinerary
 2. calculate distances or ideal route
 3. save it in a file
 4. exit the program\n
Input: """ 
    while True: 
        user = input(green_font + instruction + reset_font)
        if user =='1':
            # ask country
            
            # ask all cities to visit
            
            # make a data list of cities with lat and lng
            
            # make a table with the cities and ask if wants to proceed or remake
            

            warning = """
If the table missed a country: maybe you had a typo or the dataset doesn't contain info about that place 😭,
if you want to remake the table input 1 again,
if you want to proceed input 2 for an ideal route calculation!"""
            print(red_font + warning + reset_font)

        elif user == '2':
            # make an ideal route
            pass
           
        elif user == '3':
            # save in a file
            pass

        elif user == '4':
            # exit the program
            return False


def check_input():
    pass


def make_table():
    pass


def calculate_distances():
    pass


def make_map():
    pass


if __name__ == '__main__':
    main()