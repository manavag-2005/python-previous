#datetime
import datetime
print(datetime.datetime.now())
print(datetime.datetime(2023 , 10,20,10,30,0))
print(datetime.datetime.now().strftime("%m/%d/%y %H:%M:%S"))
date1 = datetime.datetime(2023, 10,20,10,30,0)
date2 = datetime.datetime.now()
print(date1 - date2)


#math
import math
x=10.83
print(math.ceil(x))
print(math.floor(x))
print(math.trunc(x))

x=3
print(math.exp(x))
print(math.log10(x))

x=90
print(math.sin(x))
print(math.cos(x))
print(math.tan(x))

print(math.pi)
print(math.e)

print(10, math.factorial(10))


#random
import random

random.seed(40)
print(random.random())
print(random.randint(1,11))
print(random.choice([1 , 2 ,3 , 4 , 5]))
print(random.sample([1 , 2,  3 , 4] , 2))
print(random.uniform(1.0 , 3.0))


#collection
from collections import Counter, defaultdict , OrderedDict
lst = [ 1 , 2 , 3 , 3 , 5 , 5 , 6 , 3 , 2 ]
print(Counter(lst))

d = defaultdict(int)
d['a']+=1
print(d)

a = OrderedDict()
a['a'] = 1
a['b']=2
print(a)


#string
import string
print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.digits)
print(string.hexdigits)
print(string.octdigits)
print(string.punctuation)