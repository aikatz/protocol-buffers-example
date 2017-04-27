import csv_pb2
import sys

def print_csv(csv_file):
  # print out header
  for header in csv_file.header:
    first = True
    for column_name in header.column_name:
      if first:
        first = False
        sys.stdout.write(column_name)
      else:
        sys.stdout.write("," + column_name)
    sys.stdout.write("\n")

  #print out data
  for row in csv_file.row:
    first = True
    for value in row.column_value:
      if first:
        first = False
        sys.stdout.write(str(value))
      else:
        sys.stdout.write("," + str(value))
    sys.stdout.write("\n")


csv_file = csv_pb2.CSVFile()
f = open(sys.argv[1], "rb")
csv_file.ParseFromString(f.read())
f.close()
print_csv(csv_file)
