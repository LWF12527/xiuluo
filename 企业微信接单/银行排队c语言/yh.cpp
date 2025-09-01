#include <stdio.h>
#include <stdlib.h>

#define MAX_CUSTOMERS 1000  // 最大客户数
#define MAX_WINDOWS 5      // 窗口数量

// 客户结构体
typedef struct {
	int arrival_time;  // 到达时间
	int leave_time;    // 离开时间
} Customer;

// 队列结构体
typedef struct {
	Customer customers[MAX_CUSTOMERS];
	int front;
	int rear;
} Queue;

// 初始化队列
void initQueue(Queue *q) {
	q->front = 0;
	q->rear = 0;
}

// 判断队列是否为空
int isEmpty(Queue *q) {
	return q->front == q->rear;
}

// 判断队列是否满
int isFull(Queue *q) {
	return (q->rear + 1) % MAX_CUSTOMERS == q->front;
}

// 入队
void enqueue(Queue *q, Customer c) {
	if (isFull(q)) {
		printf("队列已满，无法加入更多客户。\n");
		return;
	}
	q->customers[q->rear] = c;
	q->rear = (q->rear + 1) % MAX_CUSTOMERS;
}

// 出队
Customer dequeue(Queue *q) {
	if (isEmpty(q)) {
		printf("队列为空，无法出队。\n");
		Customer empty = {0, 0};
		return empty;
	}
	Customer c = q->customers[q->front];
	q->front = (q->front + 1) % MAX_CUSTOMERS;
	return c;
}

// 计算队列长度
int queueLength(Queue *q) {
	return (q->rear - q->front + MAX_CUSTOMERS) % MAX_CUSTOMERS;
}

int main() {
	int N = MAX_WINDOWS;  // 设置窗口数量
	Queue windows[MAX_WINDOWS];  // 每个窗口一个队列
	for (int i = 0; i < N; i++) {
		initQueue(&windows[i]);
	}
	
	int open_time, close_time;
	printf("请输入银行开门时间（单位:分钟, 如9点为540）：");
	scanf("%d", &open_time);
	printf("请输入银行关门时间（单位:分钟, 如17点为1020）：");
	scanf("%d", &close_time);
	
	int total_customers = 0;  // 总客户数
	int total_wait_time = 0;  // 总逗留时间
	
	while (1) {
		int arrival_time, service_time;
		printf("请输入客户到达时间（分钟, 输入-1结束）：");
		scanf("%d", &arrival_time);
		if (arrival_time == -1) break;
		
		printf("请输入客户办理业务所需时间（分钟）：");
		scanf("%d", &service_time);
		
		if (arrival_time < open_time || arrival_time >= close_time) {
			printf("客户到达时间不在营业时间内，无法受理。\n");
			continue;
		}
		
		// 找到人数最少的队列
		int min_queue = 0;
		for (int i = 1; i < N; i++) {
			if (queueLength(&windows[i]) < queueLength(&windows[min_queue])) {
				min_queue = i;
			}
		}
		
		// 创建客户
		Customer new_customer;
		new_customer.arrival_time = arrival_time;
		
		// 如果队列空闲，直接办理业务
		if (isEmpty(&windows[min_queue])) {
			new_customer.leave_time = arrival_time + service_time;
		} else {
			Customer last_customer = windows[min_queue].customers[windows[min_queue].rear - 1];
			if (last_customer.leave_time > arrival_time) {
				new_customer.leave_time = last_customer.leave_time + service_time;
			} else {
				new_customer.leave_time = arrival_time + service_time;
			}
		}
		
		// 记录客户逗留时间
		int wait_time = new_customer.leave_time - new_customer.arrival_time;
		total_wait_time += wait_time;
		total_customers++;
		
		// 将客户加入队列
		enqueue(&windows[min_queue], new_customer);
		
		printf("客户已分配到窗口 %d，预计离开时间：%d 分钟。\n", min_queue + 1, new_customer.leave_time);
	}
	
	// 计算平均逗留时间
	if (total_customers > 0) {
		double average_time = (double)total_wait_time / total_customers;
		printf("总客户数：%d\n", total_customers);
		printf("客户在银行逗留的平均时间：%.2f 分钟。\n", average_time);
	} else {
		printf("今天没有客户光临银行。\n");
	}
	
	return 0;
}

