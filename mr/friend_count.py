import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # record: key/value pair of person (key) and friend (value)
    mr.emit_intermediate(record[0],1)

def reducer(key, list_of_values):
    count=0
    for i in list_of_values:
        count+=i
    mr.emit((key,count))


# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
