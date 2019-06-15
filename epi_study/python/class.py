# Class syntax
# ref -> https://www.tutorialspoint.com/python3/python_classes_objects.htm
# class Employee:
#    'Common base class for all employees'
#    empCount = 0

#    def __init__(self, name, salary):
#       self.name = name
#       self.salary = salary
#       Employee.empCount += 1

#    def displayCount(self):
#      print("Total Employee %d" % Employee.empCount)

#    def displayEmployee(self):
#       print("Name : ", self.name,  ", Salary: ", self.salary)


# #This would create first object of Employee class"
# emp1 = Employee("Zara", 2000)
# #This would create second object of Employee class"
# emp2 = Employee("Manni", 5000)
# emp1.displayEmployee()
# emp2.displayEmployee()
# print("Total Employee %d" % Employee.empCount)
# When the above code is executed, it produces the following result −

# Name:  Zara, Salary:  2000
# Name:  Manni, Salary:  5000
# Total Employee 2

# The self Parameter is mutable
# ref -> https://www.w3schools.com/python/python_classes.asp

# Namespaces & Scoping
# ref -> https://docs.python.org/3/tutorial/classes.html#python-scopes-and-namespaces

# Namespaces:
    # What they are?
        # A namespace is a mapping from names to objects. Most namespaces are currently
        # implemented as Python dictionaries, but that’s normally not noticeable in any 
        # way(except for performance), and it may change in the future.

    # Examples:
        # The set of built-in names(containing functions such as abs(), and built-in 
        # exception names) the global names in a module and the local names in a function 
        # invocation.

    # An important note:
        # There is absolutely no relation between names in different namespaces for 
        # instance, two different modules may both define a function maximize without 
        # confusion — users of the modules must prefix it with the module name.

    # Creations moments:
        # builtins or native namespaces:
            # The namespace containing the built-in names is created when the 
            # Python interpreter starts up, and is never deleted.
        # Global namespace or the file or module:
            # The global namespace for a module is created when the module 
            # definition is read in; normally, module namespaces also last until 
            # the interpreter quits. The statements executed by the top-level 
            # invocation of the interpreter, either read from a script file or 
            # interactively, are considered part of a module called __main__, 
            # so they have their own global namespace.
        # Local namespace or function namespace:
            # The local namespace for a function is created when the function 
            # is called, and deleted when the function returns or raises an 
            # exception that is not handled within the function. (Actually, 
            # forgetting would be a better way to describe what actually 
            # happens.) Of course, recursive invocations each have their own 
            # local namespace.


# Scoping:
    # What is it?
        # A scope is a textual region of a Python program where a namespace is 
        # directly accessible.
    # Types of scope:
        # -> the innermost scope, which is searched first, contains the local names
        # -> the scopes of any enclosing functions, which are searched starting with the nearest enclosing scope, contains non-local, but also non-global names
        # -> the next-to-last scope contains the current module’s global names
        # -> the outermost scope(searched last) is the namespace containing built-in names
    # Global vs nonlocal scope:
        # If a name is declared global, then all references and assignments go 
        # directly to the middle scope containing the module’s global names. To 
        # rebind variables found outside of the innermost scope, the nonlocal 
        # statement can be used if not declared nonlocal, those variables are 
        # read-only(an attempt to write to such a variable will simply create a 
        # new local variable in the innermost scope, leaving the identically 
        # named outer variable unchanged).
    # Relative perspective:
        # Usually, the local scope references the local names of the(textually) 
        # current function. Outside functions, the local scope references the 
        # same namespace as the global scope: the module’s namespace. Class 
        # definitions place yet another namespace in the local scope.
    # Textual vs dynamic scope search:
        # It is important to realize that scopes are determined textually: the 
        # global scope of a function defined in a module is that module’s 
        # namespace, no matter from where or by what alias the function is 
        # called. On the other hand, the actual search for names is done 
        # dynamically, at run time — however, the language definition is 
        # evolving towards static name resolution, at “compile” time, so don’t 
        # rely on dynamic name resolution! (In fact, local variables are already 
        # determined statically.)
    # Assignments:
        # A special quirk of Python is that – if no global statement is in 
        # effect – assignments to names always go into the innermost scope. 
        # Assignments do not copy data — they just bind names to objects. The 
        # same is true for deletions: the statement del x removes the binding of 
        # x from the namespace referenced by the local scope. In fact, all 
        # operations that introduce new names use the local scope: in particular, 
        # import statements and function definitions bind the module or function 
        # name in the local scope.
    # global vs nonlocal statements:
        # -> global - The global statement can be used to indicate that particular 
        #             variables live in the global scope and should be rebound there
        # -> nonlocal - indicates that particular variables live in an enclosing 
        #               scope and should be rebound there.
        # Syntax:
            # def scope_test():
            #     def do_local():
            #         spam = "local spam"

            #     def do_nonlocal():
            #         nonlocal spam
            #         spam = "nonlocal spam"

            #     def do_global():
            #         global spam
            #         spam = "global spam"

            #     spam = "test spam"
            #     do_local()
            #     print("After local assignment:", spam)
            #     do_nonlocal()
            #     print("After nonlocal assignment:", spam)
            #     do_global()
            #     print("After global assignment:", spam)

            # scope_test()
            # print("In global scope:", spam)

            # The output of the example code is:
            # After local assignment: test spam
            # After nonlocal assignment: nonlocal spam
            # After global assignment: nonlocal spam
            # In global scope: global spam

