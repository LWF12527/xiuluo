using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace program01
{
    
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        class MyMath
    {
       public const double PI = 3.14159;
        public static double Perimeter(double r)
        {
            double p= 2 * PI * r;
            return p;
        }
        public static double Area(double r)
        {
            double a= r * r * PI;
            return a;
        }
        public  double Voloume(double r)
        {
            double v= 4 * PI * r * r * r / 3;
            return v;
        }
    }
        private void button1_Click(object sender, EventArgs e)
        {

            double r;
            MyMath v = new MyMath();
            r = Convert.ToDouble(textBox1.Text);
            textBox2.Text = Convert.ToString(MyMath.Perimeter(r));
            textBox3.Text = Convert.ToString(MyMath.Area(r));
            textBox4.Text = Convert.ToString(v.Voloume(r));
        }

        private void button2_Click(object sender, EventArgs e)
        {
            textBox1.Text = "";
            textBox2.Text = "";
            textBox3.Text = "";
            textBox4.Text = "";
	  textBox5.Text = "学生班级信息";
        }
    }
}

