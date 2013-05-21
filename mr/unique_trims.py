import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

friendlist_dict={}

def mapper(record):
    # record: key/value pair of sequence-id (key) and nucleotides (value)
    nucleotides=record[1]
    mr.emit_intermediate(nucleotides[:len(nucleotides[:-10])],"")

def reducer(key, list_of_values):
    mr.emit((key))


# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
