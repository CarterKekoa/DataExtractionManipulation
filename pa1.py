import os


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
    # TODO: fix this
    return None


def main():
    filename = os.path.join("input_data", "tv_shows.csv")
    print(filename)

if __name__ == "__main__":
    main()