#ifdef HAVE_CONFIG_H
#include<config.h>
#endif

#include<stdio.h>
#include<stdlib.h>
#define MAPSIZE 100

struct map    //空闲区域表项结构
{
	int m_addr;  //空闲区域首址
	int m_size;  //空闲区域长度
};

struct map map[MAPSIZE];     //空闲区域表

//最佳分配算法，mp为空闲区域表的首地址，size为所申请空闲分区的长度
int BF_malloc(struct map *mp,int size) {
	register int a,s;
	register struct map *bp,*bpp;
	for(bp=mp;bp->m_size;bp++) {
		if(bp->m_size>=size) {
			a=bp->m_addr;
			s=bp->m_size;
			for(bpp=bp;bpp->m_size;bpp++) {
				if(bpp->m_size>=size&&bpp->m_size<s) {
					a=bpp->m_addr;
					s=bpp->m_size;
					bp=bpp;
				}
			}
			bp->m_addr+=size;
			if((bp->m_size-=size)==0) {
				do {
					bp++;
					(bp-1)->m_addr=bp->m_addr;
				} while((bp-1)->m_size=bp->m_size);
			}
			// 新增代码，按空闲区域长度从小到大排序
			struct map tmp;
			for (struct map *p = mp; p->m_size; p++) {
				for (struct map *q = p+1; q->m_size; q++) {
					if (p->m_size > q->m_size) {
						tmp = *p;
						*p = *q;
						*q = tmp;
					}
				}
			}
			return(a);
		}
	}
	return(-1);
}

//最坏分配算法 mp为空闲区域表的首地址，size为所申请空闲分区的长度
int WF_malloc(struct map *mp,int size) {
	register int a,s;
	register struct map *bp,*bpp;
	for(bp=mp;bp->m_size;bp++) {
		if(bp->m_size>=size) {
			a=bp->m_addr;
			s=bp->m_size;
			for(bpp=bp;bpp->m_size;bpp++) {
				if(bpp->m_size>s) {
					a=bpp->m_addr;
					s=bpp->m_size;
					bp=bpp;
				}
			}
			bp->m_addr+=size;
			if((bp->m_size-=size)==0) {
				do {
					bp++;
					(bp-1)->m_addr=bp->m_addr;
				} while((bp-1)->m_size=bp->m_size);
			}
			// 新增代码，按空闲区域长度从大到小排序
			struct map tmp;
			for (struct map *p = mp; p->m_size; p++) {
				for (struct map *q = p+1; q->m_size; q++) {
					if (p->m_size < q->m_size) {
						tmp = *p;
						*p = *q;
						*q = tmp;
					}
				}
			}
			return(a);
		}
	}
	return(-1);
}

//分区的释放mp为空闲区域表的首地址, aa为被释放分区的首地址, size为被释放分区的
//长度
void mfree(struct map *mp,int aa,int size)
{
	register struct map *bp;
	register int t;
	register int a;
	a=aa;
	//在空闲区域表中找到首地址大于并且最接近a的空闲分区首地址bp
	for(bp=mp;bp->m_addr<=a&&bp->m_size!=0;bp++);
	if(bp>mp&&(bp-1)->m_addr+(bp-1)->m_size==a)//如果bp-1首地址加上空间长度刚好等
		//于a，即bp-1和a所代表的两空闲分区是相邻的
	{
		(bp-1)->m_size+=size;//将bp-1和a所代表的两空闲分区合并
		//如果a和bp所代表的两空闲分区相邻，则将bp-1,a和bp合并，并将bp后的分区依//次向前移
		if(a+size==bp->m_addr) 
		{  
			(bp-1)->m_size+=bp->m_size;
			while(bp->m_size)
			{
				bp++;
				(bp-1)->m_addr=bp->m_addr;
				(bp-1)->m_size=bp->m_size;
			}
		}
	}
	else{ //若bp-1和a所代表的两空闲分区不相邻
		//若a和bp所代表的两空闲分区相邻，将a和bp合并
		if(a+size==bp->m_addr&&bp->m_size){
			bp->m_addr-=size;
			bp->m_size+=size; 
		}
		else if (size) //否则不合并，将a这一新的空闲分区插入
			do{ 
				t=bp->m_addr;
				bp->m_addr=a;
				a=t;
				t=bp->m_size;
				bp->m_size=size;
				bp++;
			}while(size=t);
	}
}
void init(){   //空闲区域表的初始化
	struct map *bp;
	int addr, size;
	int i=0;
	bp=map;
	printf("please input starting addr and total size(addr,size):");
	scanf("%d, %d", &addr, &size);
	bp->m_addr=addr;
	bp->m_size=size;
	(++bp)->m_size=0;  //表尾
} 

void show_map()  //打印空闲区域表
{
	int i=0;
	struct map *bp;
	bp=map;
	printf("\nCurrent memory map...\n");
	printf("Address \t\tSize");
	while(bp->m_size!=0) {
		printf("<%d\t\t%d>\n",bp->m_addr,bp->m_size);
		bp++;
	}
	printf("\n");
}

main()
{
	int a,s;
	char c;
	int i;
	init();
	
	printf("Please input b for BF, w for WF:");
	getchar();
	scanf("%c",&c);
	
	do
	{
		show_map();
		printf("Please input 1 for request, 2 for release, 0 for exit:");
		scanf("%d",&i);
		switch(i)
{
case 1:
	printf("Please input size:");
	scanf("%d",&s);
	if(c=='b')
		a=BF_malloc(map,s);
	else
		a=WF_malloc(map,s);
	if(a==-1)
		printf("request can't be satisfied\n");
	else
		printf("alloc memory at address:%d,size:%d\n",a,s);
	break; 
case 2:
	printf("Please input addr and size(addr,size):");
	scanf("%d,%d",&a,&s);
	mfree(map,a,s);
	break;
case 0:
	exit(0);
}
	} while(1);
}

