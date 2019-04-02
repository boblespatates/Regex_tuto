import re

#https://github.com/CoreyMSchafer/code_snippets/tree/master/Python-Regular-Expressions

text_to_search = '''
azertyuiop
azertyuio
azertyuHZZHZHA
abc
'''

sentence = 'Start a sentence and then bring it to an end'

# Allow to separate the patterns into a variable
# And make it easier to reuse that variable to perform
# Multiple searches

# Here we try to find urls (and 3 groups can be seen
pattern = re.compile(r'https?://(www\.)?(\w+)(\.w+)')

matches = pattern.finditer(text_to_search)

# Substitute with groupe 2 and 3
subbed_urls = pattern.sub(r'\2\3',urls)
# input : https://www.google.com
# output : google.com

# pattern.findall list all the find elements
# pattern.match return the begining match same as finditer
# pattern.search return the first match find but in the whole text
# re.compile(r'start', re.IGNORECASE) eventhought the pattern is in lower case
# It will search also the upper cases

with open('data.txt', 'r', encoding='utf-8') as f:
    contents = f.read()
    matches = pattern.finditer(contents)

for match in matches:
    print(match)
    # return ex : <_sre.SRE_Match object; span=(37, 40), match='abc'>
    # so contains all the matches
    # span is the begining and end index of the match
    # print(text_to_search[37:40])
    print(match.group(0)) 
    # the match
    print(match.group(1))
    # only the group 1
    # if there isn't it is set as none
