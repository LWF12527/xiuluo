#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_STUDENTS 100
#define MAX_NAME_LENGTH 50
#define MAX_ID_LENGTH 20
#define MAX_ADDRESS_LENGTH 100

struct Student {
	char id[MAX_ID_LENGTH];               // 学生ID
	char name[MAX_NAME_LENGTH];           // 学生姓名
	int age;                             // 学生年龄
	char gender;                         // 学生性别
	char address[MAX_ADDRESS_LENGTH];    // 学生地址
};

struct Student students[MAX_STUDENTS];   // 学生数组，用于存储学生信息
int numStudents = 0;                      // 学生数量

// 从文件中读取学生信息
void readStudentsFromFile(const char* filename) {
	FILE* file = fopen(filename, "r");
	if (file == NULL) {
		printf("Error: Failed to open file for reading.\n");
		return;
	}
	
	numStudents = 0;
	// 逐行读取文件内容，并将学生信息存储在数组中
	while (fscanf(file, "%s %s %d %c %[^\n]%*c", students[numStudents].id, students[numStudents].name,
		&students[numStudents].age, &students[numStudents].gender, students[numStudents].address) == 5) {
		numStudents++;
	}
	
	fclose(file);
}

// 将学生信息写入文件
void writeStudentsToFile(const char* filename) {
	FILE* file = fopen(filename, "w");
	if (file == NULL) {
		printf("Error: Failed to open file for writing.\n");
		return;
	}
	
	// 将学生信息逐行写入文件
	for (int i = 0; i < numStudents; i++) {
		fprintf(file, "%s %s %d %c %s\n", students[i].id, students[i].name, students[i].age,
			students[i].gender, students[i].address);
	}
	
	fclose(file);
}

// 添加学生信息
void addStudent() {
	if (numStudents == MAX_STUDENTS) {
		printf("Error: Maximum number of students reached.\n");
		return;
	}
	
	struct Student newStudent;
	printf("Enter student ID: ");
	scanf("%s", newStudent.id);
	
	// 检查学生是否已存在
	for (int i = 0; i < numStudents; i++) {
		if (strcmp(students[i].id, newStudent.id) == 0) {
			printf("Error: Student with ID %s already exists.\n", newStudent.id);
			return;
		}
	}
	
	printf("Enter student name: ");
	scanf("%s", newStudent.name);
	printf("Enter student age: ");
	scanf("%d", &newStudent.age);
	printf("Enter student gender (M/F): ");
	scanf(" %c", &newStudent.gender);
	printf("Enter student address: ");
	scanf(" %[^\n]%*c", newStudent.address);
	
	// 将新学生信息添加到数组中
	students[numStudents] = newStudent;
	numStudents++;
	
	printf("Student added successfully!\n");
}

// 显示学生信息
void displayStudent(const struct Student* student) {
	printf("ID: %s\n", student->id);
	printf("Name: %s\n", student->name);
	printf("Age: %d\n", student->age);
	printf("Gender: %c\n", student->gender);
	printf("Address: %s\n", student->address);
	printf("\n");
}

// 二分查找学生信息
int binarySearchById(const char* id) {
	int left = 0;
	int right = numStudents - 1;
	
	while (left <= right) {
		int mid = (left + right) / 2;
		int cmp = strcmp(students[mid].id, id);
		
		if (cmp == 0) {
			return mid;   // 找到学生，返回索引
		} else if (cmp < 0) {
			left = mid + 1;   // 目标值在右侧
		} else {
			right = mid - 1;   // 目标值在左侧
		}
	}
	
	return -1;   // 未找到学生
}

// 根据学生ID查找学生信息
void searchStudentById(const char* id) {
	int index = binarySearchById(id);
	if (index != -1) {
		displayStudent(&students[index]);
	} else {
		printf("No student found with ID %s.\n", id);
	}
}

// 根据学生姓名查找学生信息
void searchStudentByName(const char* name) {
	for (int i = 0; i < numStudents; i++) {
		if (strcmp(students[i].name, name) == 0) {
			displayStudent(&students[i]);
		}
	}
}

// 使用冒泡排序按寝室号对学生信息进行排序
void bubbleSortStudentsByDormNumber() {
	for (int i = 0; i < numStudents - 1; i++) {
		for (int j = 0; j < numStudents - i - 1; j++) {
			if (students[j].address[0] > students[j + 1].address[0]) {
				struct Student temp = students[j];
				students[j] = students[j + 1];
				students[j + 1] = temp;
			}
		}
	}
	
	printf("Students sorted by dorm number.\n");
	for (int i = 0; i < numStudents; i++) {
		displayStudent(&students[i]);
	}
}

// 菜单界面
void menu() {
	while (1) {
		printf("--------------\n");
		printf("Menu:\n");
		printf("1. Add student\n");
		printf("2. Save students to file\n");
		printf("3. Search student by ID\n");
		printf("4. Search student by name\n");
		printf("5. Sort students by dorm number\n");
		printf("6. Quit\n");
		printf("Enter your choice: ");
		
		int choice;
		scanf("%d", &choice);
		
		switch (choice) {
		case 1:
			addStudent();
			break;
		case 2:
			writeStudentsToFile("stu.txt");
			printf("Students saved to file.\n");
			break;
			case 3: {
				char id[MAX_ID_LENGTH];
				printf("Enter student ID: ");
				scanf("%s", id);
				searchStudentById(id);
				break;
			}
			case 4: {
				char name[MAX_NAME_LENGTH];
				printf("Enter student name: ");
				scanf("%s", name);
				searchStudentByName(name);
				break;
			}
		case 5:
			bubbleSortStudentsByDormNumber();
			break;
		case 6:
			return;
		default:
			printf("Invalid choice. Please try again.\n");
			break;
		}
		
		printf("\n");
	}
}

int main() {
	readStudentsFromFile("stu.txt");
	
	menu();
	
	return 0;
}
