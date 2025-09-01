#include<stdio.h>               //头文件名,包含输入输出函数等
#include<stdlib.h>              //头文件名
#include<time.h>               //头文件名
#define PROCESS_NUMBER 5   //宏定义,定义进程个数为5
#define RESOURCE_NUMBER 3   //宏定义,资源类个数是3
#define true 1                  //宏定义,定义true为1
#define false 0                 //宏定义，定义false为0
typedef int bool;                //宏定义，定义bool为int类型
int Available[RESOURCE_NUMBER]={4,5,3}; //系统中三类可利用资源数分别为4，5，3
int Max[PROCESS_NUMBER][ RESOURCE_NUMBER]={{8,4,2},{3,3,2},{9,0,2},{2,1,2},{4,3,3}};               //每个进程所需求的资源最大数
int Allocation[PROCESS_NUMBER][RESOURCE_NUMBER]={
{0,1,1},
{2,0,0},
{2,0,2},
{2,1,1},
{0,0,2}};

int Need[PROCESS_NUMBER][ RESOURCE_NUMBER];  //各进程的当前需求向量
bool compare(int *a,int *b,int n)           //比较两个一维数组，如果a中各项均大于b，则返回true，否则为false
{ int i;
	for(i=0;i<n;i++)
		if(a[i]<b[i])
			return false;
	return true;
}
void assign(int *a,int *b,int n)        //将数组b的值赋给a,n为数组的大小
{ int i;
	for(i=0;i<n;i++)
		a[i]=b[i];
}
void add(int *a,int *b,int n)   //两个一维数组的加法，各对应项相加
{
	int i;
	for(i=0;i<n;i++)
		a[i]+=b[i];
}
void substract(int *a,int*b,int n)   //两个一维数组的减法，各对应项相减
{
	int i;
	for(i=0;i<n;i++)
		a[i]-=b[i];
}
void print(int *a,int n)      //打印一维数组
{
	int i;
	for(i=0;i<n;i++)
		printf("%4d",a[i]);
	printf("\n");
}
bool issafe(int *sp)                 //判断是否是安全状态
{
	int i;
	int count=0;                 //记录finish[i]=true 的进程个数为0
	int n=0;
	int work[RESOURCE_NUMBER];
	bool finish[PROCESS_NUMBER];
	//work=av
	assign(work,Available, RESOURCE_NUMBER);
	//初始化标记 finish
	for(i=0;i< PROCESS_NUMBER;i++)
		finish[i]=false;
	n= PROCESS_NUMBER;      //n为进城的个数
	while(n--)              //循环最多执行n次
		for(i=0;i< PROCESS_NUMBER;i++)
			if(finish[i]==false&&compare(work,Need[i], RESOURCE_NUMBER)) //判断能否满
				//足进程i的要求，work＞＝need[i]是否成立
			{
				add(work,Allocation[i], RESOURCE_NUMBER);  //分配，待进程完成后再释放
				finish[i]=true;                    
				sp[count]=i;                       //记录安全路径
				count++;              //记录能够满足的进程数+1
			}                                          
	if(count>= PROCESS_NUMBER)
		return true;
	else
		return false;
}
bool request(int pid,int *r,int n)
{
	int i;             
	int sp[5];                                           //记录安全路径
	if(compare(Need[pid],r,n)==true&&compare(Available,r,n)==true)  //如果
		//request[i]<=need[i]且request[i]<=available
	{                                                   //尝试分配资源
		substract(Available,r, RESOURCE_NUMBER);
		add(Allocation[pid],r, RESOURCE_NUMBER);
		substract(Need[pid],r, RESOURCE_NUMBER);
		if(issafe(sp))                                  //判断是否是安全状态
		{  
			printf("Security Path:\n\t");
			for(i=0;i< PROCESS_NUMBER;i++)               //打印安全路径
				printf("p%d",sp[i]);
			printf("\n");                            //可以分配
			return true;
		} 
		else
		{ add(Available,r, RESOURCE_NUMBER);                     //不分配
			substract(Allocation[pid],r, RESOURCE_NUMBER);    //恢复到分配前的状态
			add(Need[pid],r, RESOURCE_NUMBER);
			return false;
		}
		
	}
	else		return false;
}
//提示信息
char hint()
{   char ch;
	printf("\t------------------Operation  Hint----------\n"); 
	//按A或者a键自动分配资源
	printf("\tA(a)------------Apply For resource automated\n");
	//按H或者h键自动分配资源
	printf("\tH(h)-------------Apply For resource by human\n");
	//按Q或者q键自动分配资源
	printf("\tQ(q)-------quit\n");
	scanf("%c",&ch);
	return ch;
}
//显示系统信息
void init(){  
	int i;;
	int temp[RESOURCE_NUMBER];
	printf("Processs Numbers: %d\n Need and Allocation respectively as follow:\n",PROCESS_NUMBER);
	//显示进程最大资源需求
	for(i=0;i<PROCESS_NUMBER;i++)
	{ printf("\t process %d max need:",i);
		print(Max[i],RESOURCE_NUMBER);
	}
	printf("\n");
	//计算需求向量：Need[i]=MAX[i]-Alocation[i]
	for(i=0;i<PROCESS_NUMBER;i++){
		assign(temp,Max[i],RESOURCE_NUMBER);
		substract(temp,Allocation[i],RESOURCE_NUMBER);
		assign(Need[i],temp,RESOURCE_NUMBER);
	}
	//显示进程已分配资源
	for(i=0;i<PROCESS_NUMBER;i++){
		printf("\t processs %d allocated resources:",i);
		print(Allocation[i],RESOURCE_NUMBER);
	}
	//显示系统可用资源 
	printf("\t available resources:\t");
	print(Available,RESOURCE_NUMBER);
}
//输入
void input(int *r,int n,int *id)
{    int i;
	//提示输入进程号
	printf("please input process id(0~ %d):",n-1);
	//从键盘输入进程号
	scanf("%d",id);
	for(i=0;i<n;i++){ 
		printf("\nthe numbers of needed resource  %d(int):",i);
		scanf("%d",&r[i]);
	}
	//显示刚才输入的数据
	printf("\ndata you inputed: Request[%d](",*id);
	for(i=0;i<n;i++)
		printf("%d",r[i]);
	printf(")\n");
}
//检查输入
bool check(int id,int *r,int n)
{   
	int i;
	//判断申请资源数目是否合法
	for(i=0;i<n;i++)
		if(r[i]<0)
			return false;
	//判断进程号是否合法
	if(id>=PROCESS_NUMBER)
		return false;
	else 
		return true;
}
int main()
{
	//进程id号
	int id;
	//控制字符
	char control;
	//资源请求向量
	int r[3];
	//显示开始信息
	init();
	//随机数初始化
	srand((int)time(0));
	//主控过程
	while(1)
	{
		//提示
		control=hint();
		if(control=='a'||control=='A')
		{
			//随机申请资源
			id=rand()%5;
			r[0]=rand()%5;
			r[1]=rand()%5;
			r[2]=rand()%5;
			//显示申请信息
			printf("\tRequest[%d](%d,%d,%d)\n",id,r[0],r[1],r[2]);
			if(request(id,r,RESOURCE_NUMBER))
				printf("Alloc Success!\n");
			else
				printf("Alloc Failed!\n");
		}
		else if(control=='h'||control=='H')
		{
			//输入申请信息
			input(r,RESOURCE_NUMBER,&id);
			//检查输入是否合法
			if(check(id,r,RESOURCE_NUMBER)==false)
			{
				printf("\nInput Error!please reinput!\n");
				continue;
			}
			//换行
			if(request(id,r,RESOURCE_NUMBER))
				printf("Request Succeed!\n");
			else
				printf("Request Fail!\n");
		}
		else if(control=='q'||control=='Q')
			exit(0);
		//显示当前系统资源和进程情况
		printf("Available Resource\n");
		print(Available,RESOURCE_NUMBER);
		//显示资源最大需求
		printf("process %d max need\n",id);
		print(Max[id],RESOURCE_NUMBER);
		//显示已分配资源情况
		printf("process %d allocated resources\n",id);
		print(Allocation[id],RESOURCE_NUMBER);
	}	
	return 0;
}

