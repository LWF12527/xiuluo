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

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "../Utility/Data/data.h"
// #include "..\..\Utility\Data\data.h"


// simply print a string, followed by a newline. 
// It is used to test the print_any_array() function. 
static void print_str(const void * str){
    printf("%s\n", (const char *) str);
}

int main(void)
{
    puts("........... testing clone()............");
    {
        double y = 5.5;
        double *yp = (double *)clone(&y, sizeof(double));
        printf("The clone of y, whose value is 5.5,  is:  %lf \n", *yp);
    }

    puts("........... testing clone_str()............");
    {
        char arr[100] = "hello\0abc\0123"; // too much wasted space after the first '\0'.
        char *cp = clone_str(arr);
        printf("The clone of arr = hello\\0abc\\0123\n");
        printf("is:  %s \n", cp);
    }

    puts("........... testing clone_chars_to_string(), clone_Chars(), make_Chars(), print_chars()............");
    {
        char arr1[] = "abcdef";
        char arr2[] = {'h', 'e', 'l', 'l', 'o'};
        Chars c1 = clone_Chars_to_string(arr1, sizeof arr1); // strlen(c1.addr) == 6.
        Chars c2 = clone_Chars_to_string(arr2, sizeof arr2); // strlen(c2.addr) == 6.
        Chars c3 = clone_Chars(arr1, sizeof arr1);
        Chars c4 = clone_Chars(arr2, sizeof arr2);
        Chars c5 = make_Chars(arr2, sizeof arr2);
        printf("arr1, a c-string,  is %s,  sizeof(arr1) is %lu \n", arr1, sizeof(arr1));
        printf("the clone arr1 to a c-string is: %s, its length is %d \n", c1.addr, c1.len);
        printf("arr2 is is a character sequence, whose length is  sizeof(arr2) is %lu \n", sizeof(arr2));
        printf(" The content of arr2, shown by print_chars() is: ");
        print_chars(arr2, sizeof arr2, TRUE);
        printf("\n the clone arr2 to a c-string is: %s, its length is %d \n", c2.addr, c2.len);
        printf("The clone of arr1, by clone_Chars(), has length: %d \n", c3.len);
        printf("print its content as regular characters  by print_chars() : ");
        print_chars(c3.addr, c3.len, TRUE);
        printf("\nThe clone of arr2, by clone_Chars(), has length: %d \n", c4.len);
        printf("print its elements as integers by print_Chars() : ");
        print_chars(c4.addr, c4.len, FALSE);
        puts("\n arr2 is wrapped as a Chars by make_Chars(). Now print the Chars");
        print_chars(c5.addr, c5.len, TRUE);
        puts("");
        free(c1.addr);
        free(c2.addr);
        free(c3.addr);
        free(c4.addr); 
        // No need to free the space of c5. 
    }

    puts("........... testing clone_data(), make_Data, make_empty_Data, and print_Data()............");
    {
        char arr[100] = "hello\0abc\0123";
        char *p = clone_str(arr);
        Data d = make_Data(p, strlen(p) + 1, STR);
        Data epd = make_empty_Data();
        int x = 9;
        double y = 99.9;
        char k = 'k';
        int *xp = &x;
        Data dx, dy, dk, dxp;
        puts("arr is an array initialized by \"hello\\0abc\\0123\" ");
        puts("after clone_str(arr) and making the clone a Data by calling make_Data ");
        printf("The Data has size %u  and typeid %u \n", d.size, d.typeid);
        printf("The content of the Data is : ");
        print_Data(d);
        puts("\nThe empty Data is printed as :  ");
        print_Data(epd);
        puts("");
        dx = make_Data(&x, sizeof(int), INT);
        dy = make_Data(&y, sizeof(double), DOUBLE);
        dk = make_Data(&k, sizeof k, CHAR);
        dxp = make_Data(&xp, sizeof xp, ADDR);
        printf("Printing Data for x = 9 : ");
        print_Data(dx);
        printf("\nPrinting Data for y = 99.9 : ");
        print_Data(dy);
        printf("\nPrinting Data for the pointer to x : ");
        print_Data(dxp);
        puts("");
        free(p);
    }

    puts("........... testing   print_any_array()............");
    {   
        char arr[5][80] = {"we are the world",
                           "bye bye Mr. american pie",
                           "hey joe",
                           "texas flood",
                           "purple rain"};
        puts("The content of an array of 5 c-strings is printed. Each c-string is printed in a line: ");
        print_any_array(arr, 5, 80, print_str);
    }

    puts("...........at last, testing malloc_safe()............");
    puts("The clone functions have successfully called of malloc_safe(). ");
    {
        malloc_safe(-5);
    }

    return 0;
}


