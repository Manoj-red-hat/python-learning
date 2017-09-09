


Trivia :
1> Need to see location of imported module : <module-name>.__file__
2>To see all membors present in module : dir(<module-name>)
3> Help on particular API : help(<module-name>.<interface-name>)

#########Example-1####################
dir(...)
    dir([object]) -> list of strings

    Return an alphabetized list of names comprising (some of) the attributes
    of the given object, and of attributes reachable from it:

    No argument:  the names in the current scope.
    Module object:  the module attributes.
    Type or class object:  its attributes, and recursively the attributes of
        its bases.
    Otherwise:  its attributes, its class's attributes, and recursively the
        attributes of its class's base classes.
#########Example-2 - Name of source file####################
>>> os.__file__
'/usr/lib64/python2.4/os.pyc'

######Example-3 Name of Module ##############
>>>>>> import os as os1
>>> os1.__name__
'os' --->Original Name

################4>Purpose of __init__.py file###############
Files named __init__.py are used to mark directories on disk as a Python package directories. If you have the files
mydir/spam/__init__.py
mydir/spam/module.py

and mydir is on your path, you can import the code in module.py as:
import spam.module
or
from spam import module
If you remove the __init__.py file, Python will no longer look for submodules inside that directory, so attempts to import the module will fail.

######Use of "__name__" :######
Every module has a name and statements in a module can find out the name of its module. This is especially handy in one particular situation - As mentioned previously, when a module is imported for the first time, the main block in that module is run. What if we want to run the block only if the program was used by itself and not when it was imported from another module? This can be achieved using the __name__ attribute of the module
#!/usr/bin/python
# Filename: using_name.py
if __name__ == '__main__':
	print 'This program is being run by itself'
else:
	print 'I am being imported from another module'
$ python using_name.py
This program is being run by itself

$ python
>>> import using_name
I am being imported from another module
>>>
########################################################################
>>> l = [1,2,3]  #l,m are similar to "void" pointers and type is associated with Object.
>>> m = [1,2,3]
>>> l == m  ###Checks for only equality
True
>>> l is m ### Checks whether both point to same Object
False
>>>
################################################################
Decorators : 
What ?    		--> Function wrappers
Why Required 	-->	Tming functions, preprocessing/post-processing for fn call without changing fn	
How ?

#Decorator Functionn
def mydecorator_shout(func):
    mydecorator_shout.counter = 0		#1
    def inner_fn(*args, **kwargs):
        mydecorator_shout.counter += 1 #As function are object , they can have data 
        print "Calling before"
        try:
            retValue =  func(*args, **kwargs)
        finally:
            print "Calling After"
        return retValue
    return inner_fn		#2
#1, #2 are called only oncer

#@mydecorator_shout
def fn_sample():
    print "hello Inside function"
    #raise Exception("Unknown Error")
    
f = mydecorator_shout(fn_sample)  [Similar to decorator]
#f now points to inner_fn

f()     #Counter --> 1
f()     #Counter --> 2
f()     #Counter --> 3
print mydecorator_shout.counter

print f.__name__ #F now points to inner_fn
##########################################################################

#Assignment vs shallow copy vs deep copy.
#1)Assignment :
a = [1,2,3]
b = a
#If "a" is changed in-place , b also gets changed.
a[0] = 'h'
print b #print ['h', 2, 3]
#If a is changed to some other 
a = "hello"
print b #Print ['h',2,3] [not changed]

#2)Shallow Copy
a = [1,2,3]
b = a[:]
a[0] = "helo"
print b #No change : [1,2,3]
#But if we have is complex Type it changes 
a = [[1,23], 2 ,3]
b = a[:]
a[0][1] = "Changed"
print b #[["Changed", 23], 2, 3]

#3)Deep Copy
a = [1,2,[1,23]]
import copy
b= copy.deepcopy(a)
a[2][1] = "hello"
print b #Unchanged --> [1,2,[1,23]]
###############################################################################
Lambda create runtime functions 
fn_square = lambda x:x**2
print fn_square(3)

####################imports ##########
After the first import, later imports do nothing –  even if the source file is modified.
If it is required that Python must run the file again in the same session (without stopping and restarting the session) –
 call the reload function available in the imp standard library module as follows :
 >>> from imp import reload
	>>> reload(first)
The reload function expects the name of an already loaded module object

############################
A set itself is a mutable object , but can contain only immutable objects.
A tuple is a immutable object but can contain mutable objects.
###########################
Q > What is Iterator and Iterable ?
1.Iterable : Any object which can be iterated, an object that supports the iter call.
2.Iterator : Object which iterates on iterable object .(Created by iter() function)
iterable_list = [1,2,3]
iterable_object = iter(iterable_list)
iterable_object.next()   --> "1" 
iterable_object.next()   --> "2"
iterable_object.next()   --> "3"
iterable_object.next()   --> Raise StopIteration Exception
############################################################################

Function -->
1)is an Object.
2)Created by : def , lambda
3)Returns by : return, yield
4)For mutable --> Call by Reference ; For immutable --> Call by value
5)For variable number of arguments we can use : *args , **kwargs
	*args --> Positional arguments are converted to tuple
	**kwargs --> Key-value parameters are converted to dictionary.	
6) scope of variables can be changed by using "global <var-1>, <var-2>" this means they are modifiying globals.
	
############MAP , FILTER, REDUCE ##########
#Syntax : map(function, iterable1, iterable2,...)
#map helps to easily apply an operation on a collection
#Returns : list
#Ex-1 (using function)
def f_sq(x):
	return x**2
map(f_sq, range(1,3))
#Ex-2 (using function - 2 iterables)
def f_mul(x,y):
	return x,y
#Ex-3 Using lambda functions
map(f_mul, range(1,3),range(3,5))
#Ex-3 : Using lambda
l = map (lambda x:x**2, range(3,5)) -->9,16

#Filter : 
#>filter(function, iterable) --> returns a list for which function(iterable[0]) == true for x in len(iterable)
l = filter(lambda x:x%2==0, range(1,24))

#Reduce : 
reduce(function, iterable)
Ex : reduce(lambda x,y:x+y, [1,2,3,4])
Steps of calling :
fn(1,2) --> 3
fn(3,3) -->6
fn(6,4) --> 10
Returns single object and not an iterable.

#######Generator Function####
Has yield keyword, state of function is saved.
def gen_num(value):
	while value < 10:
		yield value
		value += 1

		
gen_obj = gen_num(7)
gen_obj.next() #-->"8"
gen_obj.next() # -->"9"
gen_obj.next() # -->Raise StopIteration
###############Generator Object ######
Similar to list comprehension in notation but very different
Ex 
gen_obj = ( x**x for x in [1,2,3])
gen_obj.next() #1
gen_obj.next() #4
gen_obj.next() #9
gen_obj.next() #-->StopIteration Exception raised
########################################

# Howto pack data into c-type structs ?
structValue = struct.pack('hl', 5,6.5)
a,b=struct.unpack('hl',structValue)

####################################

# New Style class.
>>> class Emp(object):
	pass
#Old Style class.
>>> class Emp_old:
	pass

>>> type(Emp)
<type 'type'>
>>> type(Emp_old)
<type 'classobj'>
>>> 
>>> 
>>> e1 = Emp() ; e2 = Emp_old()
>>> type(e1)
<class '__main__.Emp'>
>>> type(e2)
<type 'instance'>

#####Class Dictionary vs instance dictionary		
		
>>> class Emp(object):
		PI = 2.14
		def __init__(self, real, imag):
			self.real = real
			self.imag = imag

#Class dictionary
>>> print (Emp.__dict__)
{'__module__': '__main__', '__dict__': <attribute '__dict__' of 'Emp' objects>, 'PI': 2.1400000000000001, '__weakref__': <attribute '__weakref__' of 'Emp' objects>, '__doc__': None, '__init__': <function __init__ at 0x025911F0>}
>>> e1 = Emp(3,4)
#Instance Dictionary
>>> e1.__dict__
{'real': 3, 'imag': 4}

#e1.__class__ == Emp 
#below call is same as Emp.__dict__.
>>> e1.__class__.__dict__
<dictproxy object at 0x02588AD0>
>>> print (e1.__class__.__dict__)
{'__module__': '__main__', '__dict__': <attribute '__dict__' of 'Emp' objects>, 'PI': 2.1400000000000001, '__weakref__': <attribute '__weakref__' of 'Emp' objects>, '__doc__': None, '__init__': <function __init__ at 0x025911F0>}
		
#Resolution of name:
Find the first occurrence of attribute by looking in object, then in all classes above it, from bottom to top and left to right
class e1(e2): pass
class e3(e4): pass
class e5(e1,e3) : pass

e5.x --> e5,e1,e2,e3,e4 [Attribute search]

#Name Mangling
>>> class x(object):
	pub = 5
	_prot = 6
	__private = 7
>>> print x.__dict__
{'_prot': 6, '__module__': '__main__', 'pub': 5, '_x__private': 7, '__dict__': <attribute '__dict__' of 'x' objects>, '__weakref__': <attribute '__weakref__' of 'x' objects>, '__doc__': None}
>>> x.pub
5
>>> x._prot
6
>>> x.__private
#ERROR
>>> x._x__private           classname._classname__private.
7
>>> 

#Public :
All member variables and methods are public by default in Python

#Protected :
The only way to have protected members in Python is via convention
This is done by prefixing the member name with a single underscore
its ONLY a convention that says : 'use this attr only in subclasses'
it is still accessible everywhere
so it is not really a protected member

#Private :
Any member name prefixed with at least two underscores and suffixed with at most one underscore is modified (name mangling) by Python
So a member name __mem or __mem_ or ___mem ... is stored in the class or instance dictionary as _class__mem or _class__mem_ ...
As a result of this name mangling, class users do not see any member by the name __mem ...
But such a member is actually still accessible as _class__mem



####Properties###
class C(object):
    def __init__(self):
        self._x = None

    @property
    def x(self):
        """I'm the 'x' property."""
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        del self._x
Why use ?
1) validation/filtering of the set attributes (forcing them to be in bounds or acceptable) 2
2) Handling complex logic/Complex calculation hidden behind an attribute.

##Database :
import MySQLdb
# Open database connection
db = MySQLdb.connect("localhost","root","sarank","employees" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Drop table if it already exist using execute() method.
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE1")

# Create table as per requirement
sql = "CREATE TABLE EMPLOYEE1 (\
         FIRST_NAME  CHAR(20) NOT NULL,\
         LAST_NAME  CHAR(20),\
         AGE INT,  \
         SEX CHAR(1),\
         INCOME FLOAT )"

cursor.execute(sql)
db.commit()
db.close()
		
		

		
		
		






