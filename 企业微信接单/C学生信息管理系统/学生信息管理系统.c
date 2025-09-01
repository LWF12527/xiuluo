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
		printf("����������ѡ��: ");
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
			printf("��лʹ��ѧ����Ϣ����ϵͳ���ټ���\n");
			break;
		default:
			printf("��Ч��ѡ�����������롣\n");
		}
		
	} while (choice != 0);
	return 0;
}

void displayMenu() {
	printf("\n===== ѧ����Ϣ����ϵͳ =====\n");
	printf("1. ¼��ѧ���ɼ���Ϣ\n");
	printf("2. ����ѧ���ɼ���Ϣ\n");
	printf("3. ɾ��ѧ���ɼ���Ϣ\n");
	printf("4. �޸�ѧ���ɼ���Ϣ\n");
	printf("5. ����ѧ���ɼ���Ϣ\n");
	printf("6. ���ܷ�����\n");
	printf("7. ͳ����Ϣ\n");
	printf("8. ��ʾ����ѧ����Ϣ\n");
	printf("0. �˳�ϵͳ\n");
	printf("============================\n");
}
void addStudent() {
	if (studentCount >= MAX_STUDENTS) {
		printf("ѧ�������Ѵ����ޣ��޷�������ӡ�\n");
		return;
	}
	
	printf("������ѧ������: ");
	scanf("%s", students[studentCount].name);
	
	// ���ѧ���Ƿ��Ѵ���
	int newId;
	int found = 0;
	do {
		printf("������ѧ��ѧ��: ");
		scanf("%d", &newId);
		
		found = 0;
		for (int i = 0; i < studentCount; i++) {
			if (students[i].id == newId) {
				found = 1;
				printf("��ѧ���Ѵ��ڣ����������롣\n");
				break;
			}
		}
	} while (found);
	
	students[studentCount].id = newId;
	
	printf("�������һ�ſγɼ�: ");
	scanf("%f", &students[studentCount].grade1);
	printf("������ڶ��ſγɼ�: ");
	scanf("%f", &students[studentCount].grade2);
	printf("����������ſγɼ�: ");
	scanf("%f", &students[studentCount].grade3);
	
	students[studentCount].totalGrade = students[studentCount].grade1 +
	students[studentCount].grade2 +
	students[studentCount].grade3;
	
	studentCount++;
	
	printf("ѧ���ɼ���Ϣ¼��ɹ���\n");
}

void deleteStudent() {
	int deleteId;
	printf("������Ҫɾ��ѧ����ѧ��: ");
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
			printf("ѧ���ɼ���Ϣɾ���ɹ���\n");
			break;
		}
	}
	
	if (!found) {
		printf("δ�ҵ���ѧ���ɼ���Ϣ��\n");
	}
}

void searchStudent() {
	int searchId;
	printf("������Ҫ����ѧ����ѧ��: ");
	scanf("%d", &searchId);
	
	int found = 0;
	int i;
	for (i = 0; i < studentCount; i++) {
		if (students[i].id == searchId) {
			found = 1;
			printf("ѧ���ɼ���Ϣ��\n");
			printf("����: %s\n", students[i].name);
			printf("ѧ��: %d\n", students[i].id);
			printf("��һ�ſγɼ�: %.2f\n", students[i].grade1);
			printf("�ڶ��ſγɼ�: %.2f\n", students[i].grade2);
			printf("�����ſγɼ�: %.2f\n", students[i].grade3);
			printf("�ܷ�: %.2f\n", students[i].totalGrade);
			break;
		}
	}
	
	if (!found) {
		printf("δ�ҵ���ѧ���ɼ���Ϣ��\n");
	}
}

void modifyStudent() {
	int modifyId;
	printf("������Ҫ�޸�ѧ���ɼ���ѧ��: ");
	scanf("%d", &modifyId);
	
	int found = 0;
	int i;
	for (i = 0; i < studentCount; i++) {
		if (students[i].id == modifyId) {
			found = 1;
			printf("�������޸ĺ�ĵ�һ�ſγɼ�: ");
			scanf("%f", &students[i].grade1);
			printf("�������޸ĺ�ĵڶ��ſγɼ�: ");
			scanf("%f", &students[i].grade2);
			printf("�������޸ĺ�ĵ����ſγɼ�: ");
			scanf("%f", &students[i].grade3);
			
			students[i].totalGrade = students[i].grade1 +
			students[i].grade2 +
			students[i].grade3;
			
			printf("ѧ���ɼ���Ϣ�޸ĳɹ���\n");
			break;
		}
	}
	
	if (!found) {
		printf("δ�ҵ���ѧ���ɼ���Ϣ��\n");
	}
}

void insertStudent() {
	if (studentCount >= MAX_STUDENTS) {
		printf("ѧ�������Ѵ����ޣ��޷����롣\n");
		return;
	}
	
	int position;
	printf("������Ҫ�����λ��(1-%d): ", studentCount + 1);
	scanf("%d", &position);
	
	if (position < 1 || position > studentCount + 1) {
		printf("��Ч�Ĳ���λ�á�\n");
		return;
	}
	
	printf("������ѧ������: ");
	scanf("%s", students[studentCount].name);
	printf("������ѧ��ѧ��: ");
	scanf("%d", &students[studentCount].id);
	printf("�������һ�ſγɼ�: ");
	scanf("%f", &students[studentCount].grade1);
	printf("������ڶ��ſγɼ�: ");
	scanf("%f", &students[studentCount].grade2);
	printf("����������ſγɼ�: ");
	scanf("%f", &students[studentCount].grade3);
	
	students[studentCount].totalGrade = students[studentCount].grade1 +
	students[studentCount].grade2 +
	students[studentCount].grade3;
	int i;
	for (i = studentCount; i > position - 1; i--) {
		students[i] = students[i - 1];
	}
	studentCount++;
	
	printf("ѧ���ɼ���Ϣ����ɹ���\n");
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
	
	printf("ѧ���ɼ���Ϣ���ܷ�����ɹ���\n");
}

void statistics() {
	printf("��ѧ����: %d\n", studentCount);
	
	int below60Count = 0;
	int i;
	for (i = 0; i < studentCount; i++) {
		if (students[i].grade1 < 60 || students[i].grade2 < 60 || students[i].grade3 < 60) {
			below60Count++;
		}
	}
	printf("ÿ�ſγ�С��60�ֵ�����: %d\n", below60Count);
	
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
	printf("��һ�ſγ̵���߷�: %.2f\n", maxGrade1);
	printf("�ڶ��ſγ̵���߷�: %.2f\n", maxGrade2);
	printf("�����ſγ̵���߷�: %.2f\n", maxGrade3);
}

void showAllStudents() {
	printf("����ѧ����Ϣ��\n");
	printf("%-5s%-15s%-8s%-8s%-8s%-8s\n", "ѧ��", "����", "�γ�1", "�γ�2", "�γ�3", "�ܷ�");
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
		printf("�޷��������ݵ��ļ���\n");
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
	printf("���ݱ���ɹ���\n");
}

void loadDataFromFile() {
	FILE *file = fopen(FILENAME, "r");
	if (file == NULL) {
		printf("�޷����ļ��������ݡ�\n");
		return;
	}
	
	while (fscanf(file, "%s %d %f %f %f %f",
		students[studentCount].name, &students[studentCount].id,
		&students[studentCount].grade1, &students[studentCount].grade2,
		&students[studentCount].grade3, &students[studentCount].totalGrade) == 6) {
		studentCount++;
	}
	
	fclose(file);
	printf("���ݼ��سɹ���\n");
}

void clearScreen() {
#ifdef _WIN32
	system("cls");
#else
	system("clear");
#endif
}

