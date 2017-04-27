# protocol-buffers-example

To compile the proto file:  
`$ protoc -I=. --cpp_gout=. csv.proto`  

To compile the cpp files:  
`$ g++ -c -I$STOW_PKGS_GLOBAL_PREFIX/include -o csv_example.o csv_example.cpp`  
`$ g++ -c -I$STOW_PKGS_GLOBAL_PREFIX/include -o csv.pb.o csv.pb.cc`  
`$ g++ -L$STOW_PKGS_GLOBAL_PREFIX/lib -Wl,-rpath=$STOW_PKGS_GLOBAL_PREFIX/lib -lprotobuf -o csv_example csv_example.o csv.pb.o`  


