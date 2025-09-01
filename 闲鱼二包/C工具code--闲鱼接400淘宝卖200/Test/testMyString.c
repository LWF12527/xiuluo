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
#include <ctype.h>
#include <string.h> 
//#include "../Utility/Data/data.h"
#include "../Utility/String/myString.h" 


/**
 * @brief To judge if a character is a whitespace or not.
 * 
 * @param c    an int, normally a character
 * @return      return 1 if is not a white space character, otherwise, return 0. 
  I.e., simply return !(isspace(c))
  @note  The prototype of isspace() is : 
  @note int isspace(int ch);
  @note https://en.cppreference.com/w/c/string/byte/isspace
  @note This function is very simple. Another way is to put the definition in this .h, and make the definition a static one. 
 */
static int is_no_space(int c); 

static int is_no_space(int c){
    return !isspace(c); 
}

void test_sort_Chars(void);

int main(void){
    puts("............. test  comp_chars() ..............");
    {
    char arr1[3] = {'a', 'b', 'c'};
    char arr2[4] = "abc"; // ending character is '\0'
    char arr3[4] = {'a', 'b', 'x', 'y'};
    char arr4[] = {'a', 'b', 'c', '\0'};
    char arr5[] = {'a', 'b', 'c', '\0', '\0'};
    puts("arr1 is an array of 3 chars : a b c ");
    puts("arr2 is a c-string \"abc\" ");
    puts("arr3 is an array of four chars: a b x y ");  
    puts("arr4 is an array of 4 chars:  a b c \\0");
    puts("arr5 is an array of 5 chars: a b c \\0 \\0");
    printf(" chars_comp(arr1, 3, arr2, 4 ) = %d \n", comp_chars(arr1, 3, arr2, 4 ));
    printf(" chars_comp(arr2, 3, arr2, 4 ) = %d \n", comp_chars(arr2, 3, arr2, 4 ));
    printf(" chars_comp(arr4, 4, arr2, 4 ) = %d \n", comp_chars(arr4, 4, arr2, 4 ));
    printf(" chars_comp(arr4, 4, arr5, 6 ) = %d \n", comp_chars(arr4, 4, arr5, 6 ));
    }

    puts("..............test  find_char_by_cond() , and, find_non_whitespace()........... "); 
    {
        char arr[] = "  \t \r \n  ab ccd xy ";
        //char * arr2 = "    "; // c-string of 4 spaces 
        char * chp; 
        puts("arr is a c-string:  \"  \t \r \n  ab ccd xy \"");
        chp = find_char_by_cond(arr, strlen(arr), is_no_space);
        puts(" at the address returned by:   find_char_by_cond(arr, strlen(arr), is_no_space)");
        printf(" which has index  %ld\n",  chp - arr);
        printf("the character is  %c\n", *chp);
        puts(" at the address returned by:   find_non_whitespace(arr, strlen(arr)+1 )");
        chp = find_non_whitespace(arr, strlen(arr)+1 );
        printf(" which has index  %ld\n",  chp - arr);
        printf("the character is  %c\n", *chp);
        puts("arr2 is a c-string of 4 spaces,");
        puts(" the address returned by:   find_non_whitespace(\"    \", 4 )");
        chp = find_non_whitespace("    ", 4);
        if(chp == NULL )
            printf(" is %p \n",  chp);
        else 
            printf("it is at the index %ld\n", chp-"    ");
        puts(" the address returned by:   find_non_whitespace(\"    \", 5 )");
        chp = find_non_whitespace("    ", 5);
        if(chp == NULL )
            printf(" is %p \n",  chp);
        else 
            printf("it is at the index %ld with char value %d \n", chp - "    ", *chp);
    }

    puts("..............test  find_word()........... "); 
    {
        char arr1[] = "   abc  123  56x  ";
        char arr2[] = " \t \r \n  ";
        Chars r1, r2; 
        puts("arr1 is a c-string  \"   abc  123  56x  \" ");
        puts("arr2 is a c-string \" \\t \\r \\n  \" ");
        r1 = find_word(arr1, strlen(arr1)+1);
        r2 = find_word(arr2, strlen(arr2)+1);
        printf("For The word found by find_word(arr1, strlen(arr1)+1, TRUE), its number of characters is %d \n", r1.len);
        printf("The word is: ");
        print_chars(r1.addr, r1.len, TRUE);
        puts("");
        printf("For The word found by find_word(arr2, strlen(arr2)+1, TRUE), its number of characters is %d \n", r2.len);
        printf("The word is: ");
        print_chars(r2.addr, r2.len, TRUE);
        puts("");
    }

    puts("..............test  find_nth_subcs()........... "); 
    {
        char arr[] = " xx 1abc yy 2abc zz 3abc 4abc haha";
        char *c1 = find_nth_subcs(arr, sizeof arr, "abc", strlen("abc"), 3, TRUE);
        char *c2 = find_nth_subcs(arr, sizeof arr, "abc", strlen("abc"), 2, FALSE);
        char *c3 = find_nth_subcs(arr, sizeof arr, "abc", strlen("abc"), 5, TRUE);
        char *c4 = find_nth_subcs(arr, sizeof arr, "abc", strlen("abc"), 4, FALSE);
        puts("arr is a c-string: \" xx 1abc yy 2abc zz 3abc 4abc haha\" ");
        printf(" The 3th abc, from left to right, ");
        (c1!=NULL) ? 
            printf(" is found, after the character %c \n", *(c1-1))
            :
            printf(" not found \n");
        printf(" The 2th abc, from right to left, ");
        (c2!=NULL) ? 
            printf(" is found, after the character %c \n", *(c2-1))
            :
            printf(" not found \n");
        printf(" The 5th abc, from left to right, ");
        (c3!=NULL) ? 
            printf(" is found, after the character %c \n", *(c3-1))
            :
            printf(" not found \n");
        printf(" The 4th abc, from right to left, ");
        (c4!=NULL) ? 
            printf(" is found, after the character %c \n", *(c4-1))
            :
            printf(" not found \n");
    }
    
    puts("..............test  get_int()........... "); 
    {
        int x, y, z;
        Chars ca, cb, r; 
        const char * str = "good  996haha"; 
        x = y = z = 0; 
        puts(" x and y, and z are all 0"); 
        ca = get_int("-5abc", 6, &x);
        puts(" after:  ca = get_int(\"-5abc\", 6, &x) ");
        printf(" x is %d, the char at ca.addr is %c, ca.len = %u \n", x, *ca.addr, ca.len );
        cb = get_int(" abc123", 7, &y);
        puts(" after: cb = (get_int(\" abc123\", &y)) ");
        if(cb.addr != NULL)
            printf(" y is %d, the char at cb.addr is %c, cb.len = %u \n", y, *cb.addr, cb.len );
        else 
            puts(" no integer is found");
        r = get_int(str+4, strlen(str)-4, &z);
        puts("str is \"good  996haha\" ");
        printf("after: r = get_int(str+4, strlen(str)-4, &z) \n"); 
        r = get_int(str+4, strlen(str)-4, &z);
        if(r.addr == NULL)
            puts("no integer is found");
        else
            printf(" z is %d, the char at r.addr is %c, r.len = %u \n", z, *r.addr, r.len );

    }

     puts("..............test  reverse_chars_in_place()........... "); 
     {
        char arr[] = "123456789abcdef";
        puts("arr is \"123456789abcdef\"");
        puts(" after calling  reverse_chars_in_place(arr, strlen(arr))");
        reverse_chars_in_place(arr, strlen(arr));
        printf(" arr is  %s \n", arr);
     }

    puts("..............test  skip_subcs()........... ");
    {
        char arr[] = "<name>Alice</name>";
        char * a = skip_subcs(arr, sizeof(arr), "<name>", strlen("<name>"));
        char * b; 
        puts("arr is  \"<name>Alice</name>\" ");
        puts("after calling:  a = skip_subcs(arr, sizeof(arr), \"<name>\", strlen(\"<name>\")");
        if(a==NULL)
            puts("a is NULL");
        else
            printf("The character at a is %c \n", *a);
        puts("after calling:  b = skip_subcs(arr, sizeof(arr), \"</name>\", sizeof(\"</name>\")");
        b = skip_subcs(arr, sizeof(arr), "</name>", sizeof("</name>"));
        if(b==NULL)
            puts("b is NULL");
        else
            printf("The character at a is %c \n", *b);
    }

    test_sort_Chars();

    return 0; 
}


//simply compare the len of Chars.
static int comp_chars_by_len(const char *s1, Uint len1, const char *s2, Uint len2){
    if (len1 == len2)
        return 0;
    else if(len1 < len2)
        return -1;
    else 
        return +1;
}

static void print_chars_line(const void * p){
    Chars cs = *((Chars *) p);
    print_chars(cs.addr, cs.len, TRUE);
    printf("\n");
}

void test_sort_Chars(void){
    puts("..............test  sort_Char()........... ");
    {
        char arr[5][80] = { "long long time ago", 
                        "bye bye Mr. american pie",
                        "midnight, with the stars and you", 
                        "our dreams are young and we both know",
                        "here we are, here we are alone"
                        } ;
        Chars csArr[5];
        int j; 
        for(j=0; j<5; j++)
            csArr[j] = make_Chars(arr[j], strlen(arr[j]));
        puts("The 5 Chars in an array csArr are:");
        for(j=0; j<5; j++){
            print_chars(csArr[j].addr, csArr[j].len, TRUE);
            puts("");
        }
        sort_Chars(csArr, 5, comp_chars);
        puts("\nAfter calling: sort_Chars(csArr, 5, comp_chars)  ");
        puts("The array csArr becomes:\n");
        for(j=0; j<5; j++){
            print_chars(csArr[j].addr, csArr[j].len, TRUE);
            puts("");
        }

        // do not mention static in the declaration. This is how to refer global static names. 
        // Maybe names of external linkage can only be referred at some global position. 
        sort_Chars(csArr, 5, comp_chars_by_len);
        puts("\nAfter calling  sort_Chars(csArr, 5, comp_chars_by_len), the array becomes: ");
        //print_any_array(arr, 5, 80, print_str);
        print_any_array(csArr, 5, sizeof(Chars), print_chars_line);
        /*
         for(j=0; j<5; j++){
            print_chars(csArr[j].addr, csArr[j].len, TRUE);
            puts("");
        }
        */

    }

}

