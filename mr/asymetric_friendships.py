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
    # record: key/value pair of person (key) and friend (value)
    current_list=[]
    if friendlist_dict.has_key(record[0]):
      current_list=friendlist_dict[record[0]]
    current_list.append(record[1])
    friendlist_dict[record[0]] = current_list
    mr.emit_intermediate(record[0],record[1])

def reducer(key, list_of_values):
    is_symetric=0
    for friend in list_of_values:
      if friendlist_dict.has_key(friend):
        if key not in friendlist_dict[friend]:
          mr.emit((key,friend))
          mr.emit((friend,key))
      else:
        mr.emit((key,friend))
        mr.emit((friend,key))


# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
