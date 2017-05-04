import sys
from optparse import OptionParser

def parse_columns(option, opt_str, value, parser):
  parser.values.columns = value.split(',')

def parse_row_types(option, opt_str, value, parser):
  parser.values.row_types = value.split(',')

parser = OptionParser()
parser.add_option("--output_file", type=str, dest="output_file", help="output file")
parser.add_option("--columns", type=str, action="callback", dest="columns", callback=parse_columns)
parser.add_option("--row_types", type=str, action="callback", dest="row_types", callback=parse_row_types)

(options, args) = parser.parse_args()
f = open(options.output_file, "w")

# Make the DataFile object
template = '''message DataFile {
  repeated DataHeader header = 1;
  repeated DataRow row = 2;
}
'''
f.write(template)

template = ''

# make the DataHeader object
for i in range(len(options.columns)):
  template += "  string " + options.columns[i] + " = " + str(i+1) + ";\n"
template = "message DataHeader {\n " + template + "}\n"
f.write(template)

# make the DataRow object
for i in range(len(options.columns)):
  template += "  + options.columns[i] + " = " + str(i+1) + ";\n"
template = "message DataHeader {\n " + template + "}\n"
f.write(template)
