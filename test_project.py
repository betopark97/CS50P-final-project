# import project functions to test
from project import check_place, calculate_distance, find_farthest_cities, make_route
# import pytest to test functions
import pytest
# import necessary libraries used in the project
import pandas as pd
import numpy as np
import random
import folium
from tabulate import tabulate
import itertools
import re
import subprocess

# read csv file to a dataframe to test functions
df = pd.read_csv('worldcities.csv')
df = df.loc[:,['country','city_ascii','lat','lng']]
df = df.rename(columns={'city_ascii':'city'})
df = df.replace('Naha', 'Okinawa')

def main():
    test_check_place()
    test_calculate_distance()
    test_find_farthest_cities()
    test_make_route()


# check_place(df: pd.DataFrame, place: str, column: str) -> str
def test_check_place():

    # First check_place() for country
    # check for correct input
    output1 = check_place(df, 'Japan', 'country')
    assert output1 == 'Japan'
    # check for typo input
    output2 = check_place(df, 'Kore', 'country')
    assert output2 == None
    # check for no input
    output3 = check_place(df, '', 'country')
    assert output3 == None

    # Second check_place() for city
    # check for correct input
    output4 = check_place(df, 'Washington', 'city')
    assert output4 == 'Washington'
    # check for typo input
    output5 = check_place(df, 'Chicag', 'city')
    assert output5 == None
    # check for no input
    output6 = check_place(df, '', 'city')
    assert output6 == None
    # check for 'done' input
    output7 = check_place(df, 'Done', 'city')
    assert output7 == None


# calculate_distance(lat1: float, lng1: float, lat2: float, lng2: float) -> float
def test_calculate_distance():

    # compare result with actual result from google search
    tokyo_to_sapporo = 832
    # distance from Tokyo to Sapporo
    lat1, lng1 = df.loc[df['city']=='Tokyo',['lat', 'lng']].values[0]
    lat2, lng2 = df.loc[df['city']=='Sapporo',['lat', 'lng']].values[0]
    output1 = calculate_distance(lat1, lng1, lat2, lng2)
    assert tokyo_to_sapporo - 10 <= output1 <= tokyo_to_sapporo + 10
    
    # compare result with actual result from google search
    seoul_to_busan = 320
    # distance from Seoul to Busan
    lat3, lng3 = df.loc[df['city']=='Seoul',['lat', 'lng']].values[0]
    lat4, lng4 = df.loc[df['city']=='Busan',['lat', 'lng']].values[0]
    output2 = calculate_distance(lat3, lng3, lat4, lng4)
    assert seoul_to_busan - 10 <= output2 <= seoul_to_busan + 10

# find_farthest_cities(df: pd.DataFrame) -> list
def test_find_farthest_cities():

    # farthest cities from Okinawa, Tokyo, Kyoto, Sapporo
    # answer should be Okinawa and Sapporo
    test_dataframe1 = df.loc[(df['country']=='Japan') & (df['city'].isin(['Okinawa', 'Tokyo', 'Kyoto', 'Sapporo']))]
    assert find_farthest_cities(test_dataframe1) == ['Okinawa', 'Sapporo'] or find_farthest_cities(test_dataframe1) == ['Sapporo', 'Okinawa']

    # farthest cities from San Francisco, Chicago, Michigan, Boston, New York
    # answer should be Boston and San Francisco
    test_dataframe2 = df.loc[(df['country']=='United States') & (df['city'].isin(['San Francisco', 'Chicago', 'Michigan', 'Boston', 'New York']))]
    assert find_farthest_cities(test_dataframe2) == ['San Francisco', 'Boston'] or find_farthest_cities(test_dataframe2) == ['Boston', 'San Francisco']


# make_route(df: pd.DataFrame) -> list
def test_make_route():

    # ideal route from Okinawa, Tokyo, Kyoto, Sapporo
    # answer should be in order of ['Okinawa', 'Kyoto', 'Tokyo', 'Sapporo']
    test_dataframe3 = df.loc[(df['country']=='Japan') & (df['city'].isin(['Okinawa', 'Tokyo', 'Kyoto', 'Sapporo']))]
    assert make_route(test_dataframe3) == ['Okinawa', 'Kyoto', 'Tokyo', 'Sapporo'] or make_route(test_dataframe3) == ['Sapporo', 'Tokyo', 'Kyoto', 'Okinawa']

    # ideal route from San Francisco, Chicago, Michigan, Boston, New York
    # answer should be in order of ['San Francisco', 'Chicago', 'Michigan', 'New York', 'Boston']
    test_dataframe4 = df.loc[(df['country']=='United States') & (df['city'].isin(['San Francisco', 'Chicago', 'Los Angeles', 'New York']))]
    assert make_route(test_dataframe4) == ['San Francisco', 'Los Angeles', 'Chicago', 'New York'] or make_route(test_dataframe4) == ['New York', 'Chicago', 'San Francisco', 'Los Angeles']


if __name__ == '__main__':
    main()



