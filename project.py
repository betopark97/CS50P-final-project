# import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import folium
from tabulate import tabulate
import re


# different color fonts and reset
red_font = '\033[91m'
green_font = '\033[92m'
blue_font = '\033[94m'
reset_font = '\033[0m'

# read dataframe
df = pd.read_csv('worldcities.csv')
df = df.loc[:,['country','city_ascii','lat','lng']]
df = df.rename(columns={'city_ascii':'city'})

# find names that are hard to type to clean them
def find_non_alphabet(df,column):
    non_alphabet_country = set()

    for value in df[column]:
        if re.search(r'[^a-zA-Z\s]', value):
            non_alphabet_country.add(value)

    for country in non_alphabet_country:
        print(country)

# some manual cleaning for name of countries that are hard to type
df = df.replace("Côte D’Ivoire", 'Ivory Coast')
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

def check_country(df, country):
    # make case insensitive to match dataframe
    country = country.title().strip()
    # check if the country is in dataframe
    if country in df['country'].values:
        return 
    else:
        # if the user input doesn't match the dataframe exactly
        # loop all the input words and try to find what the user would want
        country_words = country.split()
        if len(country_words) >= 1:
            country_suggestion = []
            for word in country_words:
                for suggestion in df.loc[df['country'].str.contains(word),'country'].value_counts().index.to_list():
                    country_suggestion.append(suggestion)
            print('Perhaps you mean:')
            for suggestion in country_suggestion:
                print('...'+suggestion)
            print('Please, try again.')
        else:
            print('You didn\'t input a country, try again.')

def check_cities():
    pass

def make_table():
    pass


def calculate_distances():
    pass


def make_map():
    pass


if __name__ == '__main__':
    main()