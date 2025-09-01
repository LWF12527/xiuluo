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

#include "../Utility/UIO/uio.h"
#include <stdio.h>
#include <stdlib.h>

static void test_get_char_choice();
static void test_clear_stdin_queue(void);
static void test_pause_for_enter(void);

/* !!! Provide the  prototype of the function   test_load_file_to_Chars()     <Task 27>     !!!*/
static void test_load_file_to_Chars(const char *filename, Chars *cs);
/* !!! Provide the  prototype of the function   test_save_chars_to_file()     <Task 28>     !!!*/
static void test_save_chars_to_file(const char *filename, Chars *cs);

int main(int argc, char *argv[]) {
	Chars cs; // to record the texts of a file.

	if (argc != 3) {
		printf("correct usage:  %s  inputFileName  outputFileName\n", argv[0]);
		puts("try again.");
		exit(1);
	}

	test_get_char_choice();
	test_clear_stdin_queue();
	test_pause_for_enter();
	test_load_file_to_Chars(argv[1], &cs);

	puts("\n:) Ready to output these text to the output file? ");
	pause_for_enter();

	test_save_chars_to_file(argv[2], &cs);

	puts("Now free the space of the Character sequence");
	free(cs.addr);
	puts("bye");
}

static void test_get_char_choice() {
	char ch = get_char_choice("Apple Store");
	printf("------------------ %s -----------------\n", __FUNCTION__);
	printf("The choice is : %c \n", ch);
}

static void test_clear_stdin_queue(void) {
	int x;
	char y;
	printf("------------------ %s -----------------\n", __FUNCTION__);
	puts("Please type a line : 123abc hahaha");
	if (scanf("%d", &x) == 1) {
		puts("now an integer is read from the input");
		printf("The integer is: %d\n", x);
	} else
		puts("Fail to read an integer !");
	//puts("now an integer is read from the input");
	//printf("The integer is: %d\n", x);
	puts("Now the function clear_stdin_queue() is called");
	clear_stdin_queue();
	puts("Now input a character X followed by [enter]");
	y = getchar();
	printf("The input character is %c. ", y);
	if (y == 'X' || y == 'x')
		puts("That is correct");
	else
		puts("Something is wrong!!!");
	getchar(); // remove the '\n' from queue.
}

static void test_pause_for_enter(void) {
	printf("------------------ %s --------------\n", __FUNCTION__);
	puts("Did you see the program paused for you to enter a line?\n"
			"If yes, it is fine. Otherwise, something is wrong !!!");
	pause_for_enter();

}

/* to display chinese at command line on Windows
 For utf-8 encoding, type the following command at command-line:
 chcp 65001
 For big-5 encoding, use
 chcp 936
 */

/* !!! Provide the missing code.     <Task 29>   !!!*/
///@note Remember to close any FILE that is opened in the function 
static void test_load_file_to_Chars(const char *filename, Chars *cs) {
	FILE *fp = fopen(filename, "r");
	*cs = load_file_to_Chars(fp);

	if ((*cs).len == 0) {
		printf("Failed to load file\n");
		return;
	}

	printf("Now the file is loaded. It has %d characters. Its content is:\n",
			(*cs).len);
	printf(".......begin of the file ......\n");
	for (Uint i = 0; i < (*cs).len; i++) {
		printf("%c", (*cs).addr[i]);
	}
	printf("......end of the file ........\n");
	fclose(fp);
}

/* !!! Provide the missing code.     <Task 30>   !!!*/
///@note Remember to close any FILE that is opened in the function 
static void test_save_chars_to_file(const char *filename, Chars *cs) {
	FILE *fp = fopen(filename, "w");
	int count = save_chars_to_file((*cs).addr, (*cs).len, fp);
	printf("Now the content is written into the file %s\nTotally %d characters are written to the file %s\n",
			filename, count, filename);
	printf("Open the file and check if it the same as the input file.\n");
	fclose(fp);
}
