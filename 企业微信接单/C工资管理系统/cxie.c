#include <stdio.h>  /*标准输入输出函数库*/
#include <stdlib.h>  /*标准函数库*/
#include <string.h>  /*字符串函数库*/

#define HEADER1 " -----------------------------------------------------------Employer------------------------------------------------------------- \n"
#define HEADER2 "|     number    |     name      |     salary    |     bonus     |   deduction   |    paysalary  |    taxes      |  realsalary   | \n"
#define HEADER3 "|---------------|---------------|---------------|---------------|---------------|---------------|---------------|---------------| \n"
#define FORMAT  "|%-15s|%-15s|%15.2f|%15.2f|%15.2f|%15.2f|%15.2f|%15.2f| \n"
#define DATA      per->num,per->name,per->salary,per->bonus,per->deduction,per->paysalary,per->taxes,per->realsalary
#define END     "---------------------------------------------------------------------------------------------------------------------------- ---- \n"
#define N 60
int saveflag = 0; /*是否需要存盘的标志变量*/
/*定义与职工有关的数据结构*/
typedef struct employee {    /*标记为employee*/
	char num[10];   /*职工编号*/
	char name[15];  /*职工姓名*/
	float salary;     /*基本工资*/
	float bonus;       /*奖金*/
	float deduction;       /*扣款*/
	float paysalary;     /*应发工资*/
	float taxes;       /*税款*/
	float realsalary;     /*实发工资*/
} Employer;

void menu() { /*主菜单*/
	system("clear");   /*清屏*/
	printf("                 The Employee' Salary Management System \n");
	printf("     *************************Menu********************************\n");
	printf("     *  1 input   record             2 delete record             *\n");
	printf("     *  3 search  record             4 modify record             *\n");
	printf("     *  5 insert  record             6 count  record             *\n");
	printf("     *  7 sort    reord              8 save   record             *\n");
	printf("     *  9 display record             0 quit   system             *\n");
	printf("     *************************************************************\n");
	/*printf()送格式化输出至文本窗口屏幕中*/
}

void printheader() { /*格式化输出表头*/
	printf(HEADER1);
	printf(HEADER2);
	printf(HEADER3);
}

void printdata(Employer* per) { /*格式化输出表中数据*/
	printf(FORMAT, DATA);
}

void disp(Employer eminfo[], int n) { /*显示数组eminfo[]中存储的记录，内容为employee结构中定义的内容*/
	printheader();
	for (int i = 0; i < n; i++) {
		printdata(&eminfo[i]);
	}
	printf(END);
}

void wrong() { /*输出按键错误信息*/
	printf("\n\n\n\n\n***********Error:input has wrong! press any key to continue**********\n");
	getchar();
}

void nofind() { /*输出未查找此职工的信息*/
	printf("\n=====>Not find this employee record!\n");
}

/*************************************************************
  作用：用于定位数组中符合要求的记录，并返回保存该记录的数组元素下标值
  参数：findmess[]保存要查找的具体内容; nameornum[]保存按什么在数组中查找;
 **************************************************************/
int locate(Employer eminfo[], int n, char findmess[], char nameornum[]) {
	for (int i = 0; i < n; i++) {
		if (strcmp(nameornum, "number") == 0 && strcmp(eminfo[i].num, findmess) == 0) {
			return i;
		} else if (strcmp(nameornum, "name") == 0 && strcmp(eminfo[i].name, findmess) == 0) {
			return i;
		}
	}
	return -1;
}

/*输入字符串，并进行长度验证(长度<lens)*/
void stringinput(char* t, int lens, char* notice) {
	char n[255];
	do {
		printf("%s", notice);  /*显示提示信息*/
		scanf("%s", n);  /*输入字符串*/
		if (strlen(n) > lens) printf("\n exceed the required length! \n"); /*进行长度校验，超过lens值重新输入*/
	} while (strlen(n) > lens);
	strcpy(t, n); /*将输入的字符串拷贝到字符串t中*/
}

/*输入数值，<＝数值)*/
float numberinput(char* notice) {
	float t = 0.00;
	do {
		printf("%s", notice);    /*显示提示信息*/
		scanf("%f", &t);  /*输入如工资等数值型的值*/
		if (t < 0) printf("\n score must >=0! \n"); /*进行数值校验*/
	} while (t < 0);
	return t;
}

/*增加职工工资记录*/
int add(Employer eminfo[], int n) {
	printf("Please enter the information of the employee:\n");
	stringinput(eminfo[n].num, 10, "Enter the employee number: ");
	stringinput(eminfo[n].name, 15, "Enter the employee name: ");
	eminfo[n].salary = numberinput("Enter the employee salary: ");
	eminfo[n].bonus = numberinput("Enter the employee bonus: ");
	eminfo[n].deduction = numberinput("Enter the employee deduction: ");
	eminfo[n].paysalary = eminfo[n].salary + eminfo[n].bonus - eminfo[n].deduction;
	eminfo[n].taxes = eminfo[n].paysalary * 0.1;
	eminfo[n].realsalary = eminfo[n].paysalary - eminfo[n].taxes;
	printf("Record added successfully!\n");
	return n + 1;
}

/*按职工编号或姓名，查询记录*/
void qur(Employer eminfo[], int n) {
	char findmess[255];
	char nameornum[10];
	printf("Please enter the search criteria (number or name): ");
	scanf("%s", nameornum);
	printf("Please enter the search keyword: ");
	scanf("%s", findmess);
	int index = locate(eminfo, n, findmess, nameornum);
	if (index != -1) {
		printheader();
		printdata(&eminfo[index]);
		printf(END);
	} else {
		nofind();
	}
}

/*删除记录：先找到保存该记录的数组元素的下标值，然后在数组中删除该数组元素*/
int del(Employer eminfo[], int n) {
	char findmess[255];
	char nameornum[10];
	printf("Please enter the search criteria (number or name): ");
	scanf("%s", nameornum);
	printf("Please enter the search keyword: ");
	scanf("%s", findmess);
	int index = locate(eminfo, n, findmess, nameornum);
	if (index != -1) {
		for (int i = index; i < n - 1; i++) {
			eminfo[i] = eminfo[i + 1];
		}
		printf("Record deleted successfully!\n");
		return n - 1;
	} else {
		nofind();
		return n;
	}
}

/*修改记录。先按输入的职工编号查询到该记录，然后提示用户修改编号之外的值，编号不能修改*/
void modify(Employer eminfo[], int n) {
	char findmess[255];
	printf("Please enter the employee number to modify: ");
	scanf("%s", findmess);
	int index = locate(eminfo, n, findmess, "number");
	if (index != -1) {
		printf("Please enter the new values for the following fields (or enter '-' to keep the original value):\n");
		stringinput(eminfo[index].name, 15, "Enter the new employee name: ");
		float salary = numberinput("Enter the new employee salary: ");
		eminfo[index].salary = salary != -1 ? salary : eminfo[index].salary;
		float bonus = numberinput("Enter the new employee bonus: ");
		eminfo[index].bonus = bonus != -1 ? bonus : eminfo[index].bonus;
		float deduction = numberinput("Enter the new employee deduction: ");
		eminfo[index].deduction = deduction != -1 ? deduction : eminfo[index].deduction;
		eminfo[index].paysalary = eminfo[index].salary + eminfo[index].bonus - eminfo[index].deduction;
		eminfo[index].taxes = eminfo[index].paysalary * 0.1;
		eminfo[index].realsalary = eminfo[index].paysalary - eminfo[index].taxes;
		printf("Record modified successfully!\n");
	} else {
		nofind();
	}
}

/*插入记录:按职工编号查询到要插入的数组元素的位置，然后在该编号之后插入一个新数组元素。*/
int insert(Employer eminfo[], int n) {
	char findmess[255];
	printf("Please enter the employee number to insert after: ");
	scanf("%s", findmess);
	int index = locate(eminfo, n, findmess, "number");
	if (index != -1) {
		printf("Please enter the information of the employee to insert:\n");
		stringinput(eminfo[n].num, 10, "Enter the employee number: ");
		stringinput(eminfo[n].name, 15, "Enter the employee name: ");
		eminfo[n].salary = numberinput("Enter the employee salary: ");
		eminfo[n].bonus = numberinput("Enter the employee bonus: ");
		eminfo[n].deduction = numberinput("Enter the employee deduction: ");
		eminfo[n].paysalary = eminfo[n].salary + eminfo[n].bonus - eminfo[n].deduction;
		eminfo[n].taxes = eminfo[n].paysalary * 0.1;
		eminfo[n].realsalary = eminfo[n].paysalary - eminfo[n].taxes;
		for (int i = n; i > index + 1; i--) {
			eminfo[i] = eminfo[i - 1];
		}
		printf("Record inserted successfully!\n");
		return n + 1;
	} else {
		nofind();
		return n;
	}
}

/*统计公司的员工的工资在各等级的人数*/
void sta(Employer eminfo[], int n) {
	int count[5] = { 0 };
	for (int i = 0; i < n; i++) {
		if (eminfo[i].realsalary < 1000) {
			count[0]++;
		} else if (eminfo[i].realsalary < 2000) {
			count[1]++;
		} else if (eminfo[i].realsalary < 3000) {
			count[2]++;
		} else if (eminfo[i].realsalary < 4000) {
			count[3]++;
		} else {
			count[4]++;
		}
	}
	printf("The number of employees in each salary level:\n");
	printf("Level 1 (<1000): %d\n", count[0]);
	printf("Level 2 (1000-1999): %d\n", count[1]);
	printf("Level 3 (2000-2999): %d\n", count[2]);
	printf("Level 4 (3000-3999): %d\n", count[3]);
	printf("Level 5 (>=4000): %d\n", count[4]);
}

/*利用冒泡排序法实现数组的按实发工资字段的降序排序，从高到低*/
void sort(Employer eminfo[], int n) {
	for (int i = 0; i < n - 1; i++) {
		for (int j = 0; j < n - i - 1; j++) {
			if (eminfo[j].realsalary < eminfo[j + 1].realsalary) {
				Employer temp = eminfo[j];
				eminfo[j] = eminfo[j + 1];
				eminfo[j + 1] = temp;
			}
		}
	}
	printf("Records sorted successfully!\n");
}

/*数据存盘,若用户没有专门进行此操作且对数据有修改，在退出系统时，会提示用户存盘*/
void save(Employer eminfo[], int n) {
	FILE* fp;
	fp = fopen("eminfo.txt", "w");
	if (fp == NULL) {
		printf("File open error!\n");
		return;
	}
	for (int i = 0; i < n; i++) {
		fprintf(fp, "%s %s %.2f %.2f %.2f %.2f %.2f %.2f\n", eminfo[i].num, eminfo[i].name, eminfo[i].salary, eminfo[i].bonus, eminfo[i].deduction, eminfo[i].paysalary, eminfo[i].taxes, eminfo[i].realsalary);
	}
	fclose(fp);
	printf("Records saved successfully!\n");
}

void load(Employer eminfo[], int* n) {
	FILE* fp;
	fp = fopen("eminfo.txt", "r");
	if (fp == NULL) {
		printf("File open error!\n");
		return;
	}
	*n = 0;
	while (fscanf(fp, "%s %s %f %f %f %f %f %f\n", eminfo[*n].num, eminfo[*n].name, &eminfo[*n].salary, &eminfo[*n].bonus, &eminfo[*n].deduction, &eminfo[*n].paysalary, &eminfo[*n].taxes, &eminfo[*n].realsalary) != EOF) {
		(*n)++;
	}
	fclose(fp);
	printf("Records loaded successfully!\n");
}

int main() {
	Employer eminfomation[N];         /*定义Employer结构体*/
	int select;         /*保存选择结果变量*/
	char ch;            /*保存(y,Y,n,N)*/
	int count = 0;        /*保存文件中的记录条数（或元素个数）*/

	load(eminfomation, &count);

	while (1) {
		menu();
		printf("Please enter your choice: ");
		scanf("%d", &select);
		getchar();
		switch (select) {
			case 1:
				count = add(eminfomation, count);
				break;
			case 2:
				count = del(eminfomation, count);
				break;
			case 3:
				qur(eminfomation, count);
				break;
			case 4:
				modify(eminfomation, count);
				break;
			case 5:
				count = insert(eminfomation, count);
				break;
			case 6:
				sta(eminfomation, count);
				break;
			case 7:
				sort(eminfomation, count);
				break;
			case 8:
				save(eminfomation, count);
				break;
			case 9:
				disp(eminfomation, count);
				break;
			case 0:
				printf("Do you want to save the changes? (Y/N): ");
				scanf("%c", &ch);
				if (ch == 'Y' || ch == 'y') {
					save(eminfomation, count);
				}
				return 0;
			default:
				wrong();
				break;
		}
	}
}
