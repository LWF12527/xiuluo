#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#define MAX_STUDENTS 100
#define FILENAME "student_data.txt"

struct Student {
	char name[50];
	int id; 
	float grade1;
	float grade2;
	float grade3;
	float totalGrade;
};

struct Student students[MAX_STUDENTS];
int studentCount = 0;


void displayMenu();
void addStudent();
void deleteStudent();
void searchStudent();
void modifyStudent();
void insertStudent();
void sortByTotalGrade();
void statistics();
void showAllStudents();
void saveDataToFile();
void loadDataFromFile();
void clearScreen();

int main() {
	loadDataFromFile();  
	int choice;
	do {
		
		displayMenu();
		printf("请输入您的选择: ");
		scanf("%d", &choice);
		
		switch (choice) {
		case 1:
			clearScreen();
			addStudent();
			break;
		case 2:
			clearScreen();
			searchStudent();
			break;
		case 3:
			clearScreen();
			deleteStudent();
			break;
		case 4:
			clearScreen();
			modifyStudent();
			break;
		case 5:
			clearScreen();
			insertStudent();
			break;
		case 6:
			clearScreen();
			sortByTotalGrade();
			break;
		case 7:
			clearScreen();
			statistics();
			break;
		case 8:
			clearScreen();
			showAllStudents();
			break;
		case 0:
			saveDataToFile();  
			printf("感谢使用学生信息管理系统，再见！\n");
			break;
		default:
			printf("无效的选择，请重新输入。\n");
		}
		
	} while (choice != 0);
	return 0;
}

void displayMenu() {
	printf("\n===== 学生信息管理系统 =====\n");
	printf("1. 录入学生成绩信息\n");
	printf("2. 查找学生成绩信息\n");
	printf("3. 删除学生成绩信息\n");
	printf("4. 修改学生成绩信息\n");
	printf("5. 插入学生成绩信息\n");
	printf("6. 按总分排序\n");
	printf("7. 统计信息\n");
	printf("8. 显示所有学生信息\n");
	printf("0. 退出系统\n");
	printf("============================\n");
}
void addStudent() {
	if (studentCount >= MAX_STUDENTS) {
		printf("学生人数已达上限，无法继续添加。\n");
		return;
	}
	
	printf("请输入学生姓名: ");
	scanf("%s", students[studentCount].name);
	
	// 检查学号是否已存在
	int newId;
	int found = 0;
	do {
		printf("请输入学生学号: ");
		scanf("%d", &newId);
		
		found = 0;
		for (int i = 0; i < studentCount; i++) {
			if (students[i].id == newId) {
				found = 1;
				printf("该学号已存在，请重新输入。\n");
				break;
			}
		}
	} while (found);
	
	students[studentCount].id = newId;
	
	printf("请输入第一门课成绩: ");
	scanf("%f", &students[studentCount].grade1);
	printf("请输入第二门课成绩: ");
	scanf("%f", &students[studentCount].grade2);
	printf("请输入第三门课成绩: ");
	scanf("%f", &students[studentCount].grade3);
	
	students[studentCount].totalGrade = students[studentCount].grade1 +
	students[studentCount].grade2 +
	students[studentCount].grade3;
	
	studentCount++;
	
	printf("学生成绩信息录入成功！\n");
}

void deleteStudent() {
	int deleteId;
	printf("请输入要删除学生的学号: ");
	scanf("%d", &deleteId);
	
	int found = 0; 
	int i;
	int j;
	for (i = 0; i < studentCount; i++) {
		if (students[i].id == deleteId) {
			found = 1;
			for (j = i; j < studentCount - 1; j++) {
				students[j] = students[j + 1];
			}
			studentCount--;
			printf("学生成绩信息删除成功！\n");
			break;
		}
	}
	
	if (!found) {
		printf("未找到该学生成绩信息。\n");
	}
}

void searchStudent() {
	int searchId;
	printf("请输入要查找学生的学号: ");
	scanf("%d", &searchId);
	
	int found = 0;
	int i;
	for (i = 0; i < studentCount; i++) {
		if (students[i].id == searchId) {
			found = 1;
			printf("学生成绩信息：\n");
			printf("姓名: %s\n", students[i].name);
			printf("学号: %d\n", students[i].id);
			printf("第一门课成绩: %.2f\n", students[i].grade1);
			printf("第二门课成绩: %.2f\n", students[i].grade2);
			printf("第三门课成绩: %.2f\n", students[i].grade3);
			printf("总分: %.2f\n", students[i].totalGrade);
			break;
		}
	}
	
	if (!found) {
		printf("未找到该学生成绩信息。\n");
	}
}

void modifyStudent() {
	int modifyId;
	printf("请输入要修改学生成绩的学号: ");
	scanf("%d", &modifyId);
	
	int found = 0;
	int i;
	for (i = 0; i < studentCount; i++) {
		if (students[i].id == modifyId) {
			found = 1;
			printf("请输入修改后的第一门课成绩: ");
			scanf("%f", &students[i].grade1);
			printf("请输入修改后的第二门课成绩: ");
			scanf("%f", &students[i].grade2);
			printf("请输入修改后的第三门课成绩: ");
			scanf("%f", &students[i].grade3);
			
			students[i].totalGrade = students[i].grade1 +
			students[i].grade2 +
			students[i].grade3;
			
			printf("学生成绩信息修改成功！\n");
			break;
		}
	}
	
	if (!found) {
		printf("未找到该学生成绩信息。\n");
	}
}

void insertStudent() {
	if (studentCount >= MAX_STUDENTS) {
		printf("学生人数已达上限，无法插入。\n");
		return;
	}
	
	int position;
	printf("请输入要插入的位置(1-%d): ", studentCount + 1);
	scanf("%d", &position);
	
	if (position < 1 || position > studentCount + 1) {
		printf("无效的插入位置。\n");
		return;
	}
	
	printf("请输入学生姓名: ");
	scanf("%s", students[studentCount].name);
	printf("请输入学生学号: ");
	scanf("%d", &students[studentCount].id);
	printf("请输入第一门课成绩: ");
	scanf("%f", &students[studentCount].grade1);
	printf("请输入第二门课成绩: ");
	scanf("%f", &students[studentCount].grade2);
	printf("请输入第三门课成绩: ");
	scanf("%f", &students[studentCount].grade3);
	
	students[studentCount].totalGrade = students[studentCount].grade1 +
	students[studentCount].grade2 +
	students[studentCount].grade3;
	int i;
	for (i = studentCount; i > position - 1; i--) {
		students[i] = students[i - 1];
	}
	studentCount++;
	
	printf("学生成绩信息插入成功！\n");
}

void sortByTotalGrade() {
	
	int i;
	int j;
	for (i = 0; i < studentCount - 1; i++) {
		for (j = 0; j < studentCount - i - 1; j++) {
			float total1 = students[j].totalGrade;
			float total2 = students[j + 1].totalGrade;
			
			if (total1 < total2) {
				
				struct Student temp = students[j];
				students[j] = students[j + 1];
				students[j + 1] = temp;
			}
		}
	}
	
	printf("学生成绩信息按总分排序成功！\n");
}

void statistics() {
	printf("总学生数: %d\n", studentCount);
	
	int below60Count = 0;
	int i;
	for (i = 0; i < studentCount; i++) {
		if (students[i].grade1 < 60 || students[i].grade2 < 60 || students[i].grade3 < 60) {
			below60Count++;
		}
	}
	printf("每门课程小于60分的人数: %d\n", below60Count);
	
	float maxGrade1 = 0, maxGrade2 = 0, maxGrade3 = 0;
	for (i = 0; i < studentCount; i++) {
		if (students[i].grade1 > maxGrade1) {
			maxGrade1 = students[i].grade1;
		}
		if (students[i].grade2 > maxGrade2) {
			maxGrade2 = students[i].grade2;
		}
		if (students[i].grade3 > maxGrade3) {
			maxGrade3 = students[i].grade3;
		}
	}
	printf("第一门课程的最高分: %.2f\n", maxGrade1);
	printf("第二门课程的最高分: %.2f\n", maxGrade2);
	printf("第三门课程的最高分: %.2f\n", maxGrade3);
}

void showAllStudents() {
	printf("所有学生信息：\n");
	printf("%-5s%-15s%-8s%-8s%-8s%-8s\n", "学号", "姓名", "课程1", "课程2", "课程3", "总分");
	int i;
	for (i = 0; i < studentCount; i++) {
		printf("%-5d%-15s%-8.2f%-8.2f%-8.2f%-8.2f\n", students[i].id, students[i].name,
			students[i].grade1, students[i].grade2, students[i].grade3, students[i].totalGrade);
	}
}

void saveDataToFile() 
{
	FILE *file = fopen(FILENAME, "w");
	if (file == NULL) {
		printf("无法保存数据到文件。\n");
		return;
	}
	int i;
	for (i = 0; i < studentCount; i++) {
		fprintf(file, "%s %d %.2f %.2f %.2f %.2f\n",
			students[i].name, students[i].id,
			students[i].grade1, students[i].grade2,
			students[i].grade3, students[i].totalGrade);
	}
	
	fclose(file);
	printf("数据保存成功。\n");
}

void loadDataFromFile() {
	FILE *file = fopen(FILENAME, "r");
	if (file == NULL) {
		printf("无法从文件加载数据。\n");
		return;
	}
	
	while (fscanf(file, "%s %d %f %f %f %f",
		students[studentCount].name, &students[studentCount].id,
		&students[studentCount].grade1, &students[studentCount].grade2,
		&students[studentCount].grade3, &students[studentCount].totalGrade) == 6) {
		studentCount++;
	}
	
	fclose(file);
	printf("数据加载成功。\n");
}

void clearScreen() {
#ifdef _WIN32
	system("cls");
#else
	system("clear");
#endif
}

