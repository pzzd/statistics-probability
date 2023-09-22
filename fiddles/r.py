import os, sys

modules_path = os.path.join(os.path.dirname(__file__), '..', 'modules')
print (modules_path)

sys.path.append(modules_path)
import my_stat_functions as my

my.say_hello()

r = my.correlation_coefficient ([1,2,2,3], [1,2,3,6])
print ('r ', r)
