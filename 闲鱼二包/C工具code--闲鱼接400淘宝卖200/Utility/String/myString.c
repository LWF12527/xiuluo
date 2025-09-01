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

/***
 * Student names and classes:
 *
 *
 *  // For example:  LI Bai (CS110-D2) ; DU Fu (EIE110-D3) ; LI Qingzhao (CS110-D3)
 */

/*******************************************************
 * C Programming  2022 Fall FIE MUST
 * Assignment Designed by instructor: Zhiyao Liang
 *******************************************************/

#include "../Data/data.h" // not needed. For intellisense of vscode.
#include "myString.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

/**
 @param s1    address of the first character of a charater sequence.
 @param len1    length of s1
 @param s2    address of the first character of a charater sequence.
 @param len2    length of s2
 @return
 Compare the character sequence (CS) of s1 and s2 by dictionary order.
 Return
 -1 if the CS of s1 is smaller than the CS of s2;
 0 if the two CS' of s1 nad s2 are the same;
 1 if the CS of s1 is smaller than the CS of s2.
 @note   It is similar to strcmp()
 @note int strcmp ( const char * str1, const char * str2 );
 @note https://cplusplus.com/reference/cstring/strcmp/
 @note a special case:  a sequence of {'a', '\0'} is less than  {'a', '\0', '\0'},
 while by strcmp, they are the same.
 @example
 char arr1[3] = {'a', 'b', 'c'};
 char arr2[4] = "abc"; // ending character is '\0'
 char arr3[4] = {'a', 'b', 'x', 'y'};
 char arr4[] = {'a', 'b', 'c', '\0'};
 char arr5[] = {'a', 'b', 'c', '\0', '\0'};
 //This is an example of comparing a c-string and a Chars
 int r =  comp_chars(arr1, 3, arr2, 4 ) ; // r is -1.
 int s =  comp_chars(arr2, 3, arr4, 4 ) ; // s is -1
 int t =  comp_chars(arr4, 4, arr2, 4 ) ; // t is 0
 int u =  comp_chars(arr4, 4, arr5, 6 ) ; // u is -1
 */
int comp_chars(const char *s1, Uint len1, const char *s2, Uint len2) {
	/* !!! Provide the missing code.     <Task 13>   !!!*/
	Uint i = 0;
	Uint j = 0;
	while (i < len1 && j < len2) {
		char c1 = s1[i];
		char c2 = s2[j];
		if (c1 < c2) {
			return -1;
		} else if (c1 > c2) {
			return 1;
		}

		i++;
		j++;
	}

	if (len1 < len2) {
		return -1;
	} else if (len1 > len2) {
		return 1;
	} else {
		return 0;
	}
}

/**
 @brief Find the first character in a CS (Character Sequence) that satisfy some condition.
 @param s : an address of a sequence of characters
 @param len : the number of characters in the sequence s
 @param condition : a pointer to a function like isspace() declared in <ctype.h>. such a function accepts an int, and returns 0 if some condition is not satisfied, and 1 otherwise.
 @return return the address of the first (left-most) character in   s that satisfy the condition. If no such character exists (after the laster character is checked), return NULL.
 @note  condition can be like the isspace() function. The prototype of isspace() is :
 @note     int isspace(int ch)
 @note  https://en.cppreference.com/w/c/string/byte/isspace
 @example
 // to find the first non-white space character in string s:
 int isNoSpace(int c) {return !isspace(c);}
 int main(void){
 char * s = "    hello";
 // Since the last character of s is NULL, a non space, it is also ok:
 // char * p = addr_at_char_by_cond(s, strlen(s), isNoSpace);
 char * p = addr_at_char_by_cond(s, strlen(s)+1, isNoSpace);
 printf("The fist non-space character in s is %c \n", *p);
 return 0;
 }
 */
char* find_char_by_cond(const char *s, Uint len, int (*condition)(int)) {
	/* !!! Provide the missing code.     <Task 14>   !!!*/
	for (Uint i = 0; i < len; i++) {
		if ((*condition)(s[i])) {
			return (char*) (&s[i]);
		}
	}

	return NULL;
}

static int isNoSpace(int c) {
	return !(c == ' ' || c == '\t' || c == '\n' || c == '\r');
}

char* find_non_whitespace(const char *cs, Uint len) {
	/* !!! Provide the missing code.     <Task 15>   !!!*/
	return find_char_by_cond(cs, len, isNoSpace);
}

Chars find_word(const char *cs, Uint len) {
	/* !!! Provide the missing code.     <Task 16>   !!!*/
	Chars chars;
	chars.addr = NULL;
	chars.len = 0;

	char *p = find_non_whitespace(cs, len);
	if (p) {
		chars.addr = p;
		while (isNoSpace(*p) && *p != 0 && chars.len < len) {

			chars.len++;
			p++;
		}
	}
	return chars;
}

/**
 @brief Find the nth occurrence of a subsequence in a CS.  Searching direction is chosen by a parameter.
 @param s    the address of a sequence of characters
 @param sLen    the number of characters in the sequence s.
 @param subcs    the address of a sequence of characters, the subsequence .
 @param subcsLen    the number of characters in subs
 @param n    An integer.
 @param l2r    The boolean parameter. If it is TRUE, then the finding direction is from left-to-right. Otherwise, the direction is right-to-left.
 @return  Find the nth occurrence of subs in s.
 If l2r is TRUE, find it from left-to-right.  Otherwise, find it from right-to-left.
 If found, return the starting character's address of  of the nth occurrence of subs. Otherwise, if it is not found, then return NULL.
 If n is 0 or negative, the computation is not defined.
 @note  Special case 1:  if s is NULL or sLen is 0, return NULL.
 @note  Special case 2:  if subs is NULL or subsLen is 0, return NULL.
 @note  Special case 3: if n<=0, return NULL, because the computation is meaningless.
 @example
 // to find the 2nd occurrence of "abc" in "1abc2abc3abc"
 char *p = find_nth_subs("1abc2abc3abc", 10, "abc", 3, 2, TRUE); // return address of 'a' after '2'
 // find the last (right-most)  occurrence of "abc" in "1abc2abc3abc"
 char *q = find_nth_subs("1abc2abc3abc", 10, "abc", 3, 1, FALSE); // return address of 'a' after '3'
 */
char* find_nth_subcs(const char *s, Uint sLen, const char *subcs, Uint subcsLen,
		int n, Bool l2r) {
	/* !!! Provide the missing code.     <Task 17>   !!!*/
	if (s == NULL || sLen == 0) {
		return NULL;
	}
	if (subcs == NULL || subcsLen == 0) {
		return NULL;
	}
	if (n <= 0) {
		return NULL;
	}

	if (l2r == TRUE) {
		Uint i = 0;
		while (i < sLen) {
			int match = 0;
			for (int j = 0; j < subcsLen; j++) {
				int i2 = i + j;
				if (i2 < sLen && s[i2] == subcs[j]) {
					match++;
				}
			}

			if (match == subcsLen) {
				n--;
				if (n == 0) {
					return (char*) (&s[i]);
				}
			}

			i++;
		}
	} else {
		Uint i = sLen - 1;
		while (i >= 0) {
			int match = 0;
			for (int j = 0; j < subcsLen; j++) {
				int i2 = i - j;
				if (i2 < sLen && s[i2] == subcs[subcsLen - 1 - j]) {
					match++;
				}
			}

			if (match == subcsLen) {
				n--;
				if (n == 0) {
					return (char*) (&s[i - subcsLen + 1]);
				}
			}

			i--;
		}
	}

	return NULL;
}

/**
 @param cs    the address of the first character in some CS.
 @param len     the length of the CS.
 @param nump     a pointer to some int variable, which could be changed by calling this function.
 @return  Starting from cs, skip any proceed white space character, then read several consecutive non-space characters, that can form an int  (an optional sign of + or - is allowed).
 The integer is saved at the address nump. The return value is a Chars   which include the address of the first character of the the integer in the CS, and the number of characters appear in the integer (including the possible sign). If no integer appears at the beginning of the CS at addr (skipping starting spaces), then an empty Chars (with NULL address and 0 length) is returned.
 @note The starting character of an integer should be + - or a digit.  After the sign of + and - each character in the integer should be a digit.
 @note The library function sscanf() has similar usage.
 @note https://cplusplus.com/reference/cstdio/sscanf/
 @note int sscanf ( const char * s, const char * format, ...);
 @example
 For example:
 int x;
 Chars ca = (get_int("-5abc", &x)).addr ;
 // ca.addr is the address of a, and x become -5.
 Chars cb = (get_int(" abc123", &x));
 // cb.addr is NULL, and x does not change
 const char * str = "good  996haha";
 Chars r = get_int(&str[4], &x);
 // r.addr is the address of the h after 6, and x becomes 996
 */
Chars get_int(const char *cs, Uint len, int *nump) {
	/* !!! Provide the missing code.     <Task 18>   !!!*/
	Chars chars;
	chars.addr = NULL;
	chars.len = 0;

	int n = 0;
	int sign = 1;
	char *p = find_non_whitespace(cs, len);
	char *start = p;
	int digits = 0;
	if (p) {
		if (*p == '+') {
			p++;
			digits++;
		} else if (*p == '-') {
			p++;
			digits++;
			sign = -1;
		} else if (!(*p >= '0' && *p <= '9')) {
			return chars;
		}

		int pos = p - cs;

		while (pos < len) {
			if (!(*p >= '0' && *p <= '9')) {
				break;
			}

			digits++;
			n = n * 10 + (*p - '0');
			pos++;
			p++;
		}

		if (digits == 0) {
			return chars;
		}

		if (sign < 0) {
			n = -n;
		}
		*nump = n;

		chars.addr = start;
		chars.len = digits;
		return chars;
	}
	return chars;
}

/**
 @param cs    the address of the first character of a character sequence.
 @param len    the number of characters in the character sequence.
 @return    In the space of s, reverse the character sequence. I.e.  abc becomes cba.
 nothing is returned.
 @example
 // Given a c-string str, reverse it in its space:
 reverse_chars_in_place(cs.addr, cs.len-1) ;
 // create a reverse clone of str:
 Chars cs = clone_chars(str, strlen(str)+1)
 reverse_chars_in_place(cs.addr, cs.len-1);
 */
void reverse_chars_in_place(char *cs, Uint len) {
	/* !!! Provide the missing code.     <Task 19>   !!!*/
	if (!cs || len <= 1) {
		return;
	}

	for (Uint i = 0; i < len / 2; i++) {
		Uint j = len - 1 - i;

		char t = cs[i];
		cs[i] = cs[j];
		cs[j] = t;
	}
}

/**
 * @brief  find the first character after the first sub-CS in a CS.
 *
 * @param cs  The address of the first character of a CS.
 * @param csLen  the length of CS of cs
 * @param substr  The address of the first character of a sub-CS
 * @param subcsLen  The length of the CS of subcs
 * @return  if the subCS is not found in the CS, or it is found but no character appear in CS after the subCS
 * (the last character of subCS is the last on of CS), return NULL; Otherwise, return the first character in CS after the first subCS.
 */
char* skip_subcs(const char *cs, Uint csLen, const char *subcs, Uint subcsLen) {
	/* !!! Provide the missing code.     <Task 20>   !!!*/
	if (cs == NULL || csLen == 0) {
		return NULL;
	}
	if (subcs == NULL || subcsLen == 0) {
		return (char*) (&cs[0]);
	}

	Uint i = 0;
	while (i < csLen) {
		int match = 0;
		for (int j = 0; j < subcsLen; j++) {
			int i2 = i + j;
			if (i2 < csLen && cs[i2] == subcs[j]) {
				match++;
			}
		}

		if (match == subcsLen) {
			int i2 = i + subcsLen - 1;
			if (i2 < csLen - 1) {
				return (char*) (&cs[i2 + 1]);
			} else {
				return NULL;
			}
		}

		i++;
	}
	return NULL;
}

// also ok
// void sort_Chars(Chars arr [], Uint arrLen, int (* compChars)(const char *s1, Uint len1, const char *s2, Uint len2))

void sort_Chars(Chars arr[], Uint arrLen,
		int (*compChars)(const char*, Uint, const char*, Uint)) {
	/* !!! Provide the missing code.     <Task 21>   !!!*/

	for (int i = 0; i < arrLen - 1; i++) {
		for (int j = 0; j < arrLen - 1 - i; j++) {
			int cmp = (*compChars)(arr[j].addr, arr[j].len, arr[j + 1].addr,
					arr[j + 1].len);
			if (cmp > 0) {
				Chars t = arr[j];
				arr[j] = arr[j + 1];
				arr[j + 1] = t;
			}
		}
	}
}

