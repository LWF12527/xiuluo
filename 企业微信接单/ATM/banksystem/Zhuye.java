package banksystem;

import javax.swing.*;
import javax.sound.sampled.*;//播放音频的包
import java.awt.*;
import java.awt.event.*;
import java.io.*;
public class Zhuye extends JFrame {
	static JFrame z=new JFrame();//实现一个窗体
	@SuppressWarnings("removal")
	public Zhuye(){
		setTitle("ATM管理系统");
		setBounds(370,190,800,500);
		setVisible(true);
		setResizable(false);
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);//结束程序
		setLayout(null);

		//修改窗体图标
		Toolkit tk=Toolkit.getDefaultToolkit();
		Image img=tk.getImage("bank/tb.jpg");//登入成功关闭登录窗口，找图标和背景图片
		setIconImage(img);
		//背景图片
		ImageIcon t1=new ImageIcon("bank/zy.jpg");
		JLabel label0=new JLabel(t1);
		label0.setSize(t1.getIconWidth(),t1.getIconHeight());
		add(label0);
		JPanel pan=(JPanel) getContentPane();
		getLayeredPane().add(label0,new Integer(Integer.MIN_VALUE));//见标签面板设置为最底层面板
		pan.setOpaque(false);

		JLabel hy=new JLabel("欢迎使用ATM管理系统");
		Font font=new Font("楷体",Font.BOLD,40);
		hy.setFont(font);
		JButton button1=new JButton("取    款");
		JButton button2=new JButton("修改密码");
		JButton button3=new JButton("存    款");
		JButton button4=new JButton("显示余额");
		JButton button5=new JButton("转    账");
		JButton button6=new JButton("查询修改");
		JButton button7=new JButton("退  出");
		JButton button8=new JButton("注  销");
		//将按钮透明
		Shujuk.touming a = new Shujuk.touming();//将类放在了Shujuk里
		a.touming(button1);
		a.touming(button2);
		a.touming(button3);
		a.touming(button4);
		a.touming(button5);
		a.touming(button6);
		a.touming(button7);
		a.touming(button8);

		zy h=new zy();
		button1.addActionListener(h);
		button2.addActionListener(h);
		button3.addActionListener(h);
		button4.addActionListener(h);
		button5.addActionListener(h);
		button6.addActionListener(h);
		button7.addActionListener(h);
		button8.addActionListener(h);

		hy.setBounds(200,0,500,60);
		add(hy);
		button1.setBounds(150,70,150,40);
		add(button1);
		button2.setBounds(500,70,150,40);
		add(button2);
		button3.setBounds(150,170,150,40);
		add(button3);
		button4.setBounds(500,170,150,40);
		add(button4);
		button5.setBounds(150,270,150,40);
		add(button5);
		button6.setBounds(500,270,150,40);
		add(button6);
		button7.setBounds(220,370,130,40);
		add(button7);
		button8.setBounds(450,370,130,40);
		add(button8);
		setVisible(true);
	}

	public class zy implements ActionListener {
		public void actionPerformed (ActionEvent e) {
			if(e.getActionCommand()=="取    款")
				new Qukuan(z,"取款业务");
			else if(e.getActionCommand()=="修改密码")
				new Gaimi(z,"修改密码");
			else if(e.getActionCommand()=="存    款")
				new Cunkuan(z,"存款业务");
			else if(e.getActionCommand()=="显示余额")
				new Xianshi(z,"显示余额");
			else if(e.getActionCommand()=="转    账")
				new Zhuanzhang(z,"转账业务");
			else if(e.getActionCommand()=="查询修改")
				new Chagai(z,"查询修改");
			else if(e.getActionCommand()=="退  出") {
				dispose();//这里的z不是主页窗体
			}
			else if(e.getActionCommand()=="注  销") {

				String  str = JOptionPane.showInputDialog(null,"请输入正确的密码：","@输入密码",0);
				Icon tb = new ImageIcon("bank/tb.jpg");//替换对话框图标
				int n = JOptionPane.showConfirmDialog(null,"是否确定注销","注销！！！",JOptionPane.YES_NO_OPTION,0,tb);
				if(n==JOptionPane.YES_OPTION){
					double a=(Shujuk.xianshi());
					if(a<0) {
						int b=(Shujuk.shanchu(str,Denlu.Kahao.getText()));
						if(b==1){
							JOptionPane.showMessageDialog(Zhuye.this,"注销成功！");
							dispose();
							new Denlu();
						}
						else if(b==0)
							JOptionPane.showMessageDialog(Zhuye.this,"密码错误！");
						else if(b==-1)
							JOptionPane.showMessageDialog(Zhuye.this,"系统错误！");
					}
					else
						JOptionPane.showMessageDialog(Zhuye.this,"！！！账户仍有余额，请取出剩余的钱再注销");
				}
				else if(n==JOptionPane.NO_OPTION) {}
			}

		}
	}
}
