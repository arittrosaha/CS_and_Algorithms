#                  In place?   Stable?   Worst case?    Avg case?   Best case?
# quicksort      -     y     -    y    -     n^2      -   nlogn   -   nlogn
# merge sort     -     n     -    y    -    nlogn     -   nlogn   -   nlogn
# heapsort       -     y     -    n    -    nlogn     -   nlogn   -   nlogn
# count sort     -     n     -    y    -      n       -     n     -     n

# Stable means preservation of the original order
# In place means no additional space complexitiy 

# Insertion sort is easier to code and faster for arrays with 10 or fewer elements
# Heapsort is better for almost sorted arrays where k is the furthest any element is from its final spot
# Count sort is better if there are a small number of distinct keys


# Know your libraries
class Student(object):
    def __init__(self, name, grade_point_average):
        self.name = name
        self.grade_point_average = grade_point_average
    
    def __lt__(self, other):
        return self.name < other.name

students = [
    Student("A", 4.0),
    Student("C", 3.0),
    Student("B", 2.0),
    Student("D", 3.2)
]

# Sort according to __lt__ defined in Student
students_sort_by_name = sorted(students)

# Sort students in-place by grade_point_average
students.sort(key=lambda student: student.grade_point_average)

# sort()
    # in place and stable sort for list objects
    # returns None but the calling list itself is updated

# sorted() 
    # takes an iterable
    # returns a new ascending sorted list   

# two optional arguments for both sort() and sorted()
    # key=None 
        # -> if the key is not None, it is assumed to be a function which takes list elements and maps them to objects which are comparable - this function defines the sort order
        # -> a = [1,2,4,3,5,0,11,21,100] ; a.sort(key=lambda x: str(x)) maps int to str and a is [0,1,100,11,2,21,3,4,5]
    # reverse=False
        # -> if it is set to True, the sort is done in descending order

