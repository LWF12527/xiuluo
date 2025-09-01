#include<iostream>
#include <windows.h>
using namespace std;
#define maxsize 100
typedef struct LNode {
	char data;
	struct LNode* next;
} LinkList;
void GreatListR(LinkList*& L, char a[], int n) { //尾插法建表
	LinkList* s, * r;
	int i;
	L = (LinkList*)malloc(sizeof(LinkList)); //创建头节点
	r = L;
	for (i = 0; i < n; i++) {
		s = (LinkList*)malloc(sizeof(LinkList));
		s->data = a[i];
		r->next = s;
		r = s;
	}
	r->next = NULL;
}
void InitList(LinkList * &L) { //初始化线性表
	L = (LinkList*)malloc(sizeof(LinkList));
	L->next = NULL;
}
void DestroyList(LinkList*& L) {
	LinkList* pre = L, * p = L->next;
	while (p != NULL) {
		free(pre);
		pre = p;
		p = pre->next;
	}
	free(pre);
}
void DispList(LinkList* L) { //输出线性表
	LinkList* p = L->next;
	while (p != NULL) {
		if ((p->data >= 'a') && (p->data <= 'z'))
			cout << p->data;
		p = p->next;
	}
	cout << endl;
}
void sort(LinkList*& L) { //元素排序
	LinkList* p, * pre, * q;
	p = L->next->next; //p 指向 L 的第 2 个数据节点
	L->next->next = NULL; //构件只含一个数据节点的有序表
	while (p != NULL) {
		q = p->next;
		while (p != NULL) {
			q = p->next; //q 保存*p 节点没后继节点的指针
			pre = L; //从有序表开头进行比较， pre 指向插入*p 的前驱节点
			while (pre->next != NULL && pre->next->data < p->data)
				pre = pre->next;
			p->next = pre->next;
			pre->next = p;
			p = q;
		}
	}
}
void bingji(LinkList* L, LinkList* N, LinkList*& M) { //并集运算
	LinkList* pa = L->next, * pb = N->next, * r, * s; //时归并算法
	M = (LinkList*)malloc(sizeof(LinkList));
	r = M;
	while (pa != NULL && pb != NULL) { //集合合并
		if (pa->data < pb->data) {
			s = (LinkList*)malloc(sizeof(LinkList));
			s->data = pa->data;
			r->next = s;
			r = s;
			pa = pa->next;
		} else {
			s = (LinkList*)malloc(sizeof(LinkList));
			s->data = pb->data;
			r->next = s;
			r = s;
			pb = pb->next;
		}
	}
	while (pa != NULL) {
		s = (LinkList*)malloc(sizeof(LinkList));
		s->data = pa->data;
		r->next = s;
		r = s;
		pa = pa->next;
	}
	while (pb != NULL) {
		s = (LinkList*)malloc(sizeof(LinkList));
		s->data = pb->data;
		r->next = s;
		r = s;
		pb = pb->next;
	}
	r->next = NULL;
	cout << "两个集合的并集为 set1∪ set2:";
}
void dels(LinkList*& M) { //删除相同元素 仅留一个
	LinkList* p = M->next, * q;
	while (p->next != NULL) {
		if (p->data == p->next->data) {
			q = p->next;
			p->next = q->next;
			free(q);
		} else
			p = p->next;
	}
}
void jiaoji(LinkList*& M, LinkList* L, LinkList* N) { //交集运算
	LinkList* pa = L->next, * pb = N->next, * q, * r; //以单链表 M 的头节点创建一个空单链表
	M->next = NULL;
	r = M; //r指向这个新链表的最后一个节点
	while (pa != NULL) { //以 pa 扫描单链表 M 的数据节点， 判断是否在单链表 L 和 N 中
		while (pb != NULL && pa->data > pb->data)
			pb = pb->next;
		if (pa != NULL && pb != NULL && pa->data == pb->data) {
			r->next = pa;
			r = pa;
			pa = pa->next;
		} else {
			q = pa;
			pa = pa->next;
			free(q);
		}
	}
	r->next = NULL;
	cout << "两个集合的交集为 set1∩ set2=";
}
void chayunsuan(LinkList* L, LinkList* M, LinkList*& K) { //集合差运算
	LinkList* p1 = L->next, * p2 = M->next, * s, * r;
	K = (LinkList*)malloc(sizeof(LinkList));
	r = K;
	r->next = NULL;
	while (p1 != NULL) {
		p2 = M->next;
		while (p2 != NULL && p2->data != p1->data)
			p2 = p2->next;
		if (p2 == NULL) {
			s = (LinkList*)malloc(sizeof(LinkList));
			s->data = p1->data;
			r->next = s;
			r = s;
		}
		p1 = p1->next;
	}
	r->next = NULL;
	cout << "两个集合的差集为 set1 - set2=";
}
int main() {
	cout << "****************************** 集 合 的 并 、 交 和 差 运 算******************************\n 运算完输入“e” 退出运算， 否则按回车键继续下次运算！ \n";
	system("color B5");
	int k;
	LinkList * L, *N, *U, *M, *K;
	for (k = 0;; k++) {
		int i, j;
		char set1[maxsize], set2[maxsize];
		cout << "请输入集合 set1=";
		cin.getline(set1,maxsize);
		cout<<"输出set1:  "<<set1<<endl;
		i = strlen(set1);
		//回车退出输入
//		for (i = 0; i < maxsize; i++) {
//			cin >> set1[i];
//			if (set1[i] == '\n')
//				break;
//		}
		InitList(L);
		InitList(N);
		GreatListR(L, set1, i);
		GreatListR(U, set1, i);
		sort(U); //元素排序
		dels(U); //删除相同元素 仅留一个
		sort(L); //元素排序
		dels(L); //删除相同元素 仅留一个
		cout << "请输入集合"<<set2;
		cin.getline(set2,maxsize);
		cout<<"输出set2:  "<<set2<<endl;
		j = strlen(set2);
//		for (j = 0; j < maxsize; j++) {
//			cin >> set2[j];
//			if (set2[j] == '\n')
//				break;
//		}
		
		GreatListR(N, set2, j);
		sort(N); //元素排序
		dels(N); //删除相同元素 仅留一个
		bingji(L, N, M); //集合合并
		dels(M); //删除相同元素 仅留一个
		DispList(M);
		jiaoji(M, L, N); //交集运算
		DispList(M);
		chayunsuan(U, M, K); //集合差运算
		DispList(K);
		char n;
		cout << "\n 是否退出运算？ \n";
		cin >> n;
		if (n == 'e')
			exit(0);
	}
	DestroyList(L);
	DestroyList(N);
	DestroyList(U);
	DestroyList(M);
	DestroyList(K);
	system("PAUSE");
}
