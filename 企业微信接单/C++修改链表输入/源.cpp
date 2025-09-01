#include<iostream>
#include <windows.h>
using namespace std;
#define maxsize 100
typedef struct LNode {
	char data;
	struct LNode* next;
} LinkList;
void GreatListR(LinkList*& L, char a[], int n) { //β�巨����
	LinkList* s, * r;
	int i;
	L = (LinkList*)malloc(sizeof(LinkList)); //����ͷ�ڵ�
	r = L;
	for (i = 0; i < n; i++) {
		s = (LinkList*)malloc(sizeof(LinkList));
		s->data = a[i];
		r->next = s;
		r = s;
	}
	r->next = NULL;
}
void InitList(LinkList * &L) { //��ʼ�����Ա�
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
void DispList(LinkList* L) { //������Ա�
	LinkList* p = L->next;
	while (p != NULL) {
		if ((p->data >= 'a') && (p->data <= 'z'))
			cout << p->data;
		p = p->next;
	}
	cout << endl;
}
void sort(LinkList*& L) { //Ԫ������
	LinkList* p, * pre, * q;
	p = L->next->next; //p ָ�� L �ĵ� 2 �����ݽڵ�
	L->next->next = NULL; //����ֻ��һ�����ݽڵ�������
	while (p != NULL) {
		q = p->next;
		while (p != NULL) {
			q = p->next; //q ����*p �ڵ�û��̽ڵ��ָ��
			pre = L; //�������ͷ���бȽϣ� pre ָ�����*p ��ǰ���ڵ�
			while (pre->next != NULL && pre->next->data < p->data)
				pre = pre->next;
			p->next = pre->next;
			pre->next = p;
			p = q;
		}
	}
}
void bingji(LinkList* L, LinkList* N, LinkList*& M) { //��������
	LinkList* pa = L->next, * pb = N->next, * r, * s; //ʱ�鲢�㷨
	M = (LinkList*)malloc(sizeof(LinkList));
	r = M;
	while (pa != NULL && pb != NULL) { //���Ϻϲ�
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
	cout << "�������ϵĲ���Ϊ set1�� set2:";
}
void dels(LinkList*& M) { //ɾ����ͬԪ�� ����һ��
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
void jiaoji(LinkList*& M, LinkList* L, LinkList* N) { //��������
	LinkList* pa = L->next, * pb = N->next, * q, * r; //�Ե����� M ��ͷ�ڵ㴴��һ���յ�����
	M->next = NULL;
	r = M; //rָ���������������һ���ڵ�
	while (pa != NULL) { //�� pa ɨ�赥���� M �����ݽڵ㣬 �ж��Ƿ��ڵ����� L �� N ��
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
	cout << "�������ϵĽ���Ϊ set1�� set2=";
}
void chayunsuan(LinkList* L, LinkList* M, LinkList*& K) { //���ϲ�����
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
	cout << "�������ϵĲΪ set1 - set2=";
}
int main() {
	cout << "****************************** �� �� �� �� �� �� �� �� �� ��******************************\n ���������롰e�� �˳����㣬 ���򰴻س��������´����㣡 \n";
	system("color B5");
	int k;
	LinkList * L, *N, *U, *M, *K;
	for (k = 0;; k++) {
		int i, j;
		char set1[maxsize], set2[maxsize];
		cout << "�����뼯�� set1=";
		cin.getline(set1,maxsize);
		cout<<"���set1:  "<<set1<<endl;
		i = strlen(set1);
		//�س��˳�����
//		for (i = 0; i < maxsize; i++) {
//			cin >> set1[i];
//			if (set1[i] == '\n')
//				break;
//		}
		InitList(L);
		InitList(N);
		GreatListR(L, set1, i);
		GreatListR(U, set1, i);
		sort(U); //Ԫ������
		dels(U); //ɾ����ͬԪ�� ����һ��
		sort(L); //Ԫ������
		dels(L); //ɾ����ͬԪ�� ����һ��
		cout << "�����뼯��"<<set2;
		cin.getline(set2,maxsize);
		cout<<"���set2:  "<<set2<<endl;
		j = strlen(set2);
//		for (j = 0; j < maxsize; j++) {
//			cin >> set2[j];
//			if (set2[j] == '\n')
//				break;
//		}
		
		GreatListR(N, set2, j);
		sort(N); //Ԫ������
		dels(N); //ɾ����ͬԪ�� ����һ��
		bingji(L, N, M); //���Ϻϲ�
		dels(M); //ɾ����ͬԪ�� ����һ��
		DispList(M);
		jiaoji(M, L, N); //��������
		DispList(M);
		chayunsuan(U, M, K); //���ϲ�����
		DispList(K);
		char n;
		cout << "\n �Ƿ��˳����㣿 \n";
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
