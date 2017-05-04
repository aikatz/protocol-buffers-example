CC=g++
INC=$(STOW_PKGS_GLOBAL_PREFIX)/include
LIB=$(STOW_PKGS_GLOBAL_PREFIX)/lib
CFLAGS= -c -I$(INC)
LDFLAGS=-L$(LIB) -Wl,-rpath=$(LIB) -lprotobuf
OBJECTS=datafile_example.o csv.pb.o
EXECUTABLE=datafile_example

all: $(EXECUTABLE)

$(EXECUTABLE): $(OBJECTS)
	$(CC) $(LDFLAGS) $(OBJECTS) -o $@

.c*.o:
	$(CC) $(CFLAGS) $< -o $@

clean:
	rm *.o $(EXECUTABLE)
