import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    all_char_dict={}
    for key in record:
      for index in range(len(key)):
        count=0
        if not all_char_dict.has_key(key[index]):
          all_char_dict[key[index]] = key.count(key[index])
          count=all_char_dict[key[index]]
          mr.emit_intermediate(key[index], str(count))

def reducer(key, list_of_values):
    count=0
    for val in list_of_values:
      count+=int(val)
    mr.emit((key, str(count)))



# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
