# Unsorted arrays can be searched for a target with O(n)
# Sorted arrays can be searched for a target with O(logn) using binary search

def bsearch(target, array):
    start_idx, end_idx = 0, len(array) - 1
    while start_idx <= end_idx:
        middle_idx = start_idx + ((end_idx - start_idx) // 2)
        if target > array[middle_idx]:
            start_idx = middle_idx + 1
        elif target == array[middle_idx]:
            return middle_idx
        else:
            end_idx = middle_idx - 1
    return -1


# -> Comparable objects can be sorted and searched by built-in functions
# -> Languages can typically know how to sort and search built-in types, i.e. integers, strings, classes for date, URL, SQL timestamps, etc.
# -> User definied custom types must explicitly implement comparision including basic transitivity (a=b, b=c, a=c) properties
    # If custom types comparision property gets implemented incorrectly, a simple lookup into a sorted array will fail even if it's actually present.

# Example:
# Input: an array of students, sorted by descending GPA, with ties broken on name.

# Below, binary search library is used to perform fast searches with a custom comparator which places GPA first, 
# followed by name so the bsearch module will give GPA more priority than name for comparison

import collections, bisect
Student = collections.namedtuple("student", ("gpa", "name"))

def comp_gpa(student):
    return (-student.gpa, student.name) # (-)ve because descending sort is asked

def search_student(students, target, comp_gpa):
    i = bisect.bisect_left([comp_gpa(s) for s in students], comp_gpa(target))
    return 0 <= i < len(students) and students[i] == target


# bisect module
# ref -> https://docs.python.org/3.0/library/bisect.html

# bisect.bisect_left(list, item[, lo[, hi]])
    # returns the index of the first entry that is greater or equal to the target. If all elements are less than target
    # len(list) is returned

# bisect.bisect_right(list, item[, lo[, hi]]) / bisect.bisect
    # returns the index of the first entry that is just greater than the target. If all elements are less or equal to 
    # target then len(list) is returned

# -> optional parameters lo and hi may be used to narrow a subset of the list. by default the entire list is used
# -> Use cases:
    # -> Locate the proper insertion point for item in list to maintain sorted order
        # -> bisect_left : the insertion point which comes before any existing entries. The return value is suitable 
        #    for use as the first parameter to list.insert()
        # -> bisect_right : an insertion point which comes after any existing entries of item in list
    # -> Finding elements
        # -> bisect_left : find the first element that is not less than the target
        # -> bisect_right : find the first element that is greater than the target
