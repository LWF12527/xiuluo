#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <fstream> // 用于打开和写入物理文件
#include <iomanip> // 用于格式化输出
#include <filesystem> // 用于文件系统操作（C++17）
using namespace std;
namespace fs = std::filesystem;

// 文件属性结构
struct File {
	string name;          // 文件名
	string physicalPath;  // 物理路径
	string protection;    // 保护码（读写保护：R、W）
	int length;           // 文件长度
	bool isOpen;          // 是否处于打开状态
};

// 子目录结构
struct Directory {
	string dirName;                 // 目录名称
	map<string, File> files;        // 文件列表
};

// 主目录结构
struct MainDirectory {
	map<string, Directory> subDirs; // 子目录列表
	string currentDir;              // 当前活动目录
};

// 全局变量
MainDirectory fileSystem;
string currentUser = "";           // 当前登录的用户名
bool isLoggedIn = false;           // 登录状态

// 工具函数：初始化用户文件夹
void initUserFolder(const string &username) {
	string userPath = "./" + username; // 根目录下创建用户目录
	if (!fs::exists(userPath)) {
		fs::create_directory(userPath);
	}
	fileSystem.subDirs[username] = Directory{username}; // 用户主目录
	fileSystem.currentDir = username; // 设置当前活动目录为用户目录
}

// 用户登录
void login() {
	string username, password;
	cout << "请输入用户名：";
	cin >> username;
	cout << "请输入密码：";
	cin >> password;
	if (username == "admin" && password == "1234") { // 简单验证
		currentUser = username;
		isLoggedIn = true;
		initUserFolder(currentUser); // 初始化用户目录
		cout << "登录成功！" << endl;
	} else {
		cout << "用户名或密码错误！" << endl;
	}
}

// 列出当前目录下的文件
void dir() {
	if (!isLoggedIn) {
		cout << "请先登录系统！" << endl;
		return;
	}
	string currentDir = fileSystem.currentDir;
	if (currentDir.empty() || fileSystem.subDirs.find(currentDir) == fileSystem.subDirs.end()) {
		cout << "当前目录为空或不存在！" << endl;
		return;
	}
	Directory &directory = fileSystem.subDirs[currentDir];
	cout << "文件名\t物理路径\t保护码\t文件长度\t是否打开" << endl;
	for (auto &fileEntry : directory.files) {
		File &file = fileEntry.second;
		cout << file.name << "\t" << file.physicalPath << "\t" << file.protection << "\t"
		<< file.length << "\t\t" << (file.isOpen ? "是" : "否") << endl;
	}
}

// 创建文件
void create() {
	if (!isLoggedIn) {
		cout << "请先登录系统！" << endl;
		return;
	}
	string fileName;
	cout << "请输入文件名：";
	cin >> fileName;
	Directory &directory = fileSystem.subDirs[fileSystem.currentDir];
	if (directory.files.find(fileName) != directory.files.end()) {
		cout << "文件已存在！" << endl;
		return;
	}
	File newFile;
	newFile.name = fileName;
	newFile.physicalPath = "./" + currentUser + "/" + fileName; // 文件路径
	newFile.protection = "RW"; // 默认读写保护
	newFile.length = 0;        // 默认长度为0
	newFile.isOpen = false;
	
	// 在磁盘上创建文件
	ofstream outFile(newFile.physicalPath);
	if (outFile.is_open()) {
		outFile << ""; // 写入空内容
		outFile.close();
	} else {
		cout << "文件创建失败！" << endl;
		return;
	}
	
	directory.files[fileName] = newFile;
	cout << "文件 " << fileName << " 创建成功，路径：" << newFile.physicalPath << endl;
}

// 删除文件
void deleteFile() {
	if (!isLoggedIn) {
		cout << "请先登录系统！" << endl;
		return;
	}
	string fileName;
	cout << "请输入要删除的文件名：";
	cin >> fileName;
	Directory &directory = fileSystem.subDirs[fileSystem.currentDir];
	if (directory.files.find(fileName) == directory.files.end()) {
		cout << "文件不存在！" << endl;
		return;
	}
	
	// 删除磁盘上的文件
	string filePath = directory.files[fileName].physicalPath;
	if (fs::exists(filePath)) {
		fs::remove(filePath);
	}
	
	directory.files.erase(fileName);
	cout << "文件 " << fileName << " 删除成功！" << endl;
}

// 打开文件
void open() {
	if (!isLoggedIn) {
		cout << "请先登录系统！" << endl;
		return;
	}
	string fileName;
	cout << "请输入要打开的文件名：";
	cin >> fileName;
	Directory &directory = fileSystem.subDirs[fileSystem.currentDir];
	if (directory.files.find(fileName) == directory.files.end()) {
		cout << "文件不存在！" << endl;
		return;
	}
	File &file = directory.files[fileName];
	if (file.isOpen) {
		cout << "文件已处于打开状态！" << endl;
		return;
	}
	file.isOpen = true;
	
	// 在桌面模拟打开文件
	cout << "文件 " << file.name << " 已打开，路径：" << file.physicalPath << endl;
	system(("notepad " + file.physicalPath).c_str()); // 使用 Notepad 打开文件（Windows 系统）
}

// 关闭文件
void close() {
	if (!isLoggedIn) {
		cout << "请先登录系统！" << endl;
		return;
	}
	string fileName;
	cout << "请输入要关闭的文件名：";
	cin >> fileName;
	Directory &directory = fileSystem.subDirs[fileSystem.currentDir];
	if (directory.files.find(fileName) == directory.files.end()) {
		cout << "文件不存在！" << endl;
		return;
	}
	File &file = directory.files[fileName];
	if (!file.isOpen) {
		cout << "文件未处于打开状态！" << endl;
		return;
	}
	file.isOpen = false;
	cout << "文件 " << file.name << " 已关闭！" << endl;
}

// 主函数
int main() {
	int choice;
	do {
		cout << "\n=== 简单文件系统 ===\n";
		cout << "1. 登录系统\n2. 列目录\n3. 创建文件\n4. 删除文件\n5. 打开文件\n6. 关闭文件\n0. 退出\n";
		cout << "请输入选项：";
		cin >> choice;
		switch (choice) {
			case 1: login(); break;
			case 2: dir(); break;
			case 3: create(); break;
			case 4: deleteFile(); break;
			case 5: open(); break;
			case 6: close(); break;
			case 0: cout << "退出系统！" << endl; break;
			default: cout << "无效选项！" << endl;
		}
	} while (choice != 0);
	return 0;
}

