#define _GNU_SOURCE
#include "sched.h"
#include "pthread.h"
#include "stdio.h"
#include "stdlib.h"
#include "semaphore.h"
#include "linux/sched.h"
#include "unistd.h"
#include "string.h"

#define BUFFER_LEN 8 //定义缓冲区长度
void producer(void *args);
void consumer(void *args);
pthread_mutex_t mutex;
sem_t product;
sem_t warehouse;

char buffer[BUFFER_LEN][4];
int in,out;  //产品进、出缓冲区指针
int tot=0;  //缓冲区中的产品总数

int main(int argc,char **argv){
	pthread_mutex_init(&mutex,NULL); //对互斥信号量进行初始化
	sem_init(&product,0,0);    //对标识产品个数的信号量进行初始化
	sem_init(&warehouse,0,BUFFER_LEN); //对标识缓冲区中空位置个数的信号量进行初始化
	in=0;
	out=0;
	int i0=0,i1=1;
	int clone_flag, retval;
	char *stack;
	clone_flag=CLONE_VM|CLONE_SIGHAND|CLONE_FS|CLONE_FILES;
	//创建两个生产者和两个消费者线程
	stack=(char *)malloc(4096);
	retval=clone((void *)producer,&(stack[4095]),clone_flag,(void *)&i0);
	
	stack=(char *)malloc(4096);
	retval=clone((void *)consumer,&(stack[4095]),clone_flag,(void *)&i0);
	
	stack=(char *)malloc(4096);
	retval=clone((void *)producer,&(stack[4095]),clone_flag,(void *)&i1);
	
	stack=(char *)malloc(4096);
	retval=clone((void *)consumer,&(stack[4095]),clone_flag,(void *)&i1);
	
	exit(1);
	
}

void producer(void *args){
	int id=*((int *)args);
	int i;
	for(i=0;i<10;i++){
		sleep(i+1);
		sem_wait(&warehouse);
		pthread_mutex_lock(&mutex);
		if(id==0)
			strcpy(buffer[in],"aaa\0");
				else
					strcpy(buffer[in],"bbb\0");
						printf("producer %d produces %s in %d\n",id,buffer[in],in);
						in=(in+1)%BUFFER_LEN;
						tot++; //当前产品总数加1
						printf("*****the number of products:%d*****\n",tot); 
						pthread_mutex_unlock(&mutex);
						sem_post(&product);
	}
	printf("producer %d is over!\n",id);
}


void consumer(void *args){
	int id=*((int *)args);
	int i;
	for(i=0;i<10;i++){
		sleep(10-i);
		sem_wait(&product);
		pthread_mutex_lock(&mutex);
		printf("consumer %d get %s in %d\n",id,buffer[out],out);
		out=(out+1)%BUFFER_LEN;
		tot--; //当前产品总数减1
		printf("*****the number of products:%d*****\n",tot); 
		pthread_mutex_unlock(&mutex);
		sem_post(&warehouse);
	}
	printf("consumer %d is over!\n",id);
}

