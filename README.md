# Part 9

## Accompanying resources
* Slide deck: https://zipcoder.github.io/reveal-slides.data-engineering/zcw_content/python/fundamentals-part9.html
* [json module](https://docs.python.org/3/library/json.html)  

## Exercise 1

### Prep Work

* Look inside the data directory. There are a few json files provided for you. Familiarize yourself with these files. Feel free to add more.

### Part A
* Create a program called *json_helper.py*
* Define a function called *read_json*. Given a string representing a file path to a json file, this function should open said file and convert its contens into a json object.
* The json object should be returned.

### Part B
* Define a function called *read_all_json_files*. Given a string representing a path to a directory, this function should read all of the json files and return a list containing all of the json objects.
* Make sure to incorporate the work from part A.

### Part C
* Define a function called *write_pickle*. This function should take a file path and some data. Given these parameters, the function should write the contents of the json files to a file called **super_smash_characters.pickle**.

### Part D
* Define a function called *load_pickle*. Given a file path, this function opens a pickled file and returns the data. 
* Use this function to print the pickled data from Part C to the screen.


**Make sure to write tests for your code**

## Exercise 2

* Create another dataset. Here are some suggestions:
  * Marvel
  * DragonBallZ

Is this program re-usable? 
