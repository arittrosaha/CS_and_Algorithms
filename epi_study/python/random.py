# printing in python
# ref - https://stackoverflow.com/questions/26862773/how-to-print-formatted-string-in-python3

# py 2.6 way
# print("So, you're %r old, %r tall and %r heavy." % (age, height, weight))

# py 3 way (backported to 2.6+)
# print("So, you're {} old, {} tall and {} heavy.".format(age, height, weight))

# For pinning
# -> to skip the variable expanding 
# -> if you want something specific to appear twice for example
# print("So, you're {0} old, {1} tall and {2} heavy and {1} tall again".format(age, height, weight))


# Printing Syntax
# ref = https://www.w3schools.com/python/ref_func_print.asp

# print(object(s), separator=separator, end=end, file=file, flush=flush)

# Parameter Values
# Parameter	         Description
# object(s)	         Any object, and as many as you like. Will be converted to string before printed
# sep = 'separator'	 Optional. Specify how to separate the objects, if there is more than one. Default is ''
# end = 'end'	     Optional. Specify what to print at the end. Default is '\n' (line feed)
# file	             Optional. An object with a write method. Default is sys.stdout
# flush	             Optional. A Boolean, specifying if the output is flushed(True) or buffered(False). Default is False


# flush

# What does print()'s `flush` do?
# ref -> https://stackoverflow.com/questions/15608229/what-does-prints-flush-do

# what exactly the python's file.flush() is doing?
# ref -> https://stackoverflow.com/questions/7127075/what-exactly-the-pythons-file-flush-is-doing



# Python Operators:
# ref -> https://www.w3schools.com/python/python_operators.asp



# Python naming conventions
# Type	      Examples                                     Naming Convention	                                              
# Function	  function, my_function                     -> Use a lowercase word or words.                                  
#                                                          Separate words by underscores to improve readability.	
# Variable	  x, var, my_variable                       -> Use a lowercase single letter, word, or words.                  
#                                                          Separate words with underscores to improve readability.	
# Class	      Model, MyClass                            -> Start each word with a capital letter. Do not separate          
#                                                          words with underscores. This style is called camel case.
# Method	  class_method, method                      -> Use a lowercase word or words. Separate words with              
#                                                          underscores to improve readability.	
# Constant	  CONSTANT, MY_CONSTANT, MY_LONG_CONSTANT   -> Use an uppercase single letter, word, or words. Separate        
#                                                          words with underscores to improve readability.	
# Module	  module.py, my_module.py                   -> Use a short, lowercase word or words. Separate words with       
#                                                          underscores to improve readability.	
# Package	  package, mypackage                        -> Use a short, lowercase word or words. Do not separate words     
#                                                          with underscores.	

# ref -> https://realpython.com/python-pep8/



# Falsy values:
# -> None
# -> False
# -> zero of any numeric type
    # -> 0 
    # -> 0L
    # -> 0.0 
    # -> 0j 
    # -> Decimal(0)
    # -> Fraction(0,1)
    # -> b"" : empty bytes
# -> any empty sequence / mapping
    # -> ''       : empty string
    # -> []       : empty list
    # -> ()       : empty tuple
    # -> {}       : empty dict
    # -> set()    : empty set
    # -> range(0) : empty range
# -> objects for which
    # -> obj.__bool__() returns False
    # -> obj.__len__() returns 0

# Truthy values : everything else is a truthy values.
# ref -> https://stackoverflow.com/questions/39983695/what-is-truthy-and-falsy-in-python-how-is-it-different-from-true-and-false
#     -> https://docs.python.org/3/library/stdtypes.html#truth-value-testing



# Lack of python shift/unshift:
# ref -> https://stackoverflow.com/questions/34210969/why-pythons-list-not-have-a-shift-unshift-methods
# ref -> https://stackoverflow.com/questions/2150108/efficient-way-to-shift-a-list-in-python

# Append vs extend:
# ref -> https://stackoverflow.com/questions/252703/difference-between-append-vs-extend-list-methods-in-python?rq=1



# Built in Functions:
# ref -> https://docs.python.org/3/library/functions.html

# Built in Constants:
# ref -> https://docs.python.org/3/library/constants.html



# Control flow:
# ref -> https://docs.python.org/3/tutorial/controlflow.html

# General Loops:
# ref -> https://www.w3schools.com/python/python_for_loops.asp

# Loops with index:
# ref -> https://treyhunner.com/2016/04/how-to-loop-with-indexes-in-python/
# ref -> https://stackoverflow.com/questions/522563/accessing-the-index-in-for-loops

# Continue and break:
# ref -> https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops



# Merge two dicts:
# ref -> https://stackoverflow.com/questions/38987/how-to-merge-two-dictionaries-in-a-single-expression?rq=1



# Python lambda or anonymous function:
# ref -> https://www.w3schools.com/python/python_lambda.asp



# Enumerable methods in Python:
# ref -> https://stackoverflow.com/questions/13638898/how-to-use-filter-map-and-reduce-in-python-3



# Create an empty list in python with certain size:
# ref -> https://stackoverflow.com/questions/10712002/create-an-empty-list-in-python-with-certain-size

