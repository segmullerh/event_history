"""
Module with a functions to read and write JSON files (using dictionaries)

This function will be used in the main project.  You should hold on to it.

Author: Hermann Segmuller
Date: 1/30/2021
"""
import json


def read_json(filename):
    """
    Returns the contents read from the JSON file filename.
    
    This function reads the contents of the file filename, and will use the json module
    to covert these contents into a Python data value.  This value will either be a
    a dictionary or a list. 
    
    Parameter filename: The file to read
    Precondition: filename is a string, referring to a file that exists, and that file 
    is a valid JSON file
    """
    # Implement this function
    file = open(filename)
    text = file.read()
    data = json.loads(text)
    file.close()

#    print ('data: ', data)
    return data


def write_json(data,filename):
    """
    Writes the given data out as a JSON file filename.
    
    To be a proper JSON file, data must be a a JSON valid type.  That is, it must be
    one of the following:
        (1) a number
        (2) a boolean
        (3) a string
        (4) the value None
        (5) a list
        (6) a dictionary
    The contents of lists or dictionaries must be JSON valid type.
    
    When written, the JSON data should be nicely indented four spaces for readability.
    
    Parameter data: The Python value to encode as a JSON file
    Precondition: data is a JSON valid type
    
    Parameter filename: The file to read
    Precondition: filename is a string representing a path to a file with extension
    .json or .JSON.  The file may or may not exist.
    """
    # Implement this function
    
    file = open(filename, 'w')
    
    #print ('data: ', data)
    
    text = json.dumps(data, indent=4)
    #print ('text: ', text)
    
#    for i in data :
#        print ('i: ',i)
        
    file.write(text)
    file.close()
    