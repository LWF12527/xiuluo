#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define MAX_PROCESS 10
#define MAX_PAGES 20
#define PAGE_SIZE 4096

typedef struct PCB {
	int pid; // 进程ID
	int page_table[MAX_PAGES]; // 页面表
	int page_fault; // 页面错误次数
	int status; // 进程状态
} PCB;

typedef struct QueueNode {
	PCB* process; // 进程指针
	struct QueueNode* next; // 下一个节点指针
} QueueNode;

typedef struct Queue {
	QueueNode* front; // 队头指针
	QueueNode* rear; // 队尾指针
} Queue;

typedef struct FreeBlock {
	int start; // 空闲块起始页号
	int length; // 空闲块长度
	struct FreeBlock* next; // 下一个空闲块指针
} FreeBlock;

PCB* create_process(int pid) {
	PCB* process = (PCB*)malloc(sizeof(PCB));
	process->pid = pid;
	process->page_fault = 0;
	process->status = 0; // 就绪状态
	
	// 初始化页面表
	for (int i = 0; i < MAX_PAGES; i++) {
		process->page_table[i] = -1; // -1表示未分配页面
	}
	
	return process;
}

void allocate_memory(PCB* process, int num_pages) {
	// 分配物理块给进程
	int allocated = 0;
	for (int i = 0; i < MAX_PAGES && allocated < num_pages; i++) {
		if (process->page_table[i] == -1) {
			process->page_table[i] = process->pid;
			allocated++;
		}
	}
	
	printf("进程 %d 被分配了 %d 个物理块\n", process->pid, allocated);
}

void deallocate_memory(PCB* process) {
	// 释放进程占用的物理块
	for (int i = 0; i < MAX_PAGES; i++) {
		if (process->page_table[i] == process->pid) {
			process->page_table[i] = -1;
		}
	}
	
	printf("进程 %d 的物理块已回收\n", process->pid);
}

void insert_ready_queue(Queue* ready_queue, PCB* process) {
	// 将进程插入就绪队列尾部
	QueueNode* node = (QueueNode*)malloc(sizeof(QueueNode));
	node->process = process;
	node->next = NULL;
	
	if (ready_queue->rear == NULL) {
		ready_queue->front = node;
		ready_queue->rear = node;
	} else {
		ready_queue->rear->next = node;
		ready_queue->rear = node;
	}
	
	printf("进程 %d 进入就绪队列\n", process->pid);
}

PCB* select_process(Queue* ready_queue) {
	// 从就绪队列选择一个进程调度
	if (ready_queue->front == NULL) {
		return NULL;
	}
	
	QueueNode* node = ready_queue->front;
	ready_queue->front = ready_queue->front->next;
	
	if (ready_queue->front == NULL) {
		ready_queue->rear = NULL;
	}
	
	PCB* process = node->process;
	free(node);
	
	printf("进程 %d 被调度执行\n", process->pid);
	
	return process;
}

void handle_page_fault(PCB* process, Queue* ready_queue, FreeBlock** free_blocks) {
	// 处理页面错误
	int page_fault_addr = rand() % MAX_PAGES; // 随机选择一个页面错误的地址
	process->page_fault++;
	process->status = 2; // 阻塞状态
	
	printf("进程 %d 发生页面错误，地址 %d\n", process->pid, page_fault_addr);
	
	// 页面置换算法：LRU，选择最近最久未使用的页面进行置换
	int victim_page = -1;
	for (int i = 0; i < MAX_PAGES; i++) {
		if (process->page_table[i] == process->pid) {
			if (victim_page == -1) {
				victim_page = i;
			} else if (process->page_table[i] < process->page_table[victim_page]) {
				victim_page = i;
			}
		}
	}
	process->page_table[victim_page] = process->pid;
	
	printf("进程 %d 的页面 %d 被置换出去\n", process->pid, victim_page);
	
	// 空闲块管理算法：位图法，将置换出的页面标记为空闲
	FreeBlock* new_block = (FreeBlock*)malloc(sizeof(FreeBlock));
	new_block->start = victim_page;
	new_block->length = 1;
	new_block->next = NULL;
	
	if (*free_blocks == NULL) {
		*free_blocks = new_block;
	} else {
		FreeBlock* tail = *free_blocks;
		while (tail->next != NULL) {
			tail = tail->next;
		}
		tail->next = new_block;
	}
	
	// 将阻塞的进程放入就绪队列尾部
	insert_ready_queue(ready_queue, process);
	
	printf("进程 %d 被阻塞\n", process->pid);
}

void print_free_blocks(FreeBlock* free_blocks) {
	// 打印空闲块链表
	printf("空闲块链表：");
	FreeBlock* block = free_blocks;
	while (block != NULL) {
		printf("[%d-%d] ", block->start, block->start + block->length - 1);
		block = block->next;
	}
	printf("\n");
}

void print_ready_queue(Queue* ready_queue) {
	// 打印就绪队列
	printf("就绪队列：");
	QueueNode* node = ready_queue->front;
	while (node != NULL) {
		printf("%d ", node->process->pid);
		node = node->next;
	}
	printf("\n");
}

int main() {
	srand(time(NULL));
	
	Queue ready_queue;
	ready_queue.front = NULL;
	ready_queue.rear = NULL;
	
	FreeBlock* free_blocks = NULL;
	
	int num_processes;
	printf("请输入要创建的进程个数：");
	scanf("%d", &num_processes);
	
	// 创建进程
	for (int i = 1; i <= num_processes; i++) {
		PCB* process = create_process(i);
		
		// 分配内存给进程
		int num_pages;
		printf("请输入进程 %d 需要的物理块个数：", process->pid);
		scanf("%d", &num_pages);
		allocate_memory(process, num_pages);
		
		// 将进程插入就绪队列
		insert_ready_queue(&ready_queue, process);
	}
	
	printf("进程创建完成。\n");
	
	printf("开始执行进程...\n");
	
	while (ready_queue.front != NULL) {
		PCB* current_process = select_process(&ready_queue);
		
		// 执行中产生逻辑地址并进行地址重定位
		int logical_address = rand() % MAX_PAGES;
		int physical_address = current_process->page_table[logical_address];
		
		printf("进程 %d 的逻辑地址 %d 映射到物理地址 %d\n", current_process->pid, logical_address, physical_address);
		
		// 模拟页面错误发生
		if (rand() % 10 < 3) { // 产生页面错误的概率为30%
			handle_page_fault(current_process, &ready_queue, &free_blocks);
		}
		
		// 打印空闲块链表
		print_free_blocks(free_blocks);
	}
	
	printf("所有进程执行完毕。\n");
	
	// 打印被阻塞的进程
	QueueNode* node = ready_queue.front;
	while (node != NULL) {
		printf("进程 %d 被阻塞\n", node->process->pid);
		node = node->next;
	}
	
	// 回收内存
	for (int i = 1; i <= num_processes; i++) {
		PCB* process = create_process(i);
		deallocate_memory(process);
	}
	
	printf("内存回收完成。\n");
	
	return 0;
}
