#include <stdio.h>
#include <stdlib.h>
#include <signal.h>
#include <sys/time.h>
#include <unistd.h>
#include <time.h>

#define TOTAL 6 // 子进程数量
#define TIME_SLICE 2 // 时间片长度（秒）

// PCB结构体
struct PCB {
	pid_t pid;                    // 子进程PID
	int state;                    // 状态信息：1-正在运行，0-暂停，-1-结束
	unsigned long runned_time;    // 已运行时间
	unsigned long need_running_time; // 剩余运行时间
};

// 全局PCB数组
struct PCB pcb[TOTAL];
int current = -1; // 当前正在运行的子进程索引

void Dispatch(int signum); // 分派函数声明

// 主函数
int main() {
	srand(time(0)); // 初始化随机种子
	
	// 创建子进程并初始化PCB
	for (int i = 0; i < TOTAL; i++) {
		pid_t pid = fork();
		if (pid < 0) {
			perror("Fork error");
			exit(1);
		} else if (pid == 0) { // 子进程
			while (1) pause(); // 等待SIGCONT信号
			exit(0);
		} else { // 父进程
			pcb[i].pid = pid;
			pcb[i].state = 0; // 初始状态为暂停
			pcb[i].runned_time = 0;
			pcb[i].need_running_time = rand() % 10 + 1; // 剩余运行时间随机生成1-10秒
			kill(pid, SIGSTOP); // 暂停子进程
		}
	}
	
	// 设置定时器
	struct itimerval timer;
	timer.it_value.tv_sec = TIME_SLICE; // 第一次定时器时间
	timer.it_value.tv_usec = 0;
	timer.it_interval.tv_sec = TIME_SLICE; // 定时器间隔时间
	timer.it_interval.tv_usec = 0;
	signal(SIGALRM, Dispatch); // 定时器到时调用分派函数
	setitimer(ITIMER_REAL, &timer, NULL);
	
	// 主循环，检测所有子进程是否结束
	while (1) {
		int all_done = 1;
		for (int i = 0; i < TOTAL; i++) {
			if (pcb[i].state != -1) {
				all_done = 0;
				break;
			}
		}
		if (all_done) break;
		pause(); // 等待信号
	}
	
	printf("All processes are finished.\n");
	return 0;
}
void Dispatch(int signum) {
	// 暂停当前正在运行的子进程
	if (current != -1 && pcb[current].state == 1) {
		kill(pcb[current].pid, SIGSTOP);
		pcb[current].state = 0;
		pcb[current].runned_time += TIME_SLICE;
		
		// 如果剩余时间小于时间片，确保不会出现溢出
		if (pcb[current].need_running_time <= TIME_SLICE) {
			pcb[current].need_running_time = 0; // 将剩余时间置0
			pcb[current].state = -1;           // 状态改为结束
			kill(pcb[current].pid, SIGKILL);  // 结束进程
			printf("Process %d finished.\n", pcb[current].pid);
		} else {
			pcb[current].need_running_time -= TIME_SLICE;
		}
	}
	
	// 查找下一个需要运行的子进程
	for (int i = 0; i < TOTAL; i++) {
		current = (current + 1) % TOTAL; // 轮转查找
		if (pcb[current].state == 0) { // 找到暂停的子进程
			pcb[current].state = 1;
			printf("Process %d is running. Runned time: %lu, Remaining time: %lu\n",
				pcb[current].pid, pcb[current].runned_time, pcb[current].need_running_time);
			kill(pcb[current].pid, SIGCONT); // 恢复子进程运行
			break;
		}
	}
}

