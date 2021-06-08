# DataExtractionManipulation
Work with files, functions, and lists in Python. Extract data from a column in a table. Remove missing values. Execute unit tests

## Project Requirements
### Programming with the 🎬 TV Shows Dataset 🎬
Write a program (pa1.py) that opens a data file called tv_shows.csv. This file contains "the data scraped comprises a comprehensive list of tv shows available on various streaming platforms." It has the following columns (AKA attributes):
* Unique TV show ID
* Title
* Year: The year in which the tv show was produced
* Age: Target age group
* IMDb: IMDb rating
* Rotten Tomatoes: Rotten Tomatoes %
* Netflix: Whether the tv show is found on Netflix
* Hulu: Whether the tv show is found on Hulu
* Prime Video: Whether the tv show is found on Prime Video
* Disney+: Whether the tv show is found on Disney+  

#### Write code to do the following:
* Define/call a function that loads the TV shows data into a 2D Python list (AKA table). Remove (and store) the first row of the table, this is the header of the table
  * Note: you can use the csv module to help with file I/O if you'd like (but if you want to write it from scratch, see the bonus below!)
* Finish the function remove_missing_values(table, header, col_name)
  * Accepts the following parameters:
    * table: the 2D list
    * header: the header of the table
    * col_name: the name of the column to check for missing values. A missing value is represented as an empty string (""). If a row has a missing value in this column, drop the row.
  * Returns the table with the rows dropped
* Define/call a function to answer each of the following data science questions (so at least 3 functions):
  * Q1: Which TV show has the highest IMDb rating?
    * Note: be sure to use your remove_missing_values() function!!
  * Q2: Which streaming service hosts the most TV shows?
  * Q3: Define and answer a data science question of your own that you are interested in about the dataset. Be creative!

# README !!!

## To Setup (One Time Only)
`git clone (your github repo url here)`  
`cd` into your local repo you just cloned 

## To Run `main()`
Run `python pa#.py` where # is this PA's number

## To Run Unit Tests
Run `pytest --verbose test_pa#.py` where # is this PA's number

## What not to Modify
You may not modify:
* `test_pa#.py` where # is this PA's number
* Anything in the `test/` directory (if it exists)
* Any hidden files (e.g. files/folders that start with a `.`)
