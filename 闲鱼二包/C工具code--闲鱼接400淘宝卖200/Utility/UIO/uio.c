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
#include <ctype.h>
#include "uio.h"
#include "../Data/data.h"
#include "../String/myString.h"

/* Given choiceStr as a string, ask the user to provide character that should appear in choiceStr.
 * Get the first character of user's input line, if the character does not appear in choiceStr, ask the user to input again. The input queue is always cleared after each input.
 For example, get_char_choice("apple") will return a user-provided character among a p l and e,
 */

/**
 * @brief Get Ask the user to input a character that is in a given c-string.
 *
 * @param choiceStr    A c-string
 * @return  Print a message asking user to type a character in the c-string. I.e., the first character in a line of user's input should appear in the c-string. If A user fails to do so, print out some error message, clear the input queue of stdin, and ask the user to do it  again. Repeat this until a wanted character is received. Return the character. The input queue of stdin is always empty after calling this function.
 * @note If choiceStr is empty, which is not a normal case, then print some warning message,  return the null ('\0') character.
 */
char get_char_choice(const char choiceStr[]) {
	/* !!! Provide the missing code.     <Task 22>   !!!*/
	char buff[100];
	int len;

	len = strlen(choiceStr);
	while (1) {
		printf(
				"Please choose a non-whitespace character that appears in:\n%s\n",
				choiceStr);

		char c;
		scanf("%s", buff);
		c = buff[0];

		for (int i = 0; i < len; i++) {
			if (choiceStr[i] == c) {
				return choiceStr[i];
			}
		}

		printf("Wrong choice: %c\n", c);
	}
}

/**
 * @brief Clear (remove) the characters in the input queue of stdin.
 *
 * @return  Remove each character in the queue of stdin, until the '\n' is removed. Return the number of characters removed from the input queue, also count the ending '\n'.
 * @note  Can be implemented by repeatedly calling the getchar() function.
 * @note If the queue of stdin is empty before calling this function, the program will pause.
 */
Uint clear_stdin_queue(void) {
	/* !!! Provide the missing code.     <Task 23>   !!!*/
	char c;
	int count = 0;

	while (1) {
		c = getchar();
		count++;
		if (c == '\n') {
			break;
		}
	}

	return count;
}

/**
 * @brief load the content of a file in a char sequence
 *
 * @param fp    A file stream that is opened already.
 * @return  If fp is NULL, return an empty Chars. Otherwise, a Chars is made, its space allocated on the Heap. Each byte of the file is copied as a character in the Chars. The Chars is fitting, whose number of characters is the same as in the file. Return the Chars.
 * @note If a '\0' character is obtained in the file stream, optionally, print some warning message and ignore this character, or exit the program.
 * @note no trailing '\0' is put at the end of the Chars.
 * @note Before calling this function, fp is be opened in some proper way.  This function does not close fp. Closing fp is the responsibility of the other part of the program.
 * @note <<hint>> If want to know the size of a file, do not use fseek(fp, 0, SEEK_END) and ftell(fp). Because this will not tell the file size correctly (proved by experiment). Instead, prepare some very large space, and read characters one by one from to file to the space, until EOF is read. Then possibly copy the content of the large space to some fitting clone.
 */
Chars load_file_to_Chars(FILE *fp) {
	/* !!! Provide the missing code.     <Task 24>   !!!*/
	Chars chars;
	chars.addr = NULL;
	chars.len = 0;

	if (!fp) {
		return chars;
	}

	int capacity = 1;
	char *addr = malloc(capacity);
	int len = 0;

	char c;
	while ((c = fgetc(fp)) != EOF) {
		if (c == 0) {
			printf("file contains \\0\n");
		} else {
			if (len >= capacity) {
				capacity += 1;
				addr = realloc(addr, capacity);
			}
			addr[len++] = c;
		}
	}

	if (len > 0) {
		chars.addr = addr;
		chars.len = len;
		return chars;
	} else {
		free(addr);
		return chars;
	}
}

/**
 * @brief Output the content of a character sequence into a file.
 *
 * @param cs    the starting address of a character sequence.
 * @param len   The number of characters of the character sequence.
 * @param fp   A file stream, which should be already be opened and ready for output.
 * @return Write the characters of cs one by one into the file fp, until all characters are written,
 * or something is wrong.  Return the number of characters written to the file.
 * @note writing a character to a file can b e done by calling putc().
 * @note https://cplusplus.com/reference/cstdio/putc/
 * @note the putc() function, which normally writes a character into to a file,  returns EOF if something is wrong.
 */
int save_chars_to_file(const char *cs, Uint len, FILE *fp) {
	/* !!! Provide the missing code.     <Task 25>   !!!*/
	int numWrites = 0;
	if (!cs) {
		return EOF;
	}

	for (Uint i = 0; i < len; i++) {
		if (EOF == fputc(cs[i], fp)) {
			return EOF;
		}
		numWrites++;
	}
	return numWrites;
}

/* Wait until the user hit enter. Print some hint message before user's input.
 * The input queue is cleared after calling this function. .  */

/**
 * @brief Pause the program until the user type the Enter key, or a line of text ended by Enter.
 * @note It should be called only when the input queue of STDIN is empty. Otherwise,
 *  it will not pause the program, just clear the input queue.
 * @note The queue of STDIN is always cleared after calling this function.
 */
void pause_for_enter(void) {
	/* !!! Provide the missing code.     <Task 26>   !!!*/
	char c;
	printf(":) To continue, hit the ENTER key\n");
	while (1) {
		c = getchar();

		if (c == '\n') {
			break;
		}
	}

}

