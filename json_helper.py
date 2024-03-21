import json
def read_json():
    with open('/Users/nathan/Dev/Labs/PythonFundamentals.Exercises.Part9/data/He-Man Action Figures/He-Man.json') as file:
        return file.load(file)

read_json()


#OPEN > CONVERT > RETURN json object
# #1. #given a string representing filePath:
##this function must OPEN the json @filePath and
# #convert contents to a json Object. #Json object should be returned

# #Part B
# Define a function called read_all_json_files.
# Given a string representing a path to a directory,
# - read all of the json files + return a list containing all json objects.
# - incorporate the work from part A.

def read_all_json_files():
    json_data = open('~/Dev/Labs/PythonFundamentals.Exercises.Part9')

    for item in json_data:
        for data_item in item['data']:
                print
                data_item['name'], data_item['value']

read_all_json_files()


# Part C
# Define a function called write_pickle. This function should
# take a file path and some data. Given these parameters,
# the function should write the contents of the json files to a file
# called super_smash_characters.pickle.

# #Part D
# Define a function called load_pickle. Given a file path, this function opens a pickled file and returns the data.
# Use this function to print the pickled data from Part C to the screen.
# Make sure to write tests for your code