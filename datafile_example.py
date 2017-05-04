import data_pb2
import pandas as pd
import numpy as np
import sys

def print_data(data_file):
  # print out header
  for header in data_file.header:
    first = True
    for column_name in header.column_name:
      if first:
        first = False
        sys.stdout.write(column_name)
      else:
        sys.stdout.write("," + column_name)
    sys.stdout.write("\n")

  #print out data
  for row in data_file.row:
    first = True
    for value in row.column_value:
      if first:
        first = False
        sys.stdout.write(str(value))
      else:
        sys.stdout.write("," + str(value))
    sys.stdout.write("\n")

'''
def make_df(data_file):
  columns = []
  for header in data_file.header:
    for column_name in header.column_name:
      columns.append(column_name);

  data = np.array([[]])
  for row in data_file.row:
    row_list = []
    for value in row.column_value:
      row_list.append(value)
    data = data.concatenate(data, row_list)
'''
data_file = data_pb2.DataFile()
f = open(sys.argv[1], "rb")
data_file.ParseFromString(f.read())
f.close()
print_data(data_file)
#make_df(data_file)
