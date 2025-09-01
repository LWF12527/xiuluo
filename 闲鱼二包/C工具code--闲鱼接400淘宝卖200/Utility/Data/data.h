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
data.h contains
- declarations of data types
- functions on storage, management of data.
    - conversion between different data types.
    - copy and clone of data.
    - allocation of space
*/

#ifndef _DATA_H_
#define _DATA_H_

/**
 * @brief a boolean type, with two symbolic constants FALSE and TRUE.
 */
typedef enum
{
  FALSE,
  TRUE
} Bool;

typedef unsigned int Uint;

/**
 * @brief   A  Character Sequence. It can be called simply CS.
 * @note    The difference between a c-string and Chars is that, in Chars, there is no need of the ending null character. A Chars is like an array of characters.
 * @note  A CS can be understood as the content of character array. It can be used to describe a piece of memory.
 */
typedef struct chars
{
  char *addr; // the address of the starting character in the sequence.
  Uint len;   // the number of characters in the character.
} Chars;

/// @brief Representing data of any general type. With three fields addr, size, and typeid.
/// @note addr: address of the data. Usually, the space should be allocated on the Heap. for c-string and a character sequence, addr is the address of the starting character.
/// @note   size: number of bytes of the data
/// @note   typeid:  A small integer, the unique id of the type of the Data.
typedef struct data
{
  void *addr;
  Uint size;
  char typeid;
} Data;

/**
 @brief  Some short names for built-in numeric types of C90. They are small integers that can be used as the typeid of a Data object.
 @note  "long long" and "long double" are not supported by C90. They are not considered here.
 @note  Other types can have an unique positive integer as its ID.
*/
typedef enum typeID
{
  ANY, /* any possible type  */
  CHAR,
  SHORT,
  INT,
  LONG,
  USHORT,
  UINT,
  ULONG,
  FLOAT,
  DOUBLE,
  ADDR, // a pointer, or address
  STR,  /* the c-string */
  CHARS /* Character sequence, may not contain a null character. */
} TypeID;

// typedef enum typeID TypeID;

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
void *clone(void *addr, Uint size);

/**
 @param s    the address of the first character of a character sequence.
 @param len    the number of characters in the character sequence.
 @return  Create a Chars, its space is allocated on the heap, with length len, and copy the all the content of s into the space of the Chars. Return the Chars
 @example
  //Given a c-string str, how to create a copy of str?
  Chars cs = chars_clone(str, strlen(str)+1);
*/
Chars clone_Chars(const char *s, Uint len);

/**
 * @brief  make a clone of a Data
 *
 * @param d    the source Data
 * @return A new Data struct, its space allocated on the Heap, a clone of d.
 */
Data clone_data(Data d);

/**
 @brief  Create a clone of a c-string without waste of space. The last character of the clone is the only null character in it.
 @param addr    The starting address of c-string
 @return A clone of the c-string at addr is made on the heap. The size of the clone is strlen(addr)+1. Return the  address of the first character of the clone.
 @note if addr is not for a c-string, i.e., a character array without ending null character, then the computation could be wrong or undefined.
 @example
 For example:
    char arr[100] = "hello\0abc\0123"; // too much wasted space after the first '\0'.
    char * cp = clone_str(arr);
    printf(cp); // print the clone of the string.
    // Some space of 6 characters recording the string "hello" is allocated on the Heap,
 */
char *clone_str(const char *addr);

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
Chars clone_Chars_to_string(const char *cs, Uint len);

/**
 * @brief  Create a Chars object using and address and a length
 *
 * @param addr    The address of the Chars
 * @param len     The number of characters in the Chars
 * @return A Chars structure is returned, simply using the parameters. No clone of the space at addr is made.
 */
Chars make_Chars(char *addr, Uint len);

/**
 * @brief    Create a Data object that contains an address addr and an unsigned integer
 *
 * @param addr    the addr field of the Data
 * @param size    the number of bytes of the Data
 * @param type    the unique id of the type of the data
 * @return A Data structure is returned, simply using the parameters. No clone of the space at addr is made.
 *  * @example
   // How to create a fit clone of a string and wrap the clone in a Data?
   char arr[100] = "hello\0abc\0123";
   char * p = clone_str(arr);
   Data d = make_Data(p, strlen(p)+1, STR);
 */
Data make_Data(void *addr, Uint size, char typeid);

/**
 * @brief   Create an empty Data object.
 *
 * @return  A empty Data object is returned. Its addr is NULL, size is 0, and typeid is ANY.
 */
Data make_empty_Data(void);

/**
 * @brief  Like malloc, allocate space of size bytes on the heap. The differences are that a. anything is wrong, quit the program; b. param is int, unlike the unsigned int parameter of malloc. It is a sensitive and alerting version of malloc. 
 *
 * @param size   Number of bytes to be allocated.
 * @return If size is 0 or negative, some error message is printed and exit the program.  If anything wrong ( malloc returns NULL), print some error message and exit the whole program. When there is no problem, return the address of the first byte of the allocated space on the heap. ( It calls malloc() or calloc() for space allocation). 
 * @note Comparing to malloc(), there is no need to worry if malloc_safe() can return NULL. As long as size is not 0, no need to check if the return value is NULL.
 * @note if the function is defined as:    void *malloc_safe(Uint size);   then malloc_safe(-5) will not have error messages. instead, 4294967291 byes will be allocated, causing a lot of confusion. 
 */
void * malloc_safe(int size);


// void qsort (void* base, size_t num, size_t size, int (*compar)(const void*,const void*))


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
void print_any_array(const void * arr, Uint elemNum, Uint elemSize, void (*printElem)(const void* ) );


/**
 * @brief
 *
 * @param s    The address of the first character in a CS.
 * @param len  The length (number of character) is the CS.
 * @param graph   A Bool value (TRUE or FALSE).
 * @return   The characters are printed one by one.  If graph is TRUE, then each character is printed in its visual form, i.e., using printf with %c; otherwise, each character is printed by its number value, i.e., using printf with %d.  Nothing is returned.
 * @note This function can be used to show the content of a piece of memory.
 * @note It is possible that when printing the elements in the CS, they can be separated by some way, like by a space or a comma, etc.
 */
void print_chars(const char *s, Uint len, Bool graph);

/**
 * @brief Print the content of a Data
 *
 * @param d   The Data object to be printed.
 * @note Different types of data are printed in some proper way according to its different typeid.
 */
void print_Data(Data d);

#endif
