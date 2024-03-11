# https://campus.datacamp.com/courses/writing-functions-in-python/best-practices?ex=1

"""
docstring - indformacje

co robi funkcja

---------
opisanie dla funkcji
co robi
jakie argumenty



różne formaty:
google style
Numpydoc
reStructuredText
EdyText

różne standardy




dostep do docstring

nazwa_funkcji.__doc__

zawiera surowy tekst (wszystkie spacje tabulatory

aby dostać czystszą wersję (bez wiodacych spacji)
można wykorzystać

inspect.getdoc()
funkcję z moduły inspect


===================
import inspect
print(inspect.getdoc(tnazwa_funkcji))

----




https://s3.amazonaws.com/assets.datacamp.com/production/course_15876/slides/chapter1.pdf#pdfjs.action=download
nie mozna pobrać !!!
"""

# Add a docstring to count_letter()
def count_letter(content, letter):
  """Count the number of times `letter` appears in `content`.
  :param content:
  :param letter:
  :return:
  """
  if (not isinstance(letter, str)) or len(letter) != 1:
    raise ValueError('`letter` must be a single character string.')
  return len([char for char in content if char == letter])


"""
# Get the "count_letter" docstring by using an attribute of the function
docstring = count_letter.__doc__

border = '#' * 28
print('{}\n{}\n{}'.format(border, docstring, border))



dir(nazwa_funkcji)   __doc__


tworzymy funkcję

inspect


"""

def build_tooltip(func):
  return func.__doc__


"""
identyfikacja funckji w pakietach

numpy.histogram

"""



"""
DRY
dont repeat yourself



użyj funckji do nie powtarza się
Zrób jedną rzecz na raz

zajmij się 1 rzeczą 
funkcje będą bardziej elastyczne

łatwiejszy do poprawy, zmiany debugowania, testowania, bardzie zrozumiały
refactor


 ---------------------
def standardize(column):
  """Standardize the values in a column.

  Args:
    column (pandas Series): The data to standardize.

  Returns:
    pandas Series: the values as z-scores
  """
  # Finish the function so that it returns the z-scores
  z_score = (____ - ____.____()) / ____.____()
  return z_score

# Use the standardize() function to calculate the z-scores
df['y1_z'] = ____
df['y2_z'] = ____
df['y3_z'] = ____
df['y4_z'] = ____


# Standardize the GPAs for each year
df['y1_z'] = (df.y1_gpa - df.y1_gpa.mean()) / df.y1_gpa.std()
df['y2_z'] = (df.y2_gpa - df.y2_gpa.mean()) / df.y2_gpa.std()
df['y3_z'] = (df.y3_gpa - df.y3_gpa.mean()) / df.y3_gpa.std()
df['y4_z'] = (df.y4_gpa - df.y4_gpa.mean()) / df.y4_gpa.std()

 
 Use the function to calculate the z-scores for each year (df['y1_z'], df['y2_z'], etc.) from the raw GPA scores (df.y1_gpa, df.y2_gpa, etc.).
 
 (df.y1_gpa - df.y1_gpa.mean()) / df.y1_gpa.std() is only performing operations on df.y1_gpa. So you should be able to pass df.y1_gpa as the column argument to the standardize() function.
 
 
 
 
 
 
 ===================
 def mean(values):
  """Get the mean of a sorted list of values

  Args:
    values (iterable of float): A list of numbers

  Returns:
    float
  """
  # Write the mean() function
  ____ = ____
  return mean
  
==================
Split up a function
Another engineer on your team has written this function to calculate the mean and median of a sorted list. You want to show them how to split it into two simpler functions: mean() and median()

def mean_and_median(values):
  """Get the mean and median of a sorted list of `values`

  Args:
    values (iterable of float): A list of numbers

  Returns:
    tuple (float, float): The mean and median
  """
  mean = sum(values) / len(values)
  midpoint = int(len(values) / 2)
  if len(values) % 2 == 0:
    median = (values[midpoint - 1] + values[midpoint]) / 2
  else:
    median = values[midpoint]

  return mean, median
  
    
    
===================
answer

def mean(values):
  """Get the mean of a sorted list of values

  Args:
    values (iterable of float): A list of numbers

  Returns:
    float
  """
  # Write the mean() function
  mean = sum(values) / len(values)
  return mean
  





qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq
pass by assignment
przekazanie przez zadanie


def foo(x):
  x[0]==99
my_list=[1,2,3]
foo(my_list)

 print(my_list)
 
 zmienione !!!!!!!!!!!!
 mutuje !!!
 
 
 3 nie mutuje 
  
  
  wskazanie a na pamięc wartośc /wskaźnik
  
  a=[1,2,3]
  
  b= a[:]
  
  
  
  >>> a=[1,2,3]                                                         
>>> b=a[:]  !!!!!!!!!!!!!!!!!!! kopia listy - ale co z elementami jeśli sa wskaźnikami obiektami!!!!
>>> b
[1, 2, 3]
>>> a[0]=1223
>>> a
[1223, 2, 3]
>>> b
[1, 2, 3]
>>>

===============

b=a 
a.append(5)
zmiania i a i b


---------pay by assignment
mutowanie !!!!


def bar(x)
  x=x+90
  
my_var =3
bar(my_var


NIE MUTUJĄ
int
float
bool
string
bytes
tuple
frozenset
None



MUTUJĄ:
list
dict
set
bytearray
objects
functions
i prawie wszystko inne  

  
!!!!!!!!!!!!!!!!!!!!!!



def foor(var=[])
  var.append(1)
  return var
  
foo() => [1]

foo() => [1,1]
  
  
  
  
  
  czy mutuje
def store_lower(_dict, _string):
  """Add a mapping between `_string` and a lowercased version of `_string` to `_dict`

  Args:
    _dict (dict): The dictionary to update.
    _string (str): The string to add.
  """
  orig_string = _string
  _string = _string.lower()
  _dict[orig_string] = _string

d = {}
s = 'Hello'

store_lower(d, s)

  
  
  
  
  
  
  
  
  
  Best practice for default arguments
One of your co-workers (who obviously didn't take this course) has written this function for adding a column to a pandas DataFrame. Unfortunately, they used a mutable variable as a default argument value! Please show them a better way to do this so that they don't get unexpected behavior.

def add_column(values, df=pandas.DataFrame()):
  """Add a column of `values` to a DataFrame `df`.
  The column will be named "col_<n>" where "n" is
  the numerical index of the column.

  Args:
    values (iterable): The values of the new column
    df (DataFrame, optional): The DataFrame to update.
      If no DataFrame is passed, one is created by default.

  Returns:
    DataFrame
  """
  df['col_{}'.format(len(df.columns))] = values
  return df
  
======================
# Use an immutable variable for the default argument
def better_add_column(values, df=____):
  """Add a column of `values` to a DataFrame `df`.
  The column will be named "col_<n>" where "n" is
  the numerical index of the column.

  Args:
    values (iterable): The values of the new column
    df (DataFrame, optional): The DataFrame to update.
      If no DataFrame is passed, one is created by default.

  Returns:
    DataFrame
  """
  # Update the function to create a default DataFrame
  if ____ is ____:
    df = pandas.DataFrame()
  df['col_{}'.format(len(df.columns))] = values
  return df
  
 
 Change the default value of df to an immutable value to follow best practices.
Update the code of the function so that a new DataFrame is created if the caller didn't pass one.

  https://s3.amazonaws.com/assets.datacamp.com/production/course_15876/slides/chapter1.pdf#pdfjs.action=download
  
   
"""


"""
context manager

with 
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

co oznacza with - context managert

konwencja managera kontekstu!!!

If you've ever seen the "with" keyword in Python and wondered what its deal was, then this is the chapter for you! Context managers are a convenient way to provide connections in Python and guarantee that those connections get cleaned up when you are done using them. This chapter will show you how to use context managers, as well as how to write your own.



1. Using context managers
00:00 - 00:07
In this lesson, I'll introduce the concept of context managers and show you how to use these special kinds of functions.

2. What is a context manager?
00:07 - 00:21
A context manager is a type of function that sets up a context for your code to run in, runs your code, and then removes the context. That's not a very helpful definition though, so let me explain with an analogy.

3. A catered party
00:21 - 00:28
Imagine that you are throwing a fancy party, and have hired some caterers to provide refreshments for your guests.

4. A catered party
00:28 - 00:33
Before the party starts, the caterers set up tables with food and drinks.

5. A catered party
00:33 - 00:38
Then you and your friends dance, eat, and have a good time.

6. A catered party
00:38 - 00:40
When the party is done,

7. A catered party
00:40 - 00:42
the caterers clean up the food and remove the tables.

8. Catered party as context
00:42 - 01:07
In this analogy, the caterers are like a context manager. First, they set up a context for your party, which was a room full of food and drinks. Then they let you and your friends do whatever you want. This is like you being able to run your code inside the context manager's context. Finally, when the party is over, the caterers clean up and remove the context that the party happened in.

9. A real-world example
01:07 - 01:49
You may have used code like this before. The "open()" function is a context manager. When you write "with open()", it opens a file that you can read from or write to. Then, it gives control back to your code so that you can perform operations on the file object. In this example, we read the text of the file, store the contents of the file in the variable "text", and store the length of the contents in the variable "length". When the code inside the indented block is done, the "open()" function makes sure that the file is closed before continuing on in the script. The print statement is outside of the context, so by the time it runs the file is closed.

10. Using a context manager
01:49 - 01:58
Any time you use a context manager, it will look like this. The keyword "with" lets Python know that you are trying to enter a context.

11. Using a context manager
01:58 - 02:09
Then you call a function. You can call any function that is built to work as a context manager. In the next lesson, I'll show you how to write your own functions that work this way.

12. Using a context manager
02:09 - 02:13
A context manager can take arguments like any normal function.

13. Using a context manager
02:13 - 02:19
You end the "with" statement with a colon as if you were writing a for loop or an if statement.

14. Using a context manager
02:19 - 02:39
Statements in Python that have an indented block after them, like for loops, if/else statements, function definitions, etc. are called "compound statements". The "with" statement is another type of compound statement. Any code that you want to run inside the context that the context manager created needs to be indented.

15. Using a context manager
02:39 - 02:49
When the indented block is done, the context manager gets a chance to clean up anything that it needs to, like when the "open()" context manager closed the file.

16. Using a context manager
02:49 - 03:17
Some context managers want to return a value that you can use inside the context. By adding "as" and a variable name at the end of the "with" statement, you can assign the returned value to the variable name. We used this ability when calling the "open()" context manager, which returns a file that we can read from or write to. By adding "as my_file" to the "with" statement, we assigned the file to the variable "my_file".

17. Let's practice!
03:17 - 03:27
You'll learn how to write your own context managers in the next lesson. For now, you can practice using them in order to understand how they work.




filmik

!!!!!!!!



menadźer kontekstu to rodzaj funkcji , która definiuje kontext
do uruchomienia kodu 
a nastepnie usuwa kontekst

nie jest to bardzo pomocna definicja wiec wyjaśnienie wymaga analogii




zatrudniacie firmę kateringową .
jak zaczyna się impreza firma zastawia słoły jedzeniem i trunkami

kiedy trwa impreza bawicie się

kiedy się kończy to firmy sprzątają jedzenie i usuwają zastaweę ze stołów , sprzataja



firma kateringowa to menadzer kontekstu

bez kontekstu mamy zwykłe stoły do konferencji
w kontekscie salę balowa



kontekst manager :     caterers:
set up kontekst     set up the tables with foot and drink

run your kode z użyciem kontekstu    let uoy and your friend have a party

remove the kontekst    clear up and removed the tables

impreza się odbyła



-------------

with open("my_file.txt") as my_file:
  text= my_file.read()
  length = len(text)
  
  print('the file is {} charakter long'.format(length))


---------------
jak uruchamiamy konteks manadzer to  otwierany jest plik i przypisywany do konkekstu  my_file

potem korzystamy z kontekstu



na zakończenie usuwa kontekst i tak zamyka plik 
"""

poza kontekstem nie ma już kontekstu





with informuje o rozpoczęciu kontekstu


with <ontextmanager>(<rgs>)  as <variable-name>:
  #run your code hier using context


# kontext removed

------------------

dodając as i nazwę zmiennej na końcu
można przypisać zwróconą wartość do nazwy zmiennej

używane w open(file)



==================================================================
# Open "alice.txt" and assign the file to "file"
with open('alice.txt') as file:
  text = file.read()

n = 0
for word in text.split():
  if word.lower() in ['cat', 'cats']:
    n += 1

print('Lewis Carroll uses the word "cat" {} times'.format(n))

liczba cats w pliku textowym - powieści o Alicji

cat cats



================================================================
image = get_image_from_instagram()

# Time how long process_with_numpy(image) takes to run
____ ____:
  print('Numpy version')
  process_with_numpy(image)

# Time how long process_with_pytorch(image) takes to run
____ ____:
  print('Pytorch version')
  process_with_pytorch(image)



https://s3.amazonaws.com/assets.datacamp.com/production/course_15876/slides/chapter2.pdf#pdfjs.action=download




Exercise
Exercise
The speed of cats
You're working on a new web service that processes Instagram feeds to identify which pictures contain cats (don't ask why -- it's the internet). The code that processes the data is slower than you would like it to be, so you are working on tuning it up to run faster. Given an image, image, you have two functions that can process it:

process_with_numpy(image)
process_with_pytorch(image)
Your colleague wrote a context manager, timer(), that will print out how long the code inside the context block takes to run. She is suggesting you use it to see which of the two options is faster. Time each function to determine which one to use in your web service.



Use the timer() context manager to time how long process_with_numpy(image) takes to run.
Use the timer() context manager to time how long process_with_pytorch(image) takes to run.




The timer() context manager does not take any arguments.
The timer() context manager doesn't yield a value, so you don't need an as <variable name> in your with statement.



with image:





  PISANIE swojego kontekstmanagera

1.
Writing
context
managers
00: 00 - 00:06
Now
that
you
know
how
to
use
context
managers, I
want
to
show
you
how
to
write
a
context
manager
for other people to use.

2.
Two
ways
to
define
a
context
manager
00: 06 - 00:20
There
are
two
ways
to
define
a
context
manager in Python: by
using
a


class that has special __enter__() and __exit__() methods or by decorating a certain kind of function.


3.
Two
ways
to
define
a
context
manager
00: 20 - 00:29
This
course is focused
on
writing
functions, and some
of
you
may
not have
been
introduced
to
the
concept
of
classes
yet, so
I
will
only
present
the
function - based
method
here.

4.
How
to
create
a
context
manager
00: 29 - 00:58
There
are
five
parts
to
creating
a
context
manager.First, you
need
to
define
a
function.Next, you
can
add
any
setup
code
your
context
needs.This is not required
though.Third, you
must
use
the
"yield"
keyword
to
signal
to
Python
that
this is a
special
kind
of
function.I
will
explain
what
this
keyword
means in a
moment.After
the
"yield"
statement, you
can
add
any
teardown
code
that
you
need
to
clean
up
the
context.

5.
How
to
create
a
context
manager
00: 58 - 01:22
Finally, you
must
decorate
the
function
with the "contextmanager" decorator from the "contextlib" module.You might not know what a decorator is, and that's ok. We will discuss decorators in-depth in the next chapter of this course. For now, the important thing to know is that you write the "at" symbol, followed by "contextlib.contextmanager" on the line immediately above your context manager function.

6.
The
"yield"
keyword
01: 22 - 02:10
The
"yield"
keyword
may
also
be
new
to
you.When
you
write
this
word, it
means
that
you
are
going
to
return a
value, but
you
expect
to
finish
the
rest
of
the
function
at
some
point in the
future.The
value
that
your
context
manager
yields
can
be
assigned
to
a
variable in the
"with"
statement
by
adding
"as <variable name>".Here, we
've assigned the value 42 that my_context() yields to the variable "foo". By running this code, you can see that after the context block is done executing, the rest of the my_context() function gets run, printing "goodbye". Some of you may recognize the "yield" keyword as a thing that gets used when creating generators. In fact, a context manager function is technically a generator that yields a single value.

7.
Setup and teardown
02: 10 - 02:32
The
ability
for a function to yield control and know that it will get to finish running later is what makes context managers so useful.This context manager is an example of code that accesses a database.Like most context managers, it has some setup code that runs before the function yields.This context manager uses that setup code to connect to the database.

8.
Setup and teardown
02: 32 - 02:43
Most
context
managers
also
have
some
teardown or cleanup
code
when
they
get
control
back
after
yielding.This
one
uses
the
teardown
section
to
disconnect
from the database.

9.
Setup and teardown
02: 43 - 02:59
This
setup / teardown
behavior
allows
a
context
manager
to
hide
things
like
connecting and disconnecting
from a database

so
that
a
programmer
using
the
context
manager
can
just
perform
operations
on
the
database
without
worrying
about
the
underlying
details.

10.
Yielding
a
value or None
02: 59 - 03:25
The
database()
context
manager
that
we
've been looking at yields a specific value - the database connection - that can be used in the context block. Some context managers don'
t
yield an
explicit
value.in_dir() is a
context
manager
that
changes
the
current
working
directory
to
a
specific
path and then
changes
it
back
after
the
context
block is done.It
does
not need
to
return anything
with its "yield" statement.

11.
Let
's practice!
03: 25 - 03:30
Now
it
's your turn to practice writing context managers.


2 sposoby tworzenia


albo
class-based


metody __enter__()
i
__exit()__

lub dekorując określnony rodzaj funkcji


)



function_bases

5 części:

1)zdefiniuj funckję
2) dodaj dowolny kod konfiguracyjny , którego potrzebuje twój kontext  (optional)
3) użyj yield aby zasygnalizować specjalny rodzaj funkcji (generator)
4) po yield dodaj dowolny kod rozłączenia , który jest potrzebny do wyczyszczenia kontekstu
na przykład zamknięci połączeń do bazy , otwarcie pliku itd
5( na koniec dekorujesz funkcję dekoratorem
"contextmanager" z modułu
"contextlib")


on załatwia (resztę



@cintextlib.contextmanager
def my_context():
  # Add any set up code you need
  yield
  # add any teardown code you need


========================

@cintextlib.contextmanager
def my_context():
  print('hello')
  yield 42
  print('goodby')


to co zwraca yield można przypisać jak "as"



with my_context() as foo:
  print("foo is {}".format(foo))


!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


hello fo is 42
goodby



yield zwraca wartość która bedzie znana w przyszłości












