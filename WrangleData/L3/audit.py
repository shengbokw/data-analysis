#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
In this problem set you work with cities infobox data, audit it, come up with a
cleaning idea and then clean it up. In the first exercise we want you to audit
the datatypes that can be found in some particular fields in the dataset.
The possible types of values can be:
- NoneType if the value is a string "NULL" or an empty string ""
- list, if the value starts with "{"
- int, if the value can be cast to int
- float, if the value can be cast to float, but CANNOT be cast to int.
   For example, '3.23e+07' should be considered a float because it can be cast
   as float but int('3.23e+07') will throw a ValueError
- 'str', for all other values

The audit_file function should return a dictionary containing fieldnames and a 
SET of the types that can be found in the field. e.g.
{"field1": set([type(float()), type(int()), type(str())]),
 "field2": set([type(str())]),
  ....
}
The type() function returns a type object describing the argument given to the 
function. You can also use examples of objects to create type objects, e.g.
type(1.1) for a float: see the test function below for examples.

Note that the first three rows (after the header row) in the cities.csv file
are not actual data points. The contents of these rows should note be included
when processing data types. Be sure to include functionality in your code to
skip over or detect these rows.
"""
import codecs
import csv
import json
import pprint

CITIES = 'cities.csv'

FIELDS = ["name", "timeZone_label", "utcOffset", "homepage", "governmentType_label",
          "isPartOf_label", "areaCode", "populationTotal", "elevation",
          "maximumElevation", "minimumElevation", "populationDensity",
          "wgs84_pos#lat", "wgs84_pos#long", "areaLand", "areaMetro", "areaUrban"]
          
def isint(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

def isfloat(value):
    try:
        float(value)    
        return True
    except:
        return False

def datatype(data):
    if data == "NULL" or data == "":
        s = type(None)
    elif "{" in data:
        s =  type([])
    elif isint(data):
        s = type(1)
    elif isfloat(data):
        s = type(1.1)
    else:
        s = type(str())
    
    return s


def audit_file(filename, fields):
  fieldtypes = {}
  for i in range(len(FIELDS)):
      fieldtypes[FIELDS[i]] = []

  with open(filename, 'r') as f:
      reader = csv.reader(f)
      for line in reader:
          if reader.line_num == 1:
              header = line
          elif reader.line_num <= 4:
              continue
          else:
              for i in range(len(header)):
                  dataName = header[i]
                  if dataName in FIELDS:
                      fieldtypes[dataName].append(datatype(line[i]))
                      
  for i in range(len(FIELDS)):
      fieldtypes[FIELDS[i]] = set(fieldtypes[FIELDS[i]])

  return fieldtypes
    

def test():
    fieldtypes = audit_file(CITIES, FIELDS)

    pprint.pprint(fieldtypes)
    
    assert fieldtypes["name"] == set([type(str()), type([]), type(None)])
    
    assert fieldtypes["areaLand"] == set([type(1.1), type([]), type(None)])
    assert fieldtypes['areaMetro'] == set([type(1.1), type(None)])
    
if __name__ == "__main__":
    test()
