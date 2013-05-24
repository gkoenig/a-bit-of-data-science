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

    for i in range(5):
        if matrix == "a":
          mr.emit_intermediate((row,i),(matrix,col,val))
        else:
          mr.emit_intermediate((i,col),(matrix,row,val))

def reducer(key, list_of_values):
    A=[0]*5
    B=[0]*5
    sum=0
    for list_in_list in list_of_values:
      index = int(list_in_list[1])
      value = int(list_in_list[2])
      if list_in_list[0] == "a":
        A[index]=value
      else:
        B[index]=value
    for i in range(0, len(A)):
      sum += int(A[i])*int(B[i])

    tup = ( key[0], key[1], sum)
    mr.emit(tup)



# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
