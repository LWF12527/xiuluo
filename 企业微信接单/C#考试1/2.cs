using System;

namespace 第二题
{
    class Program
    {
        static void Main(string[] args)
        {
            int n,i,sum=0;
            Console.Write("请输入一个正整数：\t");
            n = Convert.ToInt32(Console.ReadLine());
            ///i = Convert.ToInt32(Console.ReadLine());
            for (i = 1; i <= n; i++)
            {
                sum = sum + i;
            }
            Console.Write("1 + 2 + 3 + ......+n的值为:\t");
            Console.WriteLine("{0}", sum);
            Console.WriteLine("学号，班级信息");
        }
    }
}