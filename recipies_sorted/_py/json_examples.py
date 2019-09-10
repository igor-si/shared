import os
import re
import sys
import json
import collections

def modes():
    r #(default mode) open the file for reading
    w #open the file for writing, overwriting the content if 
    #the file already exists with data
    
    x #creates a new file, failing if it exists
    a #open the file for writing, appending new data at 
    #the end of the file's contents if it already exists
    
    b #write binary data to files instead of the default text data
    
    "+" #allow reading and writing to a mode
    
    "w+" #Let's say you wanted to write to a file and 
    #then read it after

    "a+"
    #f you wanted to write and then read from a file, 
    #without deleting the previous contents then you'll use 

    write() # function we can take one string and put it into a file. 
    writelines() #function to put data in a sequence (like a list or tuple)

# ================ Decode list without U unicode
def _decode_list(data):
    rv = []
    for item in data:
        if isinstance(item, unicode):
            item = item.encode('utf-8')
        elif isinstance(item, list):
            item = _decode_list(item)
        elif isinstance(item, dict):
            item = _decode_dict(item)
        rv.append(item)
    return rv

def _decode_dict(data):
    rv = {}
    for key, value in data.iteritems():
        if isinstance(key, unicode):
            key = key.encode('utf-8')
        if isinstance(value, unicode):
            value = value.encode('utf-8')
        elif isinstance(value, list):
            value = _decode_list(value)
        elif isinstance(value, dict):
            value = _decode_dict(value)
        rv[key] = value
    return rv
# USAGE: = json.loads(s, object_hook=_decode_dict)
#===========================================
file_path = os.path.join(  os.path.dirname (os.path.realpath(__file__)),"trash")

import io
try:
    to_unicode = unicode
except NameError:
    to_unicode = str

# Define data
data = {'a list': [1, 42, 3.141, 1337, 'help', '23'],
        'a string': 'bla',
        'another dict': {'foo': 'bar',
                         'key': 'value',
                         'the answer': 42}}

# Write JSON file with indent
with io.open(file_path+"/dump_out.json", 'w', encoding='utf8') as outfile:
    str_ = json.dumps(data,
                      indent=4, sort_keys=True,
                      separators=(',', ': '), ensure_ascii=False)
    outfile.write(to_unicode(str_))

# Load JSON file
with open(file_path+"/dump_out.json") as data_file:
    data_loaded = json.load(data_file)





# ============ write and load sorted dict
data = {"name":1,
        "color":2,
        "parms":{"t":4,
                "r":10
                }
        }
with open(file_path+"/dump_out_sorted.json", 'w') as f:  
    json.dump(data, f,indent=4,sort_keys = True)

with open(file_path+"/dump_out_sorted.json") as data_file:
    data_loaded = json.load(data_file,encoding='utf-8',object_hook=_decode_dict)
print "load sorted dict",data_loaded,"\n"*2
#----------------------------------














# URL https://stackoverflow.com/questions/30152688/json-dumps-messes-up-order
# jsom dumps messes order 
d = collections.OrderedDict([(1, 10), (2, 20)])    
print "ordered_dict",d

json_format = json.dumps(d.items()) 
print "json_format ",json_format #order maintained

load_json =collections.OrderedDict(json.loads(json_format))  # Reading from JSON: works!
print "load_json ", load_json

a = '{"fields": {"name": "%s", "city": "%s", "status": "%s", "country": "%s" }}'
b = json.loads(a, object_pairs_hook=collections.OrderedDict)
# print json.dumps(b)
# print json.dumps(b, sort_keys=False)
with open(file_path+"/dump_out.json", 'w') as f:  
    json.dump(data, f,indent=4,sort_keys = True)
# ----------------------------------------





def loads_orderedDict():
    import json
    from collections import OrderedDict
    u = json.loads('{"a":1, "b":[]}', object_pairs_hook=OrderedDict)
    print u
    ordered_dict = OrderedDict([('a', 1), ('b', [])])
    json.dumps(u)

# Can I get JSON to load into an OrderedDict?
data = '{"foo":1, "bar": 2}' 
load_ordered = json.JSONDecoder(object_pairs_hook=collections.OrderedDict).decode(data)
print "ordered dict dumps", json.dumps(load_ordered,indent=4)

load_data = json.load(open(file_path+"/dump_out.json"), object_pairs_hook=collections.OrderedDict)
print "json.load = ",load_data




















# f = json.loads(file_path+"/dump_out.json", object_hook=_decode_dict)
# print f
# import io
# with io.open(file_path, 'w', encoding='utf-8') as f:
  # f.write(json.dumps(data, ensure_ascii=False))

# import codecs
# with open(file_path, 'wb') as f:
#     json.dump(data, codecs.getwriter('utf-8')(f),indent=4, ensure_ascii=False)








