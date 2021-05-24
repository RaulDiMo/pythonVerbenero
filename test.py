import unittest
from pprint import pprint


x = 2
if x < 0:
   x = 0
   x = 'Negative changed to zero'
elif x == 0:
   x = 'Zero'
elif x == 1:
   x = 'Single'
else:
   x = 'More than one'

print(x)
