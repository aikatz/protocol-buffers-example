#include <iostream>
#include <fstream>
#include <string>
#include "datafile.pb.h"

int main() {
  GOOGLE_PROTOBUF_VERIFY_VERSION;
  datafile::DataFile data_file;

  // these could be input from user, etc.
  // they also don't need to be defined (i.e. you could have an unkown number of rows)
  int n_cols = 3;
  int n_rows = 20;
  std::string column_names[3] = {"col1", "col2", "col3"};

  // make the header (essentially a row of strings where each string is the name of a column)
  datafile::DataHeader* header = data_file.add_header();
  for(int i = 0; i < n_cols; i++) {
    header->add_column_name();
    header->set_column_name(i, column_names[i]);
  }

  // populate the rows with integers
  datafile::DataRow* row;
  for(int i = 0; i < n_rows; i++) {
    row = data_file.add_row();
    for(int j = 0; j < n_cols; j++) {
      row->add_column_value(i*j);
    }
  }

  // write the data to a file
  std::fstream output("output", std::ios::out | std::ios::trunc | std::ios::binary);
  if(!data_file.SerializeToOstream(&output)) {
    std::cerr << "Failed to write data file" << std::endl;
    return -1;
  }

  google::protobuf::ShutdownProtobufLibrary();
  return 0;
}
