#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

struct Student {
	string studentId;
	string name;
	int age;
	string gender;
	string birthDate;
	string address;
	string phone;
	string email;
};

vector<Student> students;

void addStudent() {
	Student newStudent;
	cout << "请输入学号: ";
	cin >> newStudent.studentId;
	cout << "请输入姓名: ";
	cin >> newStudent.name;
	cout << "请输入年龄: ";
	cin >> newStudent.age;
	cout << "请输入性别: ";
	cin >> newStudent.gender;
	cout << "请输入出生年月: ";
	cin >> newStudent.birthDate;
	cout << "请输入家庭住址: ";
	cin >> newStudent.address;
	cout << "请输入电话: ";
	cin >> newStudent.phone;
	cout << "请输入E-mail: ";
	cin >> newStudent.email;
	
	students.push_back(newStudent);
	cout << "学生信息添加成功！" << endl;
}

void displayStudent(const Student& student) {
	cout << "学号: " << student.studentId << endl;
	cout << "姓名: " << student.name << endl;
	cout << "年龄: " << student.age << endl;
	cout << "性别: " << student.gender << endl;
	cout << "出生年月: " << student.birthDate << endl;
	cout << "家庭住址: " << student.address << endl;
	cout << "电话: " << student.phone << endl;
	cout << "E-mail: " << student.email << endl;
	cout << endl;
}

void searchStudentById(const string& studentId) {
	bool found = false;
	for (const auto& student : students) {
		if (student.studentId == studentId) {
			displayStudent(student);
			found = true;
			break;
		}
	}
	if (!found) {
		cout << "没有找到该学号的学生。" << endl;
	}
}

void searchStudentByName(const string& name) {
	bool found = false;
	for (const auto& student : students) {
		if (student.name == name) {
			displayStudent(student);
			found = true;
		}
	}
	if (!found) {
		cout << "没有找到该姓名的学生。" << endl;
	}
}

bool compareStudentById(const Student& student1, const Student& student2) {
	return student1.studentId < student2.studentId;
}

bool compareStudentByName(const Student& student1, const Student& student2) {
	return student1.name < student2.name;
}

void sortStudentsById() {
	sort(students.begin(), students.end(), compareStudentById);
	cout << "已按学号排序。" << endl;
	for (const auto& student : students) {
		displayStudent(student);
	}
}

void sortStudentsByName() {
	sort(students.begin(), students.end(), compareStudentByName);
	cout << "已按姓名排序。" << endl;
	for (const auto& student : students) {
		displayStudent(student);
	}
}

void deleteStudent(const string& studentId) {
	for (auto it = students.begin(); it != students.end(); ++it) {
		if (it->studentId == studentId) {
			students.erase(it);
			cout << "学生信息删除成功！" << endl;
			return;
		}
	}
	cout << "没有找到该学号的学生。" << endl;
}

void menuAdmin() {
	while (true) {
		cout << "---------------------" << endl;
		cout << "系统管理员菜单：" << endl;
		cout << "1. 添加学生信息" << endl;
		cout << "2. 查询学生信息（按学号）" << endl;
		cout << "3. 查询学生信息（按姓名）" << endl;
		cout << "4. 按学号排序" << endl;
		cout << "5. 按姓名排序" << endl;
		cout << "6. 删除学生信息" << endl;
		cout << "0. 退出系统" << endl;
		cout << "请输入操作编号: ";
		
		int choice;
		cin >> choice;
		
		if (choice == 0) {
			break;
		}
		
		switch (choice) {
		case 1:
			addStudent();
			break;
			case 2: {
				string studentId;
				cout << "请输入要查询的学生学号: ";
				cin >> studentId;
				searchStudentById(studentId);
				break;
			}
			case 3: {
				string name;
				cout << "请输入要查询的学生姓名: ";
				cin >> name;
				searchStudentByName(name);
				break;
			}
		case 4:
			sortStudentsById();
			break;
		case 5:
			sortStudentsByName();
			break;
			case 6: {
				string studentId;
				cout << "请输入要删除的学生学号: ";
				cin >> studentId;
				deleteStudent(studentId);
				break;
			}
		default:
			cout << "无效的操作编号，请重新输入。" << endl;
			break;
		}
	}
}

void menuStudent() {
	while (true) {
		cout << "---------------------" << endl;
		cout << "学生菜单：" << endl;
		cout << "1. 查询学生信息（按学号）" << endl;
		cout << "2. 查询学生信息（按姓名）" << endl;
		cout << "0. 退出系统" << endl;
		cout << "请输入操作编号: ";
		
		int choice;
		cin >> choice;
		
		if (choice == 0) {
			break;
		}
		
		switch (choice) {
			case 1: {
				string studentId;
				cout << "请输入要查询的学生学号: ";
				cin >> studentId;
				searchStudentById(studentId);
				break;
			}
			case 2: {
				string name;
				cout << "请输入要查询的学生姓名: ";
				cin >> name;
				searchStudentByName(name);
				break;
			}
		default:
			cout << "无效的操作编号，请重新输入。" << endl;
			break;
		}
	}
}

int main() {
	while (true) {
		cout << "---------------------" << endl;
		cout << "欢迎使用学生信息管理系统！" << endl;
		cout << "请选择登录角色：" << endl;
		cout << "1. 系统管理员" << endl;
		cout << "2. 学生" << endl;
		cout << "0. 退出系统" << endl;
		cout << "请输入角色编号: ";
		
		int role;
		cin >> role;
		
		if (role == 0) {
			break;
		}
		
		switch (role) {
		case 1:
			menuAdmin();
			break;
		case 2:
			menuStudent();
			break;
		default:
			cout << "无效的角色编号，请重新输入。" << endl;
			break;
		}
	}
	
	return 0;
}
