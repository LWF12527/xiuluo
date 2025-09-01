
#include <iostream>
#include <vector>
#include <cmath>

// 计算矩阵的转置
std::vector<std::vector<double>> transpose(const std::vector<std::vector<double>>& matrix) {
	int rows = matrix.size();
	int cols = matrix[0].size();
	
	std::vector<std::vector<double>> result(cols, std::vector<double>(rows));
	
	for (int i = 0; i < rows; i++) {
		for (int j = 0; j < cols; j++) {
			result[j][i] = matrix[i][j];
		}
	}
	
	return result;
}

// 计算矩阵的乘法
std::vector<std::vector<double>> matrixMultiply(const std::vector<std::vector<double>>& matrix1, const std::vector<std::vector<double>>& matrix2) {
	int rows1 = matrix1.size();
	int cols1 = matrix1[0].size();
	int cols2 = matrix2[0].size();
	
	std::vector<std::vector<double>> result(rows1, std::vector<double>(cols2, 0.0));
	
	for (int i = 0; i < rows1; i++) {
		for (int j = 0; j < cols2; j++) {
			for (int k = 0; k < cols1; k++) {
				result[i][j] += matrix1[i][k] * matrix2[k][j];
			}
		}
	}
	
	return result;
}

// 最小二乘法拟合函数
void leastSquaresFit(const std::vector<double>& x1, const std::vector<double>& x2, const std::vector<double>& x3,
	const std::vector<double>& y, std::vector<double>& coefficients) {
		int n = x1.size(); // 数据点数量
		
		// 构造系数矩阵A和观测矩阵b
		std::vector<std::vector<double>> A(n, std::vector<double>(4));
		std::vector<double> b(n);
		
		for (int i = 0; i < n; i++) {
			double xi1 = x1[i];
			double xi2 = x2[i];
			double xi3 = x3[i];
			double yi = y[i];
			
			A[i][0] = xi1 * xi1 * xi1; // x1^3
			A[i][1] = xi2 * xi2 * xi2; // x2^3
			A[i][2] = xi3 * xi3 * xi3; // x3^3
			A[i][3] = 1.0;             // 常数项
			
			b[i] = yi;
		}
		
		// 使用最小二乘法求解
		std::vector<std::vector<double>> AT = transpose(A);
		std::vector<std::vector<double>> ATA = matrixMultiply(AT, A);
		std::vector<std::vector<double>> ATAInverse(n, std::vector<double>(n, 0.0));
		
		// 计算广义逆
		for (int i = 0; i < n; i++) {
			ATAInverse[i][i] = 1.0 / ATA[i][i];
		}
		
		std::vector<std::vector<double>> ATAInverseAT = matrixMultiply(ATAInverse, AT);
		
		std::vector<double> result = matrixMultiply(ATAInverseAT, b);
		
		// 将结果保存在coefficients向量中
		coefficients = result;
	}

int main() {
	// 输入数据点
	std::vector<double> x1 = {0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0,
		1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0,
		2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 3.0,
		3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 3.8, 3.9, 4.0,
		4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 4.8, 4.9, 5.0,
		5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 5.7, 5.8, 5.9, 6.0,
		6.1, 6.2, 6.3, 6.4, 6.5, 6.6, 6.7, 6.8, 6.9, 7.0,
		7.1, 7.2, 7.3, 7.4, 7.5, 7.6, 7.7, 7.8, 7.9, 8.0,
		8.1, 8.2, 8.3, 8.4, 8.5, 8.6, 8.7, 8.8, 8.9, 9.0,
		9.1, 9.2, 9.3, 9.4, 9.5, 9.6, 9.7, 9.8, 9.9, 495.0};
	
	std::vector<double> x2 = {0.2, 0.5, 0.8, 1.1, 1.4, 1.7, 2.0, 2.3, 2.6, 2.9,
		3.2, 3.5, 3.8, 4.1, 4.4, 4.7, 5.0, 5.3, 5.6, 5.9,
		6.2, 6.5, 6.8, 7.1, 7.4, 7.7, 8.0, 8.3, 8.6, 8.9,
		9.2, 9.5, 9.8, 10.1, 10.4, 10.7, 11.0, 11.3, 11.6, 11.9,
		12.2, 12.5, 12.8, 13.1, 13.4, 13.7, 14.0, 14.3, 14.6, 14.9,
		15.2, 15.5, 15.8, 16.1, 16.4, 16.7, 17.0, 17.3, 17.6, 17.9,
		18.2, 18.5, 18.8, 19.1, 19.4, 19.7, 20.0, 20.3, 20.6, 20.9,
		21.2, 21.5, 21.8, 22.1, 22.4, 22.7, 23.0, 23.3, 23.6, 23.9,
		24.2, 24.5, 24.8, 25.1, 25.4, 25.7, 26.0, 26.3, 26.6, 26.9,
		27.2, 27.5, 27.8, 28.1, 28.4, 28.7, 29.0, 29.3, 29.6, 1475.1};
	
	std::vector<double> x3 = {0.1, 0.3, 0.5, 0.7, 0.9, 1.1, 1.3, 1.5, 1.7, 1.9,
		2.1, 2.3, 2.5, 2.7, 2.9, 3.1, 3.3, 3.5, 3.7, 3.9,
		4.1, 4.3, 4.5, 4.7, 4.9, 5.1, 5.3, 5.5, 5.7, 5.9,
		6.1, 6.3, 6.5, 6.7, 6.9, 7.1, 7.3, 7.5, 7.7, 7.9,
		8.1, 8.3, 8.5, 8.7, 8.9, 9.1, 9.3, 9.5, 9.7, 9.9,
		10.1, 10.3, 10.5, 10.7, 10.9, 11.1, 11.3, 11.5, 11.7, 11.9,
		12.1, 12.3, 12.5, 12.7, 12.9, 13.1, 13.3, 13.5, 13.7, 13.9,
		14.1, 14.3, 14.5, 14.7, 14.9, 15.1, 15.3, 15.5, 15.7, 15.9,
		16.1, 16.3, 16.5, 16.7, 16.9, 17.1, 17.3, 17.5, 17.7, 17.9,
		18.1, 18.3, 18.5, 18.7, 18.9, 19.1, 19.3, 19.5, 19.7, 980.1};
	
	std::vector<double> y = {0.113277442, 1.013572809, 2.326824575, 4.002359214, 6.028424911,
		8.402679947, 11.12640979, 14.20264113, 17.63535586, 21.42910977,
		25.58882711, 30.11968108, 35.02701992, 40.31631904, 45.99314878,
		52.06315199, 58.53202794, 65.40552061, 72.68940986, 80.38950483,
		88.51163869, 97.06166465, 106.0454527, 115.4688872, 125.3378644,
		135.6582912, 146.4360835, 157.6771649, 169.3874659, 181.5729232,
		194.2394786, 207.3930786, 221.0396742, 235.1852197, 249.8356731,
		264.9969954, 280.6751501, 296.8761033, 313.6058235, 330.8702809,
		348.6754479, 367.0272983, 385.9318067, 405.3959479, 425.4266974,
		446.0310301, 467.2159213, 488.9883469, 511.3552826, 534.3237031,
		557.9005832, 582.0928974, 606.9076201, 632.3517258, 658.4321897,
		685.1559872, 712.5300936, 740.5614841, 769.2571339, 798.6240183,
		828.6691124, 859.3993915, 890.8218308, 922.9434056, 955.7710911,
		989.3118625, 1023.572694, 1058.56056, 1094.282435, 1130.74529,
		1167.956097, 1205.92183, 1244.649461, 1284.146954, 1324.421272,
		1365.479377, 1407.328232, 1450.974799, 1496.42604, 1543.688917,
		1592.77039, 1643.677422, 1696.416974, 1751.996009, 1808.421489,
		1867.700377, 1929.839634, 1994.846222, 2062.727105, 2133.489244,
		2207.139602, 2283.685143, 2363.132829, 2445.489624, 2530.762491};
	
	std::vector<double> coefficients;
	
	// 使用最小二乘法拟合
	leastSquaresFit(x1, x2, x3, y, coefficients);
	
	// 打印结果
	std::cout << "拟合结果：" << std::endl;
	std::cout << "x1^3 coefficient: " << coefficients[0] << std::endl;
	std::cout << "x2^3 coefficient: " << coefficients[1] << std::endl;
	std::cout << "x3^3 coefficient: " << coefficients[2] << std::endl;
	std::cout << "constant coefficient: " << coefficients[3] << std::endl;
	
	return 0;
}
