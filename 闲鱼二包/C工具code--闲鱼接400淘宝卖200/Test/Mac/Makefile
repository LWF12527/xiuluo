all: testData.out testMyString.out testUIO.out

testData.out : data.o testData.o
	gcc -o testData.out data.o testData.o

data.o: ../../Utility/Data/data.c
	gcc -c ../../Utility/Data/data.c

testData.o: ../testData.c
	gcc -c ../testData.c



testMyString.out: testMyString.o  myString.o data.o 
	gcc -o testMyString.out testMyString.o  myString.o data.o 

testMyString.o: ../testMyString.c
	gcc -c ../testMyString.c

myString.o: ../../Utility/String/myString.c
	gcc -c ../../Utility/String/myString.c

testUIO.o: ../testUIO.c
	gcc -c ../testUIO.c

uio.o: ../../Utility/UIO/uio.c
	gcc -c ../../Utility/UIO/uio.c

testUIO.out: testUIO.o uio.o data.o myString.o
	gcc -o testUIO.out testUIO.o uio.o data.o myString.o

clear: 
	rm data.o testData.o testData.out myString.o testMyString.out uio.o testUIO.out

