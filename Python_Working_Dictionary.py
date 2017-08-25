# This file is for working with dictionaries in python

import numpy as np
import json

dict = {}

dict['python'] = ['ali','bita']
dict['java'] = ['book','pc','android']
dict['C++'] = ['rrrr', 'fast']
dict['ruby'] = ['web']

a  = dict['java'] + dict['ruby']
print a

c = 'test'
tags = 'python,java,ruby'

print '========='
print tags.split(',')
print '========='

for t in tags.split(','):
	tmp = dict[t]
	tmp.append(c)
	dict[t] = tmp

print dict['python']

## saving the dictionary to a file
np.save('myFile.npy', dict)

## Loading the dictionary
loadeddict = np.load('myFile.npy').item()
print loadeddict.keys()

loadeddict['newkey'] = ['val1', 'val2']

print loadeddict.keys()
print loadeddict['newkey']

print('**********************')
## Using Json for storing the tags

"Save data to file"
json.dump(dict, open("json_dict.txt",'w'))

"Read File"
loaded_json = json.load(open("json_dict.txt"))

print(loaded_json)
print(loaded_json['C++'])

"Check validity of json data with original"
print(loaded_json['C++']==dict['C++'])

"Saving to anotehr file type"
json.dump(dict,open("json_dict.kkk",'w'))
other_loaded_json = json.load(open("json_dict.kkk"))

print(other_loaded_json['C++'])

"Check validity of json data with original"
print(other_loaded_json['C++']==dict['C++'])