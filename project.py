# import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import folium
from tabulate import tabulate
import itertools
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
df = df.replace('Naha', 'Okinawa')
df['country'] = df['country'].agg(lambda x: x.str.replace('-', ' '))

# some cleaning for name of cities that are hard to type
df['city'] = df['city'].agg(lambda x: x.str.replace('-', ' '))
df['city'] = df['city'].agg(lambda x: x.str.replace('\'', ''))


# main function to run the program with set of instructions
def main():
    instruction = """
What would you like to do? (Type number + Enter)
 1. make itinerary
 2. calculate distances or ideal route
 3. save it in a file
 4. exit the program\n
Input: """ 
    # while loop to keep the program running unless quitting
    while True: 

        # Option 1: Make itinerary
        user = input(green_font + instruction + reset_font)
        if user =='1':

            # Country
            final_country = None
            while True:
                # ask for country and make it case-insensitive 
                country = input('Which country are you traveling to? ').strip().title()
                # check if country is in dataset
                check = check_place(df,country, column='country')
                # if country is in dataset stop while loop
                if country == check:
                    final_country = country
                    break

            # Cities
            # instruction for cities input
            print(green_font+'Input "done" when done adding cities.'+reset_font)
            final_cities = []
            while True:
                # ask for city and make it case-insensitive
                city = input('Which city are you traveling to? ').strip().title()
                # check if cities are in dataset
                check = check_place(df, city, column='city')
                # condition to be done inputing
                if city == 'Done':
                    break
                # if cities are in dataset stop whle loop
                elif city == check:
                    final_cities.append(city)
                
            # Country and City table
            # mask dataframe to match the user inputs
            df_table = df.loc[(df['country']==final_country) & (df['city'].isin(final_cities))]
            # make the table with country, city, latitude and longitudes
            print(make_table(df_table))
            # ask if wants to proceed or remake
            

            warning = """
If the table missed a country or city: maybe you had a typo or the dataset doesn't contain info about that place 😭,
if you want to remake the table input 1 again,
if you want to proceed input 2 for an ideal route calculation!"""
            print(red_font + warning + reset_font)

        # Option 2: Make route
        elif user == '2':

            # make an ideal route
            make_route(df_table)
            
            pass
           
        elif user == '3':
            # save in a file
            pass

        elif user == '4':
            # exit the program
            return False
        

def check_place(df, place, column):
    # check if the place is in dataframe
    if place in df[column].values:
        return place
    # this is to skip the input 'done' to finish inputting cities
    elif place == 'Done':
        return
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


def make_table(df):
    # capitalize the name of columns to show in tabulate
    new_df = df.rename(columns=lambda x: x.capitalize())
    # return the tabulate table
    return tabulate(new_df, headers='keys', tablefmt='grid', showindex=False)


def calculate_distance(lat1, lng1, lat2, lng2):
    # approximate radius of earth in km
    R = 6371.0

    # convert latitudes into radians
    lat1 = np.radians(lat1)
    lng1 = np.radians(lng1)
    lat2 = np.radians(lat2)
    lng2 = np.radians(lng2)

    # distances for lat and lng
    dlng = lng2 - lng1
    dlat = lat2 - lat1

    # haversine formula
    a = np.sin(dlat / 2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlng / 2)**2
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))

    # result distance in km
    distance = R * c
    return distance


def make_route(df_table):
    # Use idea of Dijkstra's Algorithm

    # calculate the longest distances
    # Get the two farthest cities using itertools
    city_combinations = list(itertools.combinations(df_table['city'],2))
    city_distances = []
    for index, combination in enumerate(city_combinations):
        city1, city2 = combination
        lat1, lng1 = df_table.loc[df_table['city']==city1,['lat','lng']].values[0]
        lat2, lng2 = df_table.loc[df_table['city']==city2,['lat','lng']].values[0]
        print(f'Combination {index+1}')
        distance = calculate_distance(lat1,lng1,lat2,lng2)
        print(f'Distance from {city1} to {city2} is...')
        print(f'Approximately: {distance:.2f} kilometers\n')
        city_distances.append({'City1':city1, 'City2':city2, 'Distance':distance})
    city_distances_df = pd.DataFrame(city_distances)
    farthest_cities = city_distances_df.loc[city_distances_df['Distance'].idxmax()]

    # main variables used
    visited_places = [] 
    non_visited_places = df_table['city'].to_list()
    len_total_places = len(non_visited_places)
    starting_city = farthest_cities[0]
    current_city = starting_city

    visited_places.append(starting_city)
    non_visited_places.remove(starting_city)
    for trial in range(len(non_visited_places)):
        dist_dict = {}
        print(f'Stop {trial+1}')
        print(f'We are currently in: {current_city}')
        for city in non_visited_places:
            lat1, lng1 = df_table.loc[df_table['city']==current_city, ['lat','lng']].values[0]
            lat2, lng2 = df_table.loc[df_table['city']==city, ['lat','lng']].values[0]
            distance = calculate_distance(lat1, lng1, lat2, lng2)
            print(f'Distance from {current_city} to {city} is {distance:.2f}km.')
            dist_dict[city] = distance
        print(f'We have currently visited: {", ".join(visited_places)}')
        print(f'We have yet to visit: {", ".join(non_visited_places)}')
        current_city = min(dist_dict, key=lambda k: dist_dict[k])
        if trial == len_total_places-1:
            print(f'Last stop is {current_city} with a total distance of {dist_dict[current_city]:.2f}km.')
        else:    
            print(f'Next stop is {current_city} with a total distance of {dist_dict[current_city]:.2f}km.')
        visited_places.append(current_city)
        non_visited_places.remove(current_city)
        print('')


def make_map():
    pass


if __name__ == '__main__':
    main()