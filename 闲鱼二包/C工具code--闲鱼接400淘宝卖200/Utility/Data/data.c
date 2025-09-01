/***
 * !!! Provide your information please !!!
 * Student names and classes:
 *
 *
 *  // For example:  LI Bai (CS110-D2) ; DU Fu (EIE110-D3) ; LI Qingzhao (CS110-D3)
 */

/*******************************************************
 * C Programming  2022 Fall FIE MUST
 * Assignment Designed by instructor: Zhiyao Liang
 *******************************************************/

/*
 This file implements the functions declared in data.h
 */

#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include "data.h"

#define DEBUG 0

/* The clone functions always allocate a piece of memory on the Heap. The return type should be the same or close to the parameter type. */

/**
 * @brief make a clone on the Heap for a piece of memory
 *
 * @param addr    The starting address of a memory
 * @param size    The number of bytes of
 * @return void*, the address of the created clone
 * @note  It is possible that the function will quit the program if clone is not successful. It can call the the malloc_safe() function.
 * @note Hint: clone() can be implemented by the clone_chars() function declared in this file, or by the memcpy() function declared in <string.h>
 * @note  void * memcpy ( void * destination, const void * source, size_t num );
 * @note https://legacy.cplusplus.com/reference/cstring/memcpy/?kw=memcpy
 * @example
 // create a clone of a variable
 double y = 5.5;
 double *yp =  (double*) clone(&y, sizeof(y));
 // How to clone a constant 5.5? Assign it to a variable,
 // and clone the variable,   as show above.
 */
void* clone(void *addr, Uint size) {
	/* !!! Provide the missing code.     <Task 1>   !!!*/
	char *dest = malloc_safe(size);
	memcpy(dest, addr, size);
	return dest;
}

/**
 @param s    the address of the first character of a character sequence.
 @param len    the number of characters in the character sequence.
 @return  Create a Chars, its space is allocated on the heap, with length len, and copy the all the content of s into the space of the Chars. Return the Chars
 @example
 //Given a c-string str, how to create a copy of str?
 Chars cs = chars_clone(str, strlen(str)+1);
 */
Chars clone_Chars(const char *s, Uint len) {
	/* !!! Provide the missing code.     <Task 2>   !!!*/
	Chars chars;
	chars.addr = malloc_safe(len);
	chars.len = len;
	memcpy(chars.addr, s, len);
	return chars;
}

Data clone_data(Data d) {
	/* !!! Provide the missing code.     <Task 3>   !!!*/
	Data data;

	data.addr = clone(d.addr, d.size);
	data.size = d.size;
	data.typeid = d.typeid;
	return data;
}

char* clone_str(const char *addr) {
	/* !!! Provide the missing code.     <Task 4>   !!!*/
	Uint len = strlen(addr);
	char *dest = malloc_safe(len + 1);
	memcpy(dest, addr, len + 1);
	return dest;
}

/**
 * @brief  Make a clone of a Chars, and the content of the cloned Chars is a  c-string.
 *
 * @param cs    the address of the first character of some character sequence (CS) .
 * @param  len   the length of the CS
 * @return  A clone of the CS is made, whose space is on the Heap. If the last character of CS is '\0', then the length of the clone is the same as len. All content of the CS is copied to the clone, including the ending '\0'.
 Otherwise, the length of the clone is len+1, because the null character needs to be saved at the end of the clone.  The clone of CS is returned.
 * @example
 char arr1[] = "abcdef";
 char arr2[] = {'h','e','l','l','o'};
 Chars c1 = clone_chars_to_string(arr1, strlen(arr1)+1 ); // strlen(c1.addr) == 6.
 Chars c2 = clone_chars_to_string(arr2, 5); // strlen(c2.addr) == 6.
 */
Chars clone_Chars_to_string(const char *cs, Uint len) {
	/* !!! Provide the missing code.     <Task 5>   !!!*/
	Chars chars;
	if (cs[len] == 0) {
		chars.addr = malloc_safe(len + 1);
		memcpy(chars.addr, cs, len + 1);
		chars.len = strlen(chars.addr) + 1;
	} else {
		chars.addr = malloc_safe(len + 1);
		memcpy(chars.addr, cs, len + 1);
		chars.addr[len] = 0;
		chars.len = strlen(chars.addr) + 1;
	}

	return chars;
}

Chars make_Chars(char *addr, Uint len) {
	/* !!! Provide the missing code.     <Task 6>   !!!*/
	Chars chars;
	chars.addr = addr;
	chars.len = len;
	return chars;
}

Data make_Data(void *addr, Uint size, char id) {
	/* !!! Provide the missing code.     <Task 7>   !!!*/
	Data data;

	data.addr = addr;
	data.size = size;
	data.typeid = id;
	return data;
}
/**
 * @brief   Create an empty Data object.
 *
 * @return  A empty Data object is returned. Its addr is NULL, size is 0, and typeid is ANY.
 */
Data make_empty_Data(void) {
	/* !!! Provide the missing code.     <Task 8>   !!!*/
	Data data;

	data.addr = NULL;
	data.size = 0;
	data.typeid = ANY;
	return data;
}

void* malloc_safe(int size) {
	/* !!! Provide the missing code.     <Task 9>   !!!*/
	if (size <= 0) {
		printf("malloc_safe error: size is %d\n", size);
		exit(0);
	}

	void *p = malloc(size);
	if (!p) {
		printf("malloc_safe error: size is %d\n", size);
		exit(0);
	}

	return p;
}

/**
 * @brief   Print an array whose elements can be any type. Each element is printed by a function whose name is an argument.
 *
 * @param arr   The address of the first element of an array.
 * @param elemNum    The number of elements in the array.
 * @param elemSize    The size (number of bytes) of each element of the array.
 * @param printElem    A pointer to a function (represent a function name). Such a function accepts the address of an element of an array and print the element, and return nothing.
 * @note  The printElem should print something that can separate two elements.
 * @note   We can learn from the design of the general qsort function.
 * @note void qsort (void* base, size_t num, size_t size, int (*compar)(const void*,const void*));
 * @note https://cplusplus.com/reference/cstdlib/qsort/
 */
void print_any_array(const void *arr, Uint elemNum, Uint elemSize,
		void (*printElem)(const void*)) {
	/* !!! Provide the missing code.     <Task 10>   !!!*/

	for (Uint i = 0; i < elemNum; i++) {
		const void *p = arr + (i * elemSize);
		(*printElem)(p);
	}
}

/**
 * @brief
 *
 * @param s    The address of the first character in a CS.
 * @param len  The length (number of character) is the CS.
 * @param graph   A Bool value (TRUE or FALSE).
 * @return   The characters are printed one by one.  If graph is TRUE, then each character is printed in its visual form, i.e., using printf with %c; otherwise, each character is printed by its number value, i.e., using printf with %d.  Nothing is returned.
 * @note This function can be used to show the content of a piece of memory.
 * @note It is possible that when printing the elements in the CS,
 * they can be separated by some way, like by a space or a comma, etc.
 */
void print_chars(const char *s, Uint len, Bool graph) {
	/* !!! Provide the missing code.     <Task 11>   !!!*/
	for (Uint i = 0; i < len; i++) {
		if (graph == TRUE) {
			printf("%c", s[i]);
		} else {
			printf("%d ", s[i]);
		}
	}
}

/**
 * @brief Print the content of a Data
 *
 * @param d   The Data object to be printed.
 * @note Different types of data are printed in some proper way according to its different typeid.
 */
void print_Data(Data d) {
	/* !!! Provide the missing code.     <Task 12>   !!!*/
	/*
	 ANY,  any possible type
	 CHAR,
	 SHORT,
	 INT,
	 LONG,
	 USHORT,
	 UINT,
	 ULONG,
	 FLOAT,
	 DOUBLE,
	 ADDR,
	 STR,
	 CHARS
	 */

	if(d.size == 0){
		printf("Empty Data !!\n");
		return;
	}
	if (d.typeid == ANY) {
		print_chars(d.addr, d.size, FALSE);
	} else if (d.typeid == CHAR) {
		char *p = (char*) d.addr;
		printf("%c", *p);
	} else if (d.typeid == SHORT) {
		short *p = (short*) d.addr;
		printf("%d", *p);
	} else if (d.typeid == INT) {
		int *p = (int*) d.addr;
		printf("%d", *p);
	} else if (d.typeid == LONG) {
		long *p = (long*) d.addr;
		printf("%ld", *p);
	} else if (d.typeid == USHORT) {
		unsigned short *p = (unsigned short*) d.addr;
		printf("%u", *p);
	} else if (d.typeid == UINT) {
		unsigned int *p = (unsigned int*) d.addr;
		printf("%u", *p);
	} else if (d.typeid == ULONG) {
		unsigned long *p = (unsigned long*) d.addr;
		printf("%lu", *p);
	} else if (d.typeid == FLOAT) {
		float *p = (float*) d.addr;
		printf("%f", *p);
	} else if (d.typeid == DOUBLE) {
		double *p = (double*) d.addr;
		printf("%lf", *p);
	} else if (d.typeid == ADDR) {
		printf("%08lX", d.addr);
	} else if (d.typeid == STR) {
		printf("%s", d.addr);
	} else if (d.typeid == CHARS) {
		print_chars(d.addr, d.size, TRUE);
	}
}

