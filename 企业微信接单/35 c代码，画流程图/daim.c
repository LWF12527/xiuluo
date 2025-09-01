#include <stdio.h>
#include <stdlib.h>

#define MAX_SIZE 100

// 客户结构体
typedef struct {
    int id; // 客户编号
    int type; // 客户类型：0表示个人业务，1表示公司业务
} Customer;

// 队列结构体
typedef struct {
    Customer data[MAX_SIZE]; // 存储数据的数组
    int front; // 队头指针
    int rear; // 队尾指针
} Queue;

// 初始化队列
void initQueue(Queue *q) {
    q->front = q->rear = 0;
}

// 判断队列是否为空
int isQueueEmpty(Queue *q) {
    return q->front == q->rear;
}

// 判断队列是否已满
int isQueueFull(Queue *q) {
    return (q->rear + 1) % MAX_SIZE == q->front;
}

// 入队操作
void enqueue(Queue *q, Customer c) {
    if (isQueueFull(q)) {
        printf("队列已满，无法入队！\n");
        return;
    }
    q->data[q->rear] = c;
    q->rear = (q->rear + 1) % MAX_SIZE;
}

// 出队操作
Customer dequeue(Queue *q) {
    if (isQueueEmpty(q)) {
        printf("队列为空，无法出队！\n");
        exit(1);
    }
    Customer c = q->data[q->front];
    q->front = (q->front + 1) % MAX_SIZE;
    return c;
}

// 显示队列中的所有元素
void displayQueue(Queue *q) {
    if (isQueueEmpty(q)) {
        printf("队列为空！\n");
        return;
    }
    printf("当前队列中有以下客户：\n");
    int i = q->front;
    while (i != q->rear) {
        printf("编号：%d，类型：%s\n", q->data[i].id, q->data[i].type == 0 ? "个人业务" : "公司业务");
        i = (i + 1) % MAX_SIZE;
    }
}

int main() {
    Queue personalQ, companyQ;
    initQueue(&personalQ);
    initQueue(&companyQ);
    int nextId = 1; // 下一个客户的编号从1开始
    
    while (1) {
        // 输出提示信息，等待用户输入
        printf("请输入操作序号：\n");
        printf("1. 新客户（个人业务）\n");
        printf("2. 新客户（公司业务）\n");
        printf("3. 服务完成\n");
        printf("4. 显示当前队列\n");
        printf("5. 添加录入个人业务客户\n");
        printf("6. 添加录入公司业务客户\n");
        printf("7. 退出程序\n");
        
        int choice;
        scanf("%d", &choice);
        
        switch (choice) {
            case 1: { // 新客户（个人业务）
                printf("请稍等，正在为您分配排队号...\n");
                Customer c = {nextId++, 0};
                enqueue(&personalQ, c);
                printf("已为您分配排队号：%d，前面还有%d个人。\n", c.id, personalQ.rear - personalQ.front - 1);
                break;
            }
            case 2: { // 新客户（公司业务）
                printf("请稍等，正在为您分配排队号...\n");
                Customer c = {nextId++, 1};
                enqueue(&companyQ, c);
                printf("已为您分配排队号：%d，前面还有%d个人。\n", c.id, companyQ.rear - companyQ.front - 1);
                break;
            }
            case 3: { // 服务完成
                if (!isQueueEmpty(&personalQ)) {
                    printf("请%d号客户到1号窗口办理业务。\n", personalQ.front + 1);
                    dequeue(&personalQ);
                } else if (!isQueueEmpty(&companyQ)) {
                    printf("请%d号客户到2号窗口办理业务。\n", companyQ.front + 1);
                    dequeue(&companyQ);
                } else
            {
                    printf("当前没有客户在排队！\n");
                }
                break;
            }
            case 4: { // 显示当前队列
                printf("个人业务队列：\n");
                displayQueue(&personalQ);
                printf("公司业务队列：\n");
                displayQueue(&companyQ);
                break;
            }
            case 5: { // 添加录入个人业务客户
                printf("请输入客户编号：");
                int id;
                scanf("%d", &id);
                Customer c = {id, 0};
                enqueue(&personalQ, c);
                printf("已成功添加录入个人业务客户，排队号为：%d，前面还有%d个人。\n", c.id, personalQ.rear - personalQ.front - 1);
                break;
            }
            case 6: { // 添加录入公司业务客户
                printf("请输入客户编号：");
                int id;
                scanf("%d", &id);
                Customer c = {id, 1};
                enqueue(&companyQ, c);
                printf("已成功添加录入公司业务客户，排队号为：%d，前面还有%d个人。\n", c.id, companyQ.rear - companyQ.front - 1);
                break;
            }
            case 7: { // 退出程序
                printf("谢谢使用，再见！\n");
                exit(0);
            }
            default: {
                printf("无效的操作序号，请重新输入！\n");
                break;
            }
        }
    }
    
    return 0;
}