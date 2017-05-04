# protocol-buffers-example

To compile the .proto file for C++:  
`$ protoc -I=. --cpp_out=. datafile.proto`  

To compile the .proto file for Python:  
`$protoc -I=. --python_out=. datafile.proto`  

To compile the cpp files:  
`$ g++ -c -I$STOW_PKGS_GLOBAL_PREFIX/include -o datafile_example.o datafile_example.cpp`  
`$ g++ -c -I$STOW_PKGS_GLOBAL_PREFIX/include -o datafile.pb.o datafile.pb.cc`  
`$ g++ -L$STOW_PKGS_GLOBAL_PREFIX/lib -Wl,-rpath=$STOW_PKGS_GLOBAL_PREFIX/lib -lprotobuf -o datafile_example datafile_example.o datafile.pb.o`  


