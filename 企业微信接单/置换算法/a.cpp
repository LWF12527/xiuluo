#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define PAGE_SIZE 10          // 每个页面的指令数量
#define NUM_PAGES 32          // 总的虚拟页面数
#define NUM_INSTRUCTIONS 320  // 总的指令数
#define MEMORY_BLOCKS 4       // 内存块数量（最多4个页面）

// 用于模拟不同的页面置换算法
typedef enum { OPT, FIFO, LRU } PageReplacementAlgo;

// 模拟一个页面
typedef struct {
	int page_id;  // 页面号
	int last_used; // LRU 需要的时间戳
} Page;

// 全局变量
int memory[MEMORY_BLOCKS];    // 物理内存（最多4个页面）
int page_fault_count = 0;     // 缺页次数
Page memory_blocks[MEMORY_BLOCKS];  // 页面块（每个块有一个页面）
int instruction_sequence[NUM_INSTRUCTIONS];  // 模拟的指令访问序列

// 打印内存
void print_memory() {
	printf("当前内存状态: ");
	for (int i = 0; i < MEMORY_BLOCKS; i++) {
		printf("%d ", memory_blocks[i].page_id);
	}
	printf("\n");
}

// 初始化内存块
void initialize_memory() {
	for (int i = 0; i < MEMORY_BLOCKS; i++) {
		memory_blocks[i].page_id = -1;  // 设置为无效页编号（如 -1）
		memory_blocks[i].last_used = -1;  // 设置为无效时间戳
	}
}

// 查找内存中是否存在某个页面
int page_exists(int page_id) {
	for (int i = 0; i < MEMORY_BLOCKS; i++) {
		if (memory_blocks[i].page_id == page_id) {
			return i;  // 返回该页面所在的内存块位置
		}
	}
	return -1;  // 页面不在内存中
}

// 置换策略 - FIFO
int fifo_replace() {
	static int next_out = 0;  // 使用静态变量来追踪下一个要被替换的页面
	int victim_page = next_out;
	next_out = (next_out + 1) % MEMORY_BLOCKS;  // 更新下一个要被替换的页面
	return victim_page;
}

// 置换策略 - LRU
int lru_replace() {
	int lru_page = 0;
	for (int i = 1; i < MEMORY_BLOCKS; i++) {
		if (memory_blocks[i].last_used < memory_blocks[lru_page].last_used) {
			lru_page = i;
		}
	}
	return lru_page;
}

// 置换策略 - OPT (最优置换算法)
int opt_replace(int current_instruction, int total_instructions) {
	int farthest = -1;
	int victim_page = -1;
	for (int i = 0; i < MEMORY_BLOCKS; i++) {
		int j;
		for (j = current_instruction + 1; j < total_instructions; j++) {
			if (instruction_sequence[j] / PAGE_SIZE == memory_blocks[i].page_id) {
				break;
			}
		}
		if (j == total_instructions) {
			return i;  // 如果页面在未来不再使用，直接替换
		}
		if (j > farthest) {
			farthest = j;
			victim_page = i;
		}
	}
	return victim_page;
}

// 页面置换操作
void replace_page(PageReplacementAlgo algo, int page_id, int current_instruction, int total_instructions) {
	int victim_page;
	if (algo == FIFO) {
		victim_page = fifo_replace();
	} else if (algo == LRU) {
		victim_page = lru_replace();
	} else if (algo == OPT) {
		victim_page = opt_replace(current_instruction, total_instructions);
	}
	
	// 打印页面替换信息
	printf("页面替换: 被替换页面 %d, 新加载页面 %d\n", memory_blocks[victim_page].page_id, page_id);
	
	// 替换页面
	memory_blocks[victim_page].page_id = page_id;
	memory_blocks[victim_page].last_used = current_instruction;
	page_fault_count++;
	print_memory();
}

// 模拟指令执行
void execute_instructions(PageReplacementAlgo algo) {
	int current_instruction = 0;
	int instruction_count = 0;
	
	while (instruction_count < NUM_INSTRUCTIONS) {
		// 确保 current_instruction 在 [0, NUM_INSTRUCTIONS - 1] 范围内
		current_instruction = current_instruction % NUM_INSTRUCTIONS;
		
		int page_id = instruction_sequence[current_instruction] / PAGE_SIZE;
		
		// 检查页面是否已在内存中
		int page_index = page_exists(page_id);
		if (page_index != -1) {
			// 页面已经在内存中
			printf("指令 %d 已加载，物理地址: %d\n", instruction_sequence[current_instruction], current_instruction);
			memory_blocks[page_index].last_used = instruction_count;
		} else {
			// 页面不在内存，缺页
			printf("缺页: 访问指令 %d, 页面 %d\n", instruction_sequence[current_instruction], page_id);
			if (page_fault_count < MEMORY_BLOCKS) {
				// 空间足够，直接加载
				memory_blocks[page_fault_count].page_id = page_id;
				memory_blocks[page_fault_count].last_used = instruction_count;
				page_fault_count++;
				print_memory();
			} else {
				// 发生页面置换
				replace_page(algo, page_id, current_instruction, NUM_INSTRUCTIONS);
			}
		}
		
		instruction_count++;
		
		// 根据访问模式生成下一条指令
		int random_choice = rand() % 100;  // 生成0到99之间的随机数
		if (random_choice < 50) {
			// 50%的指令是顺序执行的
			current_instruction = (current_instruction + 1) % NUM_INSTRUCTIONS;
		} else if (random_choice < 75) {
			// 25%的指令是均匀分布在前地址(低地址)部分
			current_instruction = rand() % (NUM_INSTRUCTIONS / 4);
		} else {
			// 25%的指令是均匀分布在后地址(高地址)部分
			current_instruction = (rand() % (NUM_INSTRUCTIONS / 4)) + (NUM_INSTRUCTIONS * 3 / 4);
		}
	}
}

// 生成随机的指令访问序列
void generate_instruction_sequence() {
	srand(time(NULL));
	for (int i = 0; i < NUM_INSTRUCTIONS; i++) {
		instruction_sequence[i] = rand() % (NUM_PAGES * PAGE_SIZE);
	}
}

// 主函数
int main() {
	initialize_memory();  // 初始化内存
	generate_instruction_sequence();
	
	printf("选择页面置换算法:\n1. FIFO\n2. LRU\n3. OPT\n选择：");
	int choice;
	scanf("%d", &choice);
	
	PageReplacementAlgo algo;
	switch (choice) {
		case 1: algo = FIFO; break;
		case 2: algo = LRU; break;
		case 3: algo = OPT; break;
		default: 
		printf("无效选择，使用默认算法 FIFO\n"); 
		algo = FIFO;
	}
	
	printf("模拟开始...\n");
	execute_instructions(algo);
	
	// 输出结果
	printf("\n模拟结束！\n");
	printf("缺页次数：%d\n", page_fault_count);
	printf("缺页率：%.2f%%\n", (float)page_fault_count / NUM_INSTRUCTIONS * 100);
	
	return 0;
}
