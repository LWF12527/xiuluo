#include<iostream>
#include<cmath>
#include<algorithm>
using namespace std;
struct Quadratic {
	//数据a**x+b*x+c
	double a = 0, b = 0, c = 0;
	//初始化数据成员 a,b 和 c，每个成员默认值为0
	void InitQuadratic(Quadratic &q, double aa, double bb, double cc) {
		a = aa;
		b = bb;
		c = cc;
	}
	//做两个多项式加法，即对应系数相加，返回相加结果。
	Quadratic Add(Quadratic q1, Quadratic q2) {
		Quadratic q;
		q.a = q1.a + q2.a;
		q.b = q1.b + q2.b;
		q.c = q1.c + q2.c;
		return q;
	}
	//根据给定的 x 值，计算多项式的值并返回
	double Eval(Quadratic q, double x) {
		return q.a * pow(x, 2) + q.b * x + q.c;
	}
	//计算方程两个实根并输出。
	void Root(Quadratic q) {
		double delta = q.b * q.b - 4 * q.a * q.c;
		if (delta < 0)
			cout << "此方程无解" << endl;
		else {
			double R1 = (-q.b + sqrt(delta)) / (2 * q.a);
			double R2 = (-q.b - sqrt(delta)) / (2 * q.a);
			if (R1 < R2)
				swap(R1, R2);
			cout << "方程的两个实根是：" << endl;
			cout << "R1：" << R1 << endl;
			cout << "R2：" << R2 << endl;
		}
	}
	//按照 ax**2+bx+c 的格式输出二次多项式，在输出时要注意去掉系数为 0 的项，并且当
	//b 或 c 的值为负数时，其前不能出现加号。
	void Print(Quadratic q) {
		cout << q.a << "**x";
		if (q.b > 0)
			cout << "+" << q.b << "*x";
		else if(q.b < 0)
			cout << q.b << "*x";
		if (q.c > 0)
			cout << "+" << q.c;
		else if(q.c < 0)
			cout << q.c;
		cout << endl;
	}
};

int main() {
	// qu是所求方程根的方程1
	Quadratic qu, qu1, qu2;
	// 输入数据
	double a1, b1, c1, a2, b2, c2;
	cout << "输入方程Q1的数据a1, b1, c1：";
	cin >> a1 >> b1 >> c1;
	cout << "输入方程Q2的数据a2, b2, c2：";
	cin >> a2 >> b2 >> c2;
	cout << endl;
	// 初始化数据
	qu1.InitQuadratic(qu1, a1, b1, c1);
	qu2.InitQuadratic(qu2, a2, b2, c2);
	// 合并方程
	qu = qu.Add(qu1, qu2);
	// 打印方程
	cout << "Q1:";
	qu1.Print(qu1);
	cout << "Q2:";
	qu2.Print(qu2);
	cout << "Q3=Q1+Q2:";
	qu.Print(qu);
	// 输出含x的结果
	double x = 0;
	cout<<"输入x的值:";
	cin>>x;
	cout<<endl;
	cout << "Q1(x)=" << qu1.Eval(qu1, x) << endl;
	cout << "Q2(x)=" << qu2.Eval(qu2, x) << endl;
	cout << "Q3(x)=" << qu.Eval(qu, x) << endl;
	// 输出Q3多项式的根
	qu.Root(qu);
	return 0;
}
