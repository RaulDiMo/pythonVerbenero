import unittest
from pprint import pprint
words = ['cat', 'window', 'defenestrate']
string = ""
for w in words:
    string = string + w + "," + str(len(w)) +";"
print(w)