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
int saveflag=0;  /*是否需要存盘的标志变量*/
/*定义与职工有关的数据结构*/
typedef struct employee      /*标记为employee*/
{
char num[10];   /*职工编号*/
char name[15];  /*职工姓名*/
float salary;     /*基本工资*/
float bonus;       /*奖金*/
float deduction;       /*扣款*/
float paysalary;     /*应发工资*/
float taxes;       /*税款*/
float realsalary;     /*实发工资*/
}Employer;

void menu()  /*主菜单*/
{
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
void printheader() /*格式化输出表头*/
{
  printf(HEADER1);
  printf(HEADER2);
  printf(HEADER3);
}
void printdata(Employer eminfo) /*格式化输出表中数据*/
{
printf("printdata");   
}


void disp(Employer eminfo[],int n)  /*显示数组eminfo[]中存储的记录，内容为employee结构中定义的内容*/
{
printf("Disp");   



}

void wrong()  /*输出按键错误信息*/
{
printf("\n\n\n\n\n***********Error:input has wrong! press any key to continue**********\n");
getchar();
}

void nofind()  /*输出未查找此职工的信息*/
{
printf("\n=====>Not find this employee record!\n");
}

/*************************************************************
作用：用于定位数组中符合要求的记录，并返回保存该记录的数组元素下标值
参数：findmess[]保存要查找的具体内容; nameornum[]保存按什么在数组中查找;
**************************************************************/
int locate(Employer eminfo[],int n,char findmess[],char nameornum[])
{

printf("Locate");   

}


/*输入字符串，并进行长度验证(长度<lens)*/
void stringinput(char *t,int lens,char *notice)
{
   char n[255];
   do{
      printf("%s",notice);  /*显示提示信息*/
      scanf("%s",n);  /*输入字符串*/
      if(strlen(n)>lens) printf("\n exceed the required length! \n"); /*进行长度校验，超过lens值重新输入*/
     }while(strlen(n)>lens);
     strcpy(t,n); /*将输入的字符串拷贝到字符串t中*/

}

/*输入数值，<＝数值)*/
float numberinput(char *notice)
{
  float t=0.00;
   do{
      printf("%s",notice);    /*显示提示信息*/
      scanf("%f",&t);  /*输入如工资等数值型的值*/
      if(t<0) printf("\n score must >=0! \n"); /*进行数值校验*/
   }while(t<0);
   return t;
}


 /*增加职工工资记录*/
int add(Employer eminfo[],int n)
{
 printf("Add");   


}

/*按职工编号或姓名，查询记录*/
void qur(Employer eminfo[],int n)
{
 printf("Qur");   


  
}

/*删除记录：先找到保存该记录的数组元素的下标值，然后在数组中删除该数组元素*/
int del(Employer eminfo[],int n)
{

printf("Del");  


}

/*修改记录。先按输入的职工编号查询到该记录，然后提示用户修改编号之外的值，编号不能修改*/
void modify(Employer eminfo[],int n)
{
printf("Modify");  



}

/*插入记录:按职工编号查询到要插入的数组元素的位置，然后在该编号之后插入一个新数组元素。*/
int insert(Employer eminfo[],int n)
{
 
printf("Insert");  

}

/*统计公司的员工的工资在各等级的人数*/
void sta(Employer eminfo[],int n)
{

printf("Stastic");  

}

/*利用冒泡排序法实现数组的按实发工资字段的降序排序，从高到低*/
void sort(Employer eminfo[],int n)
{

printf("Sort");  

}




/*数据存盘,若用户没有专门进行此操作且对数据有修改，在退出系统时，会提示用户存盘*/
void save(Employer eminfo[],int n)
{
printf(" Save");  


}


void main()
{
  Employer eminfomation[N];         /*定义Employer结构体*/
  FILE *fp;           /*文件指针*/
  int select;         /*保存选择结果变量*/
  char ch;            /*保存(y,Y,n,N)*/
  int count=0;        /*保存文件中的记录条数（或元素个数）*/
   


}
//
//printf("Del");  
//
//
//}

///*修改记录。先按输入的职工编号
