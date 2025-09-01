#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <semaphore.h>
#include <unistd.h>

#define N 5

// 读者和写者的互斥信号量
sem_t mutex, write_mutex;

// 当前读者数量
int read_count = 0;

// 共享数据
int data = 0;

// 读者线程函数
void *reader(void *arg) {
	int id = *(int *) arg;
	while (1) {
		// 申请读者互斥信号量
		sem_wait(&mutex);

		// 读者数量加1
		read_count++;

		// 若是第一个读者，则申请写者互斥信号量
		if (read_count == 1) {
			sem_wait(&write_mutex);
		}

		// 释放读者互斥信号量
		sem_post(&mutex);

		// 读取共享数据
		printf("Reader %d read data: %d\n", id, data);

		// 申请读者互斥信号量
		sem_wait(&mutex);

		// 读者数量减1
		read_count--;

		// 若是最后一个读者，则释放写者互斥信号量
		if (read_count == 0) {
			sem_post(&write_mutex);
		}

		// 释放读者互斥信号量
		sem_post(&mutex);

		// 模拟读操作的耗时
		sleep(rand() % 3);
	}

	pthread_exit(NULL);
}

// 写者线程函数
void *writer(void *arg) {
	int id = *(int *) arg;
	while (1) {
		// 申请写者互斥信号量
		sem_wait(&write_mutex);

		// 修改共享数据
		data++;
		printf("Writer %d write data: %d\n", id, data);

		// 释放写者互斥信号量
		sem_post(&write_mutex);

		// 模拟写操作的耗时
		sleep(rand() % 3);
	}

	pthread_exit(NULL);
}

// 初始化信号量函数
void init_semaphores() {
	// 初始化读者互斥信号量
	sem_init(&mutex, 0, 1);

	// 初始化写者互斥信号量
	sem_init(&write_mutex, 0, 1);
}

// 创建读者线程函数
void create_reader_threads(pthread_t *readers, int *reader_ids) {
	int i;
	for (i = 0; i < N; i++) {
		reader_ids[i] = i + 1;
		pthread_create(&readers[i], NULL, reader, (void *) &reader_ids[i]);
	}
}

// 创建写者线程函数
void create_writer_threads(pthread_t *writers, int *writer_ids) {
	int i;
	for (i = 0; i < N; i++) {
		writer_ids[i] = i + 1;
		pthread_create(&writers[i], NULL, writer, (void *) &writer_ids[i]);
	}
}

// 等待线程结束函数
void wait_for_threads(pthread_t *threads) {
	int i;
	for (i = 0; i < N; i++) {
		pthread_join(threads[i], NULL);
	}
}

// 销毁信号量函数
void destroy_semaphores() {
	// 销毁读者互斥信号量
	sem_destroy(&mutex);

	// 销毁写者互斥信号量
	sem_destroy(&write_mutex);
}

// 主函数
int main() {
	pthread_t readers[N], writers[N];
	int reader_ids[N], writer_ids[N];

	// 初始化信号量
	init_semaphores();

	// 创建读者线程
	create_reader_threads(readers, reader_ids);

	// 创建写者线程
	create_writer_threads(writers, writer_ids);

	// 等待线程结束
	wait_for_threads(readers);
	wait_for_threads(writers);

	// 销毁信号量
	destroy_semaphores();

	return 0;
}
