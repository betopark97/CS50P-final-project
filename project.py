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
            # Country
            while True:
                # ask for country and make it case-insensitive 
                country = input('Which country are you traveling to? ').strip().title()
                # check if country is in dataset
                check = check_place(df,country, column='country')
                # if country is in dataset stop while loop
                if country == check:
                    break
            # Cities
            # instruction for cities input
            print(green_font+'Input "done" when done adding cities.'+reset_font)
            while True:
                # ask for city and make it case-insensitive
                cities = input('Which city are you traveling to? ').strip().title()
                # check if cities are in dataset
                check = check_place(df, cities)
                # if cities are in dataset stop whle loop

            
            # Country and City table

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

def check_place(df, place, column):
    # check if the country is in dataframe
    if place in df[column].values:
        return place
    else:
        # if the user input doesn't match the dataframe exactly
        # loop all the input words and try to find what the user would want
        place_words = place.split()
        # if user input one or more words
        if len(place_words) >= 1:
            place_suggestion = []
            # loop through words and see if they are in dataset
            for word in place_words:
                for suggestion in df.loc[df[column].str.contains(word),column].value_counts().index.to_list():
                    place_suggestion.append(suggestion)
            # if after loop there wasn't a word that matched dataset
            if len(place_suggestion) == 0:
                print('Please, try again.')
            # if after loop there was a word that matched dataset, suggest
            else:
                print('Perhaps you mean:')
                for suggestion in place_suggestion:
                    print('...'+suggestion)
                print('Please, try again.')
        # if user didn't input anything
        else:
            print('You didn\'t make an input, try again.')

def make_table():
    pass


def calculate_distances():
    pass


def make_map():
    pass


if __name__ == '__main__':
    main()