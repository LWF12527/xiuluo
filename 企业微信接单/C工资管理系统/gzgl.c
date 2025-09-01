#include <stdio.h>  /*��׼�������������*/
#include <stdlib.h>  /*��׼������*/
#include <string.h>  /*�ַ���������*/

#define HEADER1 " -----------------------------------------------------------Employer------------------------------------------------------------- \n"
#define HEADER2 "|     number    |     name      |     salary    |     bonus     |   deduction   |    paysalary  |    taxes      |  realsalary   | \n"
#define HEADER3 "|---------------|---------------|---------------|---------------|---------------|---------------|---------------|---------------| \n"
#define FORMAT  "|%-15s|%-15s|%15.2f|%15.2f|%15.2f|%15.2f|%15.2f|%15.2f| \n"
#define DATA      per->num,per->name,per->salary,per->bonus,per->deduction,per->paysalary,per->taxes,per->realsalary
#define END     "---------------------------------------------------------------------------------------------------------------------------- ---- \n"
#define N 60
int saveflag=0;  /*�Ƿ���Ҫ���̵ı�־����*/
/*������ְ���йص����ݽṹ*/
typedef struct employee      /*���Ϊemployee*/
{
char num[10];   /*ְ�����*/
char name[15];  /*ְ������*/
float salary;     /*��������*/
float bonus;       /*����*/
float deduction;       /*�ۿ�*/
float paysalary;     /*Ӧ������*/
float taxes;       /*˰��*/
float realsalary;     /*ʵ������*/
}Employer;

void menu()  /*���˵�*/
{
system("clear");   /*����*/
printf("                 The Employee' Salary Management System \n");
printf("     *************************Menu********************************\n");
printf("     *  1 input   record             2 delete record             *\n");
printf("     *  3 search  record             4 modify record             *\n");
printf("     *  5 insert  record             6 count  record             *\n");
printf("     *  7 sort    reord              8 save   record             *\n");
printf("     *  9 display record             0 quit   system             *\n");
printf("     *************************************************************\n");
/*printf()�͸�ʽ��������ı�������Ļ��*/
}
void printheader() /*��ʽ�������ͷ*/
{
  printf(HEADER1);
  printf(HEADER2);
  printf(HEADER3);
}
void printdata(Employer eminfo) /*��ʽ�������������*/
{
printf("printdata");   
}


void disp(Employer eminfo[],int n)  /*��ʾ����eminfo[]�д洢�ļ�¼������Ϊemployee�ṹ�ж��������*/
{
printf("Disp");   



}

void wrong()  /*�������������Ϣ*/
{
printf("\n\n\n\n\n***********Error:input has wrong! press any key to continue**********\n");
getchar();
}

void nofind()  /*���δ���Ҵ�ְ������Ϣ*/
{
printf("\n=====>Not find this employee record!\n");
}

/*************************************************************
���ã����ڶ�λ�����з���Ҫ��ļ�¼�������ر���ü�¼������Ԫ���±�ֵ
������findmess[]����Ҫ���ҵľ�������; nameornum[]���水ʲô�������в���;
**************************************************************/
int locate(Employer eminfo[],int n,char findmess[],char nameornum[])
{

printf("Locate");   

}


/*�����ַ����������г�����֤(����<lens)*/
void stringinput(char *t,int lens,char *notice)
{
   char n[255];
   do{
      printf("%s",notice);  /*��ʾ��ʾ��Ϣ*/
      scanf("%s",n);  /*�����ַ���*/
      if(strlen(n)>lens) printf("\n exceed the required length! \n"); /*���г���У�飬����lensֵ��������*/
     }while(strlen(n)>lens);
     strcpy(t,n); /*��������ַ����������ַ���t��*/

}

/*������ֵ��<����ֵ)*/
float numberinput(char *notice)
{
  float t=0.00;
   do{
      printf("%s",notice);    /*��ʾ��ʾ��Ϣ*/
      scanf("%f",&t);  /*�����繤�ʵ���ֵ�͵�ֵ*/
      if(t<0) printf("\n score must >=0! \n"); /*������ֵУ��*/
   }while(t<0);
   return t;
}


 /*����ְ�����ʼ�¼*/
int add(Employer eminfo[],int n)
{
 printf("Add");   


}

/*��ְ����Ż���������ѯ��¼*/
void qur(Employer eminfo[],int n)
{
 printf("Qur");   


  
}

/*ɾ����¼�����ҵ�����ü�¼������Ԫ�ص��±�ֵ��Ȼ����������ɾ��������Ԫ��*/
int del(Employer eminfo[],int n)
{

printf("Del");  


}

/*�޸ļ�¼���Ȱ������ְ����Ų�ѯ���ü�¼��Ȼ����ʾ�û��޸ı��֮���ֵ����Ų����޸�*/
void modify(Employer eminfo[],int n)
{
printf("Modify");  



}

/*�����¼:��ְ����Ų�ѯ��Ҫ���������Ԫ�ص�λ�ã�Ȼ���ڸñ��֮�����һ��������Ԫ�ء�*/
int insert(Employer eminfo[],int n)
{
 
printf("Insert");  

}

/*ͳ�ƹ�˾��Ա���Ĺ����ڸ��ȼ�������*/
void sta(Employer eminfo[],int n)
{

printf("Stastic");  

}

/*����ð������ʵ������İ�ʵ�������ֶεĽ������򣬴Ӹߵ���*/
void sort(Employer eminfo[],int n)
{

printf("Sort");  

}




/*���ݴ���,���û�û��ר�Ž��д˲����Ҷ��������޸ģ����˳�ϵͳʱ������ʾ�û�����*/
void save(Employer eminfo[],int n)
{
printf(" Save");  


}


void main()
{
  Employer eminfomation[N];         /*����Employer�ṹ��*/
  FILE *fp;           /*�ļ�ָ��*/
  int select;         /*����ѡ��������*/
  char ch;            /*����(y,Y,n,N)*/
  int count=0;        /*�����ļ��еļ�¼��������Ԫ�ظ�����*/
   


}
//
//printf("Del");  
//
//
//}

///*�޸ļ�¼���Ȱ������ְ�����
