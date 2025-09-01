#include <math.h>
#include<stdio.h>
#include<stdlib.h>
#define PI 3.1415926
#define SAMPLENUMBER 2048
void InitForFFT();
void FFT(float dataR[SAMPLENUMBER], float dataI[SAMPLENUMBER],int pointNum);
void Smooth(int data[], int size, int N);
float maxVal = 0;
int INPUT[SAMPLENUMBER];
float  DATA[SAMPLENUMBER];
float fWaveR[SAMPLENUMBER], fWaveI[SAMPLENUMBER], w[SAMPLENUMBER];
float sin_tab[SAMPLENUMBER], cos_tab[SAMPLENUMBER];
void main() {
    InitForFFT();
    FILE* fp;            /*文件指针*/
    if ((fp = fopen("data_10uf.txt", "r")) == NULL)//两组数据:data_01uf.txt、data_10uf.txt
    {
        perror("fail to read");
        exit(1);
    }
    for (int i = 0; i < SAMPLENUMBER; i++) {
        fscanf(fp, "%d ", &INPUT[i]);//初始化实部
    }
    //求最大值
    for (int i = 0; i < SAMPLENUMBER; i++) {
        if (INPUT[i] > maxVal) {
            maxVal = INPUT[i];
        }
    }
    //初始化虚部
    for (int i = 0; i < SAMPLENUMBER; i++) {
        fWaveR[i] = INPUT[i] / maxVal;//归一化
        fWaveI[i] = 0.0f;
        w[i] = 0.0f;
    }

    FFT(fWaveR, fWaveI, SAMPLENUMBER);//作傅里叶变换
    //输出的幅值数据
    for (int i = 0; i < SAMPLENUMBER; i++) {
        DATA[i] = w[i];
        // printf("%2f,", DATA[i]);
    }
    printf("最大幅值:%f\n", DATA[0]* maxVal);

    DATA[0] = 0;//直流分量置0
    //计算基频及对应幅值
        //1.计算最大值
    float maxVal1 = 0, R1, A1;
    int MAXIndex, K01;
    for (int i = 0; i < SAMPLENUMBER; i++) {
        if (DATA[i] > maxVal1) {
            maxVal1 = DATA[i];
            MAXIndex = i;
        }
    }
    printf("最大值及位置:%f,%d\n", DATA[MAXIndex]* maxVal, MAXIndex);
    if (DATA[MAXIndex - 1] > DATA[MAXIndex + 1]) {
        A1 = DATA[MAXIndex - 1] / DATA[MAXIndex];
        R1 = 1 / (1 + A1);
        K01 = MAXIndex - 1;
    }
    else {
        A1 = DATA[MAXIndex] / DATA[MAXIndex + 1];
        R1 = 1 / (1 + A1);
        K01 = MAXIndex;
    }
    int N = SAMPLENUMBER, fs = 3720.23809523;
    float Fn, An;
    Fn = (K01+1 + R1 - 1) * fs / N;//基波频率
    An = 2 * PI * R1 * DATA[K01] / (N * sin(R1 * PI));//基波幅值
    printf("基波(频率,幅值):%f,%f", Fn,An* maxVal);
    //平滑滤波
    int Num = 12;//滑动窗口大小
    Smooth(INPUT,SAMPLENUMBER, Num);
    //滤波后的数据
    //for (int i = 0; i < SAMPLENUMBER; i++) {
    //    printf("%d,", INPUT[i]);
    //}

}


void FFT(float dataR[SAMPLENUMBER], float dataI[SAMPLENUMBER],int pointNum) {
    int x0, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10,x11, xx;
    int i, j, k, b, p, L,mm1;
    float TR, TI, temp;
    for (i = 0; i < SAMPLENUMBER; i++) {
        x0 = x1 = x2 = x3 = x4 = x5 = x6 = x7 = x8 = x9 = x10 =x11= 0;
        x0 = i & 0x01;
        x1 = (i / 2) & 0x01;
        x2 = (i / 4) & 0x01;
        x3 = (i / 8) & 0x01;
        x4 = (i / 16) & 0x01;
        x5 = (i / 32) & 0x01;
        x6 = (i / 64) & 0x01;
        x7 = (i / 128) & 0x01;
        x8 = (i / 256) & 0x01;
        x9 = (i / 512) & 0x01;
        x10 = (i / 1024) & 0x01;
        x11 = (i / 2048) & 0x01;
        if (pointNum == 4096) {
            mm1 = 12;
            xx = x0 * 2048 + x1* 1024 + x2 * 512 + x3 * 256 + x4 * 128 + x5 * 64 + x6 * 32 + x7 * 16 + x8 * 8 + x9 * 4 + x10 * 2 + x11;
        }else  if (pointNum == 2048) {
            mm1 = 11;
            xx = x0 * 1024 + x1 * 512 + x2 * 256 + x3 * 128 + x4 * 64 + x5 * 32 + x6 * 16 + x7 * 8 + x8 * 4 + x9 * 2 + x10;
        }
        else if(pointNum == 1024) {
            mm1 = 10;
            xx = x0 * 512 + x1 * 256 + x2 * 128 + x3 * 64 + x4 * 32 + x5 * 16 + x6 * 8 + x7 * 4 + x8 * 2 + x9;
        }
        else if (pointNum == 256) {
            mm1 = 9;
            xx = x0 * 256 + x1 * 128 + x2 * 64 + x3 * 32 + x4 * 16 + x5 * 8 + x6 * 4 + x7 * 2 + x8;
        }                
        dataI[xx] = dataR[i];
    }
    for (i = 0; i < SAMPLENUMBER; i++) {
        dataR[i] = dataI[i];
        dataI[i] = 0;
    }
    for (L = 1; L <= mm1; L++) {
        b = 1; i = L - 1;
        while (i > 0) {
            b = b * 2; i--;
        }
        for (j = 0; j <= b - 1; j++) {
            p = 1; i = mm1 - L;
            while (i > 0) {
                p = p * 2; i--;
            }
            p = p * j;
            for (k = j; k < SAMPLENUMBER; k = k + 2 * b) {
                TR = dataR[k];
                TI = dataI[k];
                temp = dataR[k + b];
                dataR[k] = dataR[k] + dataR[k + b] * cos_tab[p] + dataI[k + b] * sin_tab[p];
                dataI[k] = dataI[k] - dataR[k + b] * sin_tab[p] + dataI[k + b] * cos_tab[p];
                dataR[k + b] = TR - dataR[k + b] * cos_tab[p] - dataI[k + b] * sin_tab[p];
                dataI[k + b] = TI + temp * sin_tab[p] - dataI[k + b] * cos_tab[p];
            }
        }
    }
    for (i = 0; i < SAMPLENUMBER; i++) {
        w[i] = sqrt(dataR[i] * dataR[i] + dataI[i] * dataI[i]);
    }
}
void InitForFFT() {
    int i;
    for (i = 0; i < SAMPLENUMBER; i++) {
        sin_tab[i] = sin(PI * 2 * i / SAMPLENUMBER);
        cos_tab[i] = cos(PI * 2 * i / SAMPLENUMBER);
    }
}

void Smooth(int data[],int size,int N)
{
//N:平均点数
//size:数据尺寸
//data：数据
    int Sum1 = 0;
    for (int j = 0; j < size; j++)
    {
        if (j < N / 2)
        {
            for (int k = 0; k < N; k++)
            {
                Sum1 += data[j + k];
            }
            data[j] = Sum1 / N;
        }
        else
            if (j < size - N / 2)
            {
                for (int k = 0; k < N / 2; k++)
                {
                    Sum1 += (data[j + k] + data[j - k]);
                }
                data[j] = Sum1 / N;
            }
            else
            {
                for (int k = 0; k < size - j; k++)
                {
                    Sum1 += data[j + k];
                }
                for (int k = 0; k < (N - size + j); k++)
                {
                    Sum1 += data[j - k];
                }
                data[j] = Sum1 / N;
            }
        Sum1 = 0;
    }
}

