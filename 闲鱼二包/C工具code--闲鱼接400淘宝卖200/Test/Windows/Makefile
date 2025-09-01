
all: gccTestData.exe gccTestMyString.exe gccTestUIO.exe clTestData.exe clTestMyString.exe clTestUIO.exe

## ------------------------------------ clear -------------------------------

clearExe: 
	del  gccTestData.exe gccTestMyString.exe gccTestUIO.exe clTestData.exe clTestMyString.exe clTestUIO.exe

clearO:
	del testMyString.o testData.o  testUIO.o myString.o data.o uio.o

clearObj:
	del testMyString.obj testData.obj  testUIO.obj myString.obj data.obj uio.obj

clearAll: clearObj clearExe clearO

clearGcc: 
	del data.o testData.o gccTestData.exe myString.o gccTestMyString.exe uio.o testUIO.o gccTestUIO.exe

clearCl: clearObj
	del clTestData.exe clTestMyString.exe clTestUIO.exe
	
## ------------------------------- gcc ---------------------------------------------

allgcc:  gccTestData.exe gccTestMyString.exe gccTestUIO.exe 

gccTestData.exe :   data.o testData.o
	gcc -o gccTestData.exe testData.o data.o 

data.o: ../../Utility/Data/data.c
	gcc -c ../../Utility/Data/data.c

testData.o: ../testData.c
	gcc -c ../testData.c

gccTestMyString.exe: testMyString.o  myString.o data.o 
	gcc -o gccTestMyString.exe testMyString.o  myString.o data.o 

testMyString.o: ../testMyString.c
	gcc -c ../testMyString.c

myString.o: ../../Utility/String/myString.c
	gcc -c ../../Utility/String/myString.c

gccTestUIO.exe: testUIO.o uio.o data.o myString.o
	gcc -o gccTestUIO.exe testUIO.o uio.o data.o myString.o

uio.o: ../../Utility/UIO/uio.c
	gcc -c ../../Utility/UIO/uio.c

testUIO.o: ../testUIO.c 
	gcc -c ../testUIO.c


# ------------------------ cl -------------------------
# On windows, us the vs commandline, so that the cl compiler can be used. 

allcl: clTestData.exe clTestMyString.exe clTestUIO.exe

clTestData.exe: data.obj testData.obj
	cl /FeclTestData.exe data.obj testData.obj

data.obj: ../../Utility/Data/data.c
	cl /c ../../Utility/Data/data.c

testData.obj: ../testData.c 
	cl /c ../testData.c

clTestMyString.exe: testMyString.obj  myString.obj data.obj 
	cl /FeclTestMyString.exe testMyString.obj  myString.obj data.obj 

testMyString.obj: ../testMyString.c
	cl /c ../testMyString.c

myString.obj: ../../Utility/String/myString.c
	cl /c ../../Utility/String/myString.c

clTestUIO.exe: testUIO.obj uio.obj data.obj myString.obj
	cl /FeclTestUIO.exe testUIO.obj uio.obj data.obj myString.obj

uio.obj: ../../Utility/UIO/uio.c
	cl /c ../../Utility/UIO/uio.c

testUIO.obj: ../testUIO.c 
	cl /c ../testUIO.c



# -------------------- Notes -------------------------

## can use the unix style to separate folders by /
## For example, gcc -c ../../Utility/Data/data.c   is ok 
## gcc -c ..\..\Utility\Data\data.c   is also ok
