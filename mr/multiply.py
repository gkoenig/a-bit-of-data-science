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
    A = {}
    B = {}
    matrix = str(record[0])
    row = record[1]
    col = record[2]
    val = record[3]
    #if matrix == "a":
    #    if A.has_key(row):
    #        columnlist = A[row]
    #    else
    #        columnlist = []
    #    columnlist[col] = val
    #    A[row] = columnlist
    #else:
    #    if B.has_key(row):
    #        columnlist = B[row]
    #    else
    #        columnlist = []
    #    columnlist[col] = val
    #    B[row] = columnlist
    for i in range(5):
        #print "%i,%i %s,%i,%i" % (row, i, matrix, col, val)
        mr.emit_intermediate((row,i),(matrix,col,val))
    print "MAPPER END: %s %i,%i" % (matrix,row,col)
    
def reducer(key, list_of_values):
    print "===== REDUCER START ======="
    print type(key), type(list_of_values)
    for list_in_list in list_of_values:
        mr.emit((list_in_list))
    
    

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
