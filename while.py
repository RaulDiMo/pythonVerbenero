import unittest
from pprint import pprint

vector = [1, 2, 3, 4, 5]
i = 0
string = ""
while (i < len(vector)):
    string = string + str(vector[i])
    i = i + 1

print(i)