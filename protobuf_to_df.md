

```python
import csv_pb2
import pandas as pd
import numpy as np
import sys
import ProtoText
```


```python
csv_file = csv_pb2.CSVFile()
f = open("output", "rb")
csv_file.ParseFromString(f.read())
f.close()
```


```python
columns = csv_file['header'][0]['column_name']
rows = np.array([row['column_value'] for row in csv_file['row']])
df = pd.DataFrame(rows, columns=columns)
```


```python
df
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>col1</th>
      <th>col2</th>
      <th>col3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0</td>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0</td>
      <td>2</td>
      <td>4</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0</td>
      <td>3</td>
      <td>6</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0</td>
      <td>4</td>
      <td>8</td>
    </tr>
    <tr>
      <th>5</th>
      <td>0</td>
      <td>5</td>
      <td>10</td>
    </tr>
    <tr>
      <th>6</th>
      <td>0</td>
      <td>6</td>
      <td>12</td>
    </tr>
    <tr>
      <th>7</th>
      <td>0</td>
      <td>7</td>
      <td>14</td>
    </tr>
    <tr>
      <th>8</th>
      <td>0</td>
      <td>8</td>
      <td>16</td>
    </tr>
    <tr>
      <th>9</th>
      <td>0</td>
      <td>9</td>
      <td>18</td>
    </tr>
    <tr>
      <th>10</th>
      <td>0</td>
      <td>10</td>
      <td>20</td>
    </tr>
    <tr>
      <th>11</th>
      <td>0</td>
      <td>11</td>
      <td>22</td>
    </tr>
    <tr>
      <th>12</th>
      <td>0</td>
      <td>12</td>
      <td>24</td>
    </tr>
    <tr>
      <th>13</th>
      <td>0</td>
      <td>13</td>
      <td>26</td>
    </tr>
    <tr>
      <th>14</th>
      <td>0</td>
      <td>14</td>
      <td>28</td>
    </tr>
    <tr>
      <th>15</th>
      <td>0</td>
      <td>15</td>
      <td>30</td>
    </tr>
    <tr>
      <th>16</th>
      <td>0</td>
      <td>16</td>
      <td>32</td>
    </tr>
    <tr>
      <th>17</th>
      <td>0</td>
      <td>17</td>
      <td>34</td>
    </tr>
    <tr>
      <th>18</th>
      <td>0</td>
      <td>18</td>
      <td>36</td>
    </tr>
    <tr>
      <th>19</th>
      <td>0</td>
      <td>19</td>
      <td>38</td>
    </tr>
  </tbody>
</table>
</div>




```python

```
