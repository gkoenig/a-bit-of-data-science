import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # record: list of strings of two tables lineItems and order
    emitlist = []
    emitlist.append(str(record[0]))
    orderid = record[1]
    emitlist.append(str(orderid))
    for w in record[2:]:
        emitlist.append(str(w))
    mr.emit_intermediate(orderid, emitlist)
    
def reducer(key, list_of_values):
    orderlist=[]
    orderlist = list_of_values[0]
    for list_in_list in list_of_values[1:]:
        tmplist=[]
        tmplist.extend(orderlist)
        tmplist.extend(list_in_list)
        mr.emit((tmplist))
    

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
