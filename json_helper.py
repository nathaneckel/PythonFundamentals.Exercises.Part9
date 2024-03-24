import json
import os
import pickle


def read_json(file):
    with open(file, 'r') as file:
        json_data = json.load(file)
        return json_data


file = 'data/He-Man_Figures/He-Man.json'
json_object = read_json(file)
print(json_object)


# #Part B
# Given a string representing a path to a directory, read all of the json files + return a list containing all json objects.

def read_json(file_path):
    with open(file_path, 'r') as json_file:
        json_data = json.load(json_file)

    return json_data



def read_json_files_and_print_contents(dir_path):
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            if file.endswith('.json'):
                file_path = os.path.join(root, file)
                json_data = read_json(file_path)
                print(json_data)

# Example usage:
dir_path = 'data'
read_json_files_and_print_contents(dir_path)


# Part C
# Define a function called write_pickle. This function should
# take a file path and some data. Given these parameters,
# the function should write the contents of the json files to a file
# called super_smash_characters.pickle.

def write_pickle(json_file_path, pickle_file_path):
    try:
    #LOADING JSON data from JSON file
        with open(json_file_path, 'r') as json_file:
            json_data = json.load(json_file)

        #SERIALIZE and SAVE JSON data with pickle
        with open(pickle_file_path, 'wb') as pickle_file:
            pickle.dump(json_data, pickle_file)
        print("Pickle file created successfully.")
    except FileNotFoundError:
        print("JSON file was not found.")
    except Exception as e:
        print(f"An error occurred: (e)")


json_file_path = '/Users/nathan/Dev/Labs/PythonFundamentals.Exercises.Part9/data/super_smash_bros/mario.json'
pickle_file_path = 'data/super_smash_characters.pickle'


write_pickle(json_file_path, pickle_file_path)


# Define a function called load_pickle. Given a file path, this function opens a pickled file and returns the data.# Use this function to print the pickled data from Part C to the screen.# Make sure to write tests for your code

def load_pickle(pickle_file_path):
    try:
        with open(pickle_file_path, 'rb') as pickle_file:
            pickle_data = pickle.load(pickle_file)
        return pickle_data
    except FileNotFoundError:
        print("Pickle file not found")
    except Exception as e:
        print(f"An error occurred: {e}")


pickle_file_path = 'data/super_smash_characters.pickle'
pickle_data = load_pickle(pickle_file_path)
print(load_pickle(pickle_file_path))

