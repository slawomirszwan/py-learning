"""
regex

wyodrębnianie okreslonych danych
parseowanie

String - sekwencja znaków
"""
"""
a = "hello"
b = 'hello'

len(a)

str(123)

index:

a[2]
a[-1]


0 1 2 3 4 

-4 -3 -2 -1

a[0:3]

a[:5]
a[5:]


x = "Awesome day"
x[0:3]

x[:5]
Aweso
x[5:]
me day



x[0:8:2]  

co drugi znak



a+b

a[1]

a[-1]



x[::-1]
odwrócony ciąg !!!!!!!!!!



x.lower()
x.upper()
x.capitalize()

my_string = "This string will be split"
my_string.split(sep=" ", maxsplit=2)
['This', 'string', 'will be split']




my_string.rsplit(sep=" ", maxsplit=2)
['This string will',  'be', 'split']



my_string = "This string will be split\nin two"
print(my_string)

\n 
\r 

my_string = "This string will be split\nin two"


my_string.splitlines()
['This string will be split','in two']


my_list = ["this","would","be","a","string"]
print(" ".join(my_list))



sep.join(iterable)




my_string = " This string will be stripped\n"
my_string.strip()




my_string = " This string will be stripped\n"
my_string.rstrip()


' This string will be stripped'
my_string.lstrip()
'This string will be stripped\n'


string.find(substring, start,end)


my_string = "Where's Waldo?"
my_string.find("Waldo")
8



my_string = "Where's Waldo?"
my_string.find("Waldo", 0, 6)
-1

my_string.find("Wenda")
-1

------------------
string.index(substring, start, end)

my_string = "Where's Waldo?"
my_string.index("Waldo")
8


my_string.index("Wenda")
File "<stdin>"
, line 1, in <module>
ValueError: substring not found


--------------------

my_string = "Where's Waldo?"

try:
    my_string.index("Wenda")
except ValueError:
    print("Not found")

"Not found"

--------------------

string.count(substring, stat, end)

my_string = "How many fruits do you have in your fruit basket?"
my_string.count("fruit")
2

my_string.count("fruit", 0, 16)
1

-----------
string.replace(old, new, count)

my_string = "The red house is between the blue house and the old house"
print(my_string.replace("house", "car"))

The red car is between the blue car and the old car

---
print(my_string.replace("house","car", 2))
The red car is between the blue car and the old house





length_string = len(movie)

"""

# Select the first 32 characters of movie1
movie1 = "0123456789"*40
first_part = movie1[:32]
print(f"{first_part=}", f"{len(first_part)=}")


# ----------------------
"""
 palindromes
Madam or No lemon, no melon

czaytane od początku i od końca to samo
"""
"""
# # Get the word
# movie_title = ____[____]
#
# # Obtain the palindrome
# palindrome = ____[____]
#
# # Print the word if it's a palindrome
# if movie_title == palindrome:
# 	print(____)

# Get the word  od 12 znaku do 30 znaku
movie_title = movie[11:30]

# Obtain the palindrome
# kolejność odwrotna
palindrome = movie_title[::-1]

# Print the word if it's a palindrome
if movie_title == palindrome:
	print(movie_title)

"""


"""
metody stringa

str.lower
str.upper
str.csapitalize


# Convert to lowercase and print the result
movie_lower = movie.lower()
print(movie_lower)

# Remove tags happening at the end and print results
movie_tag = ____
print(____)

string.rstrip(char)

------------------
# Split string at line boundaries
file_split = ____

# Print file_split
print(____)

# Complete for-loop to split by commas
for ____ in ____:
    substring_split = substring.____
    print(substring_split)
    
---------------------
for movie in movies:
  	# If actor is not found between character 37 and 41 inclusive
    # Print word not found
    if movie.find("____", ____, ____) == ____:
        print("Word not found")
    # Count occurrences and replace two with one
    elif movie.____("____") == 2:  
        print(movie.replace("____", "____"))
    else:
        # Replace three occurrences with one
        print(movie.replace("____", "____"))
        
 
-------
for movie in movies:
  	# If actor is not found between character 37 and 41 inclusive
    # Print word not found
    if movie.find("actor", 37, 42) == -1:
        print("Word not found")
    # Count occurrences and replace two with one
    elif movie.count("actor") == 2:  
        print(movie.replace("actor actor", "actor"))
    else:
        # Replace three occurrences with one
        print(movie.replace("actor actor actor", "actor"))
        
---
 Find the index where money occurs between characters with index 12 and 50. If not found, the method should return -1.
 
for movie in movies:
  # Find the first occurrence of word
  print(movie.find("money", 12, 51))
  
 Find the index where money occurs between characters with index 12 and 50. If not found, it should raise an error.
 
------------
# Replace negations 
movies_no_negation = movies.____("____", "____")

# Replace important
movies_antonym = movies_no_negation.____("____", "____")

# Print out
____

 Replace the substring isn't with the word is.
Replace the substring important with the word insignificant.
Print out the result contained in the variable movies_antonym
  
# Replace negations 
movies_no_negation = movies.replace("isn't", "is")

# Replace important
movies_antonym = movies_no_negation.replace("important", "insignificant")

# Print out
print(movies_antonym)
           
"""


"""
positional formatting


custom_string = "String formatting"
print(f"{custom_string} is a powerful technique")
String formatting is a powerful technique





Methods for formatting
Positional formatting
Formatted string literals
Template method


print("Machine learning provides {} the ability to learn {}".format("systems","automatically"))


my_string = "{} rely on {} datasets"
method = "Supervised algorithms"
condition = "labeled"
print(my_string.format(method, condition))




print("{} has a friend called {} and a sister called {}"
.format("Betty"
,
"Linda"
,
"Daisy"))



print("{2} has a friend called {0} and a sister called {1}".format("Betty","Linda","Daisy"))

nazwane placeholdery

tool="Unsupervised algorithms"
goal="patterns"
print("{title} try to find {aim} in the dataset".format(title=tool, aim=goal))
Unsupervised algorithms try to find patterns in the dataset


my_
methods = {"tool": "Unsupervised algorithms"
,
"goal": "patterns"}
print('{data[tool]} try to find {data[goal]} in the dataset'
.format(data=my_
methods))
Unsupervised algorithms try to find patterns in the dataset


print("Only {0:f}% of the {1} produced worldwide is {2}!"
.format(0.5155675,
"data"
,
"analyzed"))
Only 0.515568% of the data produced worldwide is analyzed!


dodanie sposobu formatowania




https://campus.datacamp.com/courses/regular-expressions-in-python/formatting-strings?ex=2

https://campus.datacamp.com/courses/regular-expressions-in-python/regular-expressions-for-pattern-matching?ex=3

,....................


"""