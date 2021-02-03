##############################################
# Programmer: Carter Mooring
# Class: CPCS 322-02, Spring 2021
# Programming Assignment #1
# 2/2/21
# 
# 
# Description: This program opens and interprets a .csv file and stores its contents in a table.
#               The tables are then used to perform various task such as variable cleaning and specific value returns.
##############################################

import os
import copy
import random


def read_file(filename):
    """Makes a new table that is a copy of the the .csv file by comma-separating values (does not modify the original table), 
    and removes any extra white space. This also removes the header from the new table and stores it separately.

    Args:
        filename (str): The filename of the .csv file being worked with

    Returns:
        table (list of list): Data in 2D table format
        header (list of str): Column names corresponding to the table (in the same order)
    """
    table = []
    infile = open(filename, "r")    # open the file name for reading="r"

    # Proccess the file
    lines = infile.readlines()
    for line in lines:
        line = line.strip()
        values = line.split(",")
        table.append(values)
    
    header = table[0]               # store first row of table
    del table[0]                    # delete the first row of the table

    infile.close()
    return (table, header)


# one required function that is tested with the provided unit test in test.py
# do not modify this function header or the unit test
def remove_missing_values(table, header, col_name):
    """Makes a new table that is a copy of the table parameter (does not modify the original table), 
    but with rows removed from the table that have missing values in the column with label col_name

    Args:
        table (list of list): Data in 2D table format
        header (list of str): Column names corresponding to the table (in the same order)
        col_name (str): Represents the name of the column to check for missing values 

    Returns:
        list of list: The new table with removed rows
    """
    # Iterate through the header categories
    length = len(header)

    for i in range(len(header)):
        # Compare (lower case versions) of header categories to desired col_name
        if header[i].lower() == col_name.lower():
            break

    table_deep_copy = copy.deepcopy(table)             # create a copy of the table since deleting values

    for row in table:
        # check for blank spaces or wrongsized rows
        # TODO: missized rows may be a result of separating by commas
        if row[i] == "" or len(row) != length:
            table_deep_copy.remove(row)
   
    return table_deep_copy


def highest_imdb_rating(table, header):
    """Q1: Returns which TV show has the highest IMDb Rating

    Args: 
        table (list of list): Data in 2D table format
        header (list of str): Column names corresponding to the table (in the same order)

    Return:
        None: Just a print statement of the result is output
    """
    col_name = "imdb"
    highest_rating = 0.0
    title = ""
    new_table = remove_missing_values(table, header, col_name)        # Only need to call on imdb cateogry since title has no "blank" values

    for row in new_table:
        # If the row value for col_name is blank
        try:
            if float(row[4]) > highest_rating:
                highest_rating = float(row[4])
                title = row[1]
        except ValueError:
            print(row[4] + " could not be converted to a float. Meaning a value is here that is not supposed to be, so it will be ignored.")
    
    print("The TV show: '" + title + "' has the highest IMDb rating of: " + str(highest_rating))
    return None


def most_tv_shows(table):
    """Q2: Which streaming service hosts the most TV shows?

    Args: 
        table (list of list): Data in 2D table format

    Return:
        None: Just a print statement of the result is output
    """
    # Counters
    netflix, hulu, prime, disney = (0,)*4
    
    
    for row in table:
        if row[6] == "1":
            netflix += 1
        elif row[7] == "1":
            hulu += 1
        elif row[8] == "1":
            prime += 1
        elif row[9] == "1":
            disney += 1

    if netflix > hulu and prime and disney:
        print("Netflix streams the most TV shows with: " + str(netflix) + " shows total")
    elif hulu > prime and disney:
        print("Hulu streams the most TV shows with: " + str(hulu) + " shows total")
    elif prime > disney:
        print("Amazon Prime streams the most TV shows with: " + str(prime) + " shows total")
    else:
        print("Disney+ streams the most TV shows with: " + str(disney) + " shows total")

    return None


def show_recomendation(table):  
    """Q3: My own data science question. This asks for a users prefered streaming service
            and recomends a random show based off their input.

    Args: 
        table (list of list): Data in 2D table format

    Return:
        None: Just a print statement of the result is output
    """ 
    target = 0 
    temp = 0
    service = ""

    # Have the user input their streaming service of choice, goes until they submit a valid input
    while target == 0:
        streaming_service = input("Enter your Streaming Service of choice using the first letter of the service \n \
            (ex: 'n' for Netflix, 'h' for Hulu, 'a' for Amazon Prime, and 'd' for Disney+): ")
        streaming_service = streaming_service.lower()

        if streaming_service == "n":
            target = 6
            service = "Netflix"
        elif streaming_service == "h":
            target = 7
            service = "Hulu"
        elif streaming_service == "a":
            target = 8
            service = "Amazon Prime Video"
        elif streaming_service == "d":
            target = 9
            service = "Disney+"
        else:
            print()
            print("Please enter a valid letter to reprisent your Streaming Service.")
            print()

    print(service + " entered...")
    # Find a random show until it is offered on their streaming service of choice
    while temp != "1":
        rand_num = random.randint(0, len(table) - 1)
        info = table[rand_num]
        temp = info[target]

    print()
    print("I recomend you watch the show '" + info[1] + "', available to stream on " + service + " right now!")
    
    return None


def main():
    # Prepare the file and table values
    filename = os.path.join("input_data", "tv_shows.csv")
    print("///////////////////////////////////////////////////////////////////////////////////////////////////")
    print(filename)
    table, header = read_file(filename)
    print()

    # Other functions
    highest_imdb_rating(table, header)
    print()
    most_tv_shows(table)
    print()
    show_recomendation(table)
    print("///////////////////////////////////////////////////////////////////////////////////////////////////")
    

if __name__ == "__main__":
    main()