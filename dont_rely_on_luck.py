"""
Question URL
https://www.codewars.com/kata/dont-rely-on-luck/python
Question:
The test fixture I use for this kata is pre-populated.
In Python by:

randint(1,100)
You can pass by relying on luck or skill but try not to rely on luck.

"The power to define the situation is the ultimate power." - Jerry Rubin

Good luck!

Important thing was the test case which gives hint to solve problem

#This is exactly what the real test fixture looks like.
lucky_number = randint(1,100)
test.assert_equals(guess, lucky_number, "Sorry. Unlucky this time.")
"""

"""
Things i learned:
----------------
Learned random class. its methods like getstate, setstate, seed.
Also function overiding.
"""

from random import seed, randint
seed(1)
guess = randint(1,100)
seed(1)

"""
Other solution:
setting state of random geenrator:
----------------------------------
from random import randint, getstate,setstate

tmp = getstate()
guess = randint(1,100)
setstate(tmp)
"""

"""
Other Solution:
Overiding randint function itself as test cases were also 
written in randint:
------------------
def randint(a,b):
	return 10

guess = 10
"""

"""
Other Solution:
Overiding __eq__ function:
-------------------------

def EqualToMe(object):
	def __eq__(self, x):
		return True
guess = EqualToMe()
"""
