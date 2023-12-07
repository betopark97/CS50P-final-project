# CS50P
This repository is for my CS50P's Final Project.

# Travel Route Estimator
    #### Video Demo:  <URL HERE>
    #### Description (Personal Thoughts and Documentation):

    #### Personal Thoughts

    This project was done in motivation of a recent incomodity I have experienced when traveling. I guess that there are people like me who like to be very detailed when it comes to planning and so, star, favorite, bookmark places to organize a certain pattern or cluster places to visit each day. However, this is very time consuming process when done manually. That is why I've tried to code a program that gives me a rough idea of the positioning and in which order I should visit those places considering only distance. This project only takes in the name of one country and its cities. I have learned that I lack so many skills when I first got a grasp of what kind of program I wanted to code. After finishing other weeks' practice sets I went ahead and watched lectures and practiced on skills that I didn't learn in `Harvard's CS50's Introduction to Python` such as numpy, pandas, folium, etc. When developing the program I also learned new things such as the Haversine Formula to calculate distances by coordinate locations (latitude and longitude) or the importance of learning Data Structure and Algorithm when trying to come up with an algorithm for the ideal route. I actually tried with just the logic that I could picture in my mind, but the problem is that it was full of bugs as sometimes it would work and sometimes it didn't. That's why I tried searching algorithms for this and I came across Dijkstra's Algorithm, which inspired me to make a similar algorithm. The only difference I'd say is that my algorithm has to cover all the nodes, but again I've never taken an algorithms course so I lack domain expertise to explain this well. I've realized that my code is very messy so after this program I'm planning to learn how to clean code and of course the classic Data Structure and Algorithm in hopes of someday making a better version of this program with less bugs and higher complexity. Some of the features I'd hope to implement in the making of a better version of this program is to learn more complex ways of using APIs to get more specific information such as routes, infrastructures, real-time traffic, etc. Also, try manipulate bigger datasets that include not only city locations, but also shops, restaurants, cafes, etc.
    Thank you for reading my personal thoughts.
    

    #### Documentation

    - What your application does,
    - Why you used the technologies you used,

    `Brief Description:`
    <br/>
    This project calculates an ideal route, as in efficiency of destination, for you trip. It does not consider roads to take or any other factors such as traffic or development of infrastructure traveling-wise.
    <br/>
    `How to use the program:`
    <br/>
    The program starts with a set of instructions and it reprompts if the user doesn't answer by inputting the provided options. There are four options to choose from: 
    <br/>
        1. make itinerary, which asks user to input a country name then goes on to ask the cities the user is visiting in that country. The input is case-insensitive and in case the user doesn't know how to correctly spell the country or the city's name the user can type the parts that they remember for suggestions. For example if the user knows that the country's name had 'South' in it, the user can try to just type 'South' and the program will suggest country names with 'South' in it's name. It also goes with just a few letters such as typing 'Jap' to get the suggestion 'Japan'.
        <br/> 
        2. make ideal route, which prints various calculations just in case the user wants to know what the program is doing in the background. It first provides the combination of distances between two cities (nCr = n!/r!(n-r)!). This is done to get hold of the two citiest that are located the farthest apart to choose as starting and ending locations. Then using a somewhat similar algorithm to the Dijkstra's Algorithm it calculates an ideal route and gives a verbose explanation of the algorithmic process. At the end giving a simplified version of that with just a list in the ideal order that the user should visit the cities. If the user wants to remake the choices, should input 1 and start again.
        <br/>
        3. make map, which makes pop-up markers on the specified cities by the user and connects them with a straight red line to show the route. This is an html map made by using the folium library and it is opened automatically on the user's default web browser. 
        <br/>
        4. exit program, which ends the program.
    <br/>
    `File descriptions:`
    <br/>
    There is a LICENSE.txt to show the licenses for the two datasets that were used in this project.
    <br/>
    There is a requirements.txt to show the pip installations to run this program along with datasets and their sources.
    <br/>
    There is a project.py, which runs the program.
    <br/>
    There is a test_project.py, which tests the most important functions of the program.
    <br/>
    There is two csv files: worldcities.csv and worldcountries.csv. The worldcities.csv is used in all the program to search the name of the country and cities the user is traveling to and their locations. The worldcountries.csv is only used for the 'make map' part to get the location of the country to start the zoom when opening the map.
    <br/>
    `Function descriptions:`
    <br/>
    main(): runs the program with a while loop to continue running unless the user types '4' to quit the program.
    <br/>
    check_place(): takes in three parameters, df, place, and column. It is to check if the country or city specified by the user exists in the dataset. It returns the country or city name as a string.
        - df: the dataset that is being used (csv file)
        - place: is the input of the user, which is a country or a city's name.
        - column: is to specify in which column the function should loop and the options are either 'country' or 'city'.
    <br/>
    make_table(): takes in the parameter df. After checking that the user's input exists in the dataset, this function converts that dataframe into a tabulate to display to the user.
    <br/>
    calculate_distance(): takes in four parameters, lat1, lng1, lat2, lng2, which are all float. The first two are the latitude and longitude of one of the two cities to calculate the distance for. The other two parameters are for the remaining city. It returns a float value for the distance.
    <br/>
    find_farthest_cities(): takes in the parameter df. It loops through all possible combination of distances using the above function to calculate the distances. It returns a list with the name of the two cities with the biggest distance among all combination of city distances.
    <br/>
    make_route(): takes in the parameter df. This uses a similar algorithm to the Dijkstra's Algorithm and considers all cities in the dataframe specified by the user as non_visited_places. Then it takes as starting city by randomly choosing one of the farthest cities by using the function above. It removes the starting city from the non_visited_places and adds the starting city to visited_places. Then the algorithm loops through all the combinations of city distances possible by find the city with the closest distance this time and chooses that city as the next stop. This process goes on until reaching the last city. It returns a list in the order of the ideal route.
    <br/>
    make_map(): takes in two parameters country, df. The country parameter is to start the zoom of the map at the user's choice of country to travel to. The df parameter is the dataset with the specified order from the above function. It loops through the dataset to create pop-up icons at the location of the cities with labels when moving the mouse cursor at the pop-up icons. Then it draws red lines connecting the cities for visualization of the route. It saves the map as an html file and simultaneously opens the html file on a web browser.

