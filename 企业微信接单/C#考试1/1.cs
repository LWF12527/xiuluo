using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace 超市满减优惠
{
    internal class Program
    {
        static void Main(string[] args)
        { 
            Console.WriteLine("请输入自己的消费金额");
            double money=double.Parse(Console.ReadLine());
            if (money <= 100)
            {
                Console.WriteLine("全额付款",money*1);
            }
            else
            {
                Console.WriteLine("有会员证吗（y/n）?");
    int pd = Console.Read();
    if (pd==89)
      Console.WriteLine("9折",money*0.9);
    else
      Console.WriteLine("9.5折",money*0.95);
            }
            Console.ReadLine();
   Console.WriteLine("学号，班级信息");
        }
    }
}
