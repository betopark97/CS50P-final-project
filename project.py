# import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import folium
from tabulate import tabulate


# different color fonts and reset
red_font = "\033[91m"
green_font = "\033[92m"
blue_font = "\033[94m"
reset_font = "\033[0m"


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
        if user == "1":
            # ask country
            
            # ask all cities to visit
            
            # make a data list of cities with lat and lng
            
            # make a table with the cities and ask if wants to proceed or remake
            

            warning = """
If the table missed a country: maybe you had a typo or the dataset doesn't contain info about that place 😭,
if you want to remake the table input 1 again,
if you want to proceed input 2 for an ideal route calculation!"""
            print(red_font + warning + reset_font)

        elif user == "2":
            # make an ideal route
            pass
           
        elif user == "3":
            # save in a file
            pass

        elif user == "4":
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