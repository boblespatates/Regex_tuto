# Library to use regex
import re

"""
Identifier :

\d any numbers
\D anything but a number

\s any space
\S anything but a space

\w any char
\W anything but a char

. anythin except a nex line
\b white space around words
\. a period

Modifier :

{1,3} 1 to 3 things are expected ex :\d{1,3}
+ match 1 or more
? match 0 or 1
* match 0 or more
$ matche the end of a sting
^ match the beginning of a string
| or
[] range ex : [A-Z][a-z]
{n} the expecting n amount

White space char :
\n new line
\s space
\t tab
\e escap
\f form feed
\r return

Need to be escaped :
. + * ? [ ] $ ^ ( ) { } | \
"""

exampleString = ''' Jessica is 15 years old, and Daniel is 27 years old
		Edward is 97, and his grand father, Oscar, is 102 '''
# Findall find all the entities in the text
ages = re.findall(r'\d{1,3}', exampleString)

names = re.findall(r'[A-Z][a-z]*', exampleString)

# Create a dictionnary
ageDict = {}
n = 0

# Feed the dictionnary
# Each person must have an age
for eachName in names:
	ageDict[eachName] = ages[n]
	n+=1

print(ageDict)
