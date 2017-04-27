# protocol-buffers-example

To compile the proto file:  
`$ protoc -I=. --cpp\_out=. csv.proto`  

To compile the cpp files:  
`$ g++ -c -I$STOW\_PKGS\_GLOBAL\_PREFIX/include -o csv\_example.o csv\_example.cpp`  
`$ g++ -c -I$STOW\_PKGS\_GLOBAL\_PREFIX/include -o csv.pb.o csv.pb.cc`  
`$ g++ -L$STOW\_PKGS\_GLOBAL\_PREFIX/lib -Wl,-rpath=$STOW\_PKGS\_GLOBAL\_PREFIX/lib -lprotobuf -o csv\_example csv\_example.o csv.pb.o`  


