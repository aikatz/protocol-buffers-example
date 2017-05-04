

```python
import csv_pb2
import pandas as pd
import numpy as np
import sys
```


```python
# Opens the binary file and parses it into the csv_file object
csv_file = csv_pb2.CSVFile()
f = open("output", "rb")
csv_file.ParseFromString(f.read())
f.close()
```


```python
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
```


```python
print_csv(csv_file)
```

    col1,col2,col3
    0,0,0
    0,1,2
    0,2,4
    0,3,6
    0,4,8
    0,5,10
    0,6,12
    0,7,14
    0,8,16
    0,9,18
    0,10,20
    0,11,22
    0,12,24
    0,13,26
    0,14,28
    0,15,30
    0,16,32
    0,17,34
    0,18,36
    0,19,38



```python
def make_df(csv_file):
    df = DataFrame()
```
